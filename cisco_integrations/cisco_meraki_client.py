################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/cisco_meraki_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging
import meraki
from meraki.exceptions import APIError

class MerakiSDKClient:
    """
    A thin wrapper around the official Meraki Dashboard API.
    """
    def __init__(self, api_key: str, base_url: str = None):
        if not meraki:
            raise ImportError("The 'meraki' Python package is not installed. Please install via 'pip install meraki'.")
        self.api_key = api_key
        self.dashboard = meraki.DashboardAPI(
            api_key=api_key,
            base_url=base_url or "https://api.meraki.com/api/v1",
            print_console=False,
        )
        logging.info("MerakiSDKClient initialized.")

class CiscoMerakiClient:
    def __init__(self, api_key: str, organization_id: str):
        """
        Initialize the Cisco Meraki client.
        """
        self.organization_id = organization_id
        # Create the underlying Meraki SDK client.
        logging.info(f"Initializing CiscoMerakiClient with organization_id: '{self.organization_id}'")
        self.client = MerakiSDKClient(api_key=api_key)
        # Expose the dashboard attribute so that unified_service.py can access it.
        self.dashboard = self.client.dashboard

# functions that are “aggregator” or multi-step logic methods instead of simple direct single-GET calls

    def list_all_clients_in_org(self, timespan=60 * 60 * 24 * 14):
        """
        Returns a list of all clients across all networks in the organization,
        optionally limited by a timespan (default 14 days).

        Example return format:
        [
          {
            "mac": "00:11:22:33:44:55",
            "description": "John's iPhone",
            "ip": "192.168.0.10",
            ...other Meraki fields...
          },
          ...
        ]
        """
        all_clients = []

        # 1) Get all networks in the org
        networks = self.dashboard.organizations.getOrganizationNetworks(self.organization_id)

        # 2) For each network, retrieve its clients
        for net in networks:
            net_id = net["id"]
            try:
                clients = self.dashboard.networks.getNetworkClients(
                    networkId=net_id,
                    timespan=timespan,       # How many seconds back to look
                    perPage=1000,
                    total_pages="all"        # auto-paginate
                )
                # 3) Append clients to our combined list
                all_clients.extend(clients)
            except APIError as e:
                logging.error(f"Meraki API error for network {net_id}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error for network {net_id}: {e}")

        return all_clients

    def list_all_clients_in_org_by_name(self, name_substring: str, timespan=60 * 60 * 24 * 14):
        """
        Searches all clients (over a given timespan) whose description or hostname
        contains the case-insensitive substring `name_substring`.
        """
        all_clients = self.list_all_clients_in_org(timespan=timespan)
        name_substring = name_substring.lower()
        
        matched = [
            c for c in all_clients
            if name_substring in (c.get("description") or "").lower()
               or name_substring in (c.get("dhcpHostname") or "").lower()
        ]
        return matched

    def get_network_alerts_history(self, network_id: str):
        """
        Retrieve alert history for a specific network (GET /networks/{networkId}/alerts/history).

        - First checks if the network_id belongs to this org (thus aggregator logic).
        - If valid, calls getNetworkAlertsHistory.
        - Returns a friendlier error if 404 or network not found.
        """
        # 1) Check if network_id belongs to the current organization
        try:
            org_networks = self.dashboard.organizations.getOrganizationNetworks(self.organization_id)
        except APIError as e:
            logging.error(f"Failed to list networks for org {self.organization_id}: {e}")
            return {"error": f"Cannot list networks for org {self.organization_id}: {e}"}

        valid_network_ids = [net["id"] for net in org_networks]
        if network_id not in valid_network_ids:
            error_msg = (
                f"Network ID '{network_id}' not found in org '{self.organization_id}'. "
                "Check that you have the correct network ID and organization."
            )
            logging.warning(error_msg)
            return {"error": error_msg}

        # 2) If it’s valid, attempt to retrieve alerts
        try:
            alerts_history = self.dashboard.networks.getNetworkAlertsHistory(network_id)
            return alerts_history
        except APIError as e:
            if e.status == 404:
                logging.error(
                    f"404 Not Found from Meraki getNetworkAlertsHistory. Possibly no alerts yet or invalid network. Error: {e}"
                )
                return {
                    "error": (
                        f"404 from Meraki getNetworkAlertsHistory. Possibly no alerts exist yet for network '{network_id}'"
                        f" or brand-new network. Details: {e}"
                    )
                }
            else:
                logging.error(f"Meraki API error: {e}")
                return {"error": str(e)}

    def get_all_access_points(self):
        """
        Retrieves all access points from the organization's inventory by filtering
        for devices whose model starts with 'MR'.
        """
        print("Retrieving all APs from the Meraki inventory. This may take a few seconds...")

        try:
            info_message = "Retrieving all APs from the Meraki inventory. This may take a few seconds..."

            # 1) List all devices in the organization
            devices = self.dashboard.organizations.getOrganizationInventoryDevices(
                self.organization_id,
                total_pages="all"
            )

            # 2) Filter for models starting with 'MR'
            access_points = [d for d in devices if d.get("model", "").startswith("MR")]

            return {
                "status": "success",
                "message": info_message,
                "access_points": access_points
            }
        except APIError as e:
            logging.error(f"Meraki API error retrieving APs for org {self.organization_id}: {e}")
            return {
                "status": "error",
                "message": str(e),
                "access_points": []
            }
        except Exception as ex:
            error_msg = f"Unexpected error retrieving APs for org {self.organization_id}: {ex}"
            logging.error(error_msg)
            return {
                "status": "error",
                "message": error_msg,
                "access_points": []
            }

    def list_all_switches_in_org(self):
        """
        Retrieve all Meraki switches (models starting with 'MS') from the inventory.
        """
        try:
            # 1) List all devices in the org inventory
            inventory_devices = self.dashboard.organizations.getOrganizationInventoryDevices(
                self.organization_id,
                total_pages="all"
            )
            # 2) Filter out only the devices whose model starts with 'MS'
            return [dev for dev in inventory_devices if dev.get("model", "").startswith("MS")]
        except APIError as e:
            if e.status == 404:
                error_msg = (
                    f"404 Not Found: Possibly invalid org ID '{self.organization_id}' or no devices found. Error: {e}"
                )
                return {"error": error_msg}
            else:
                return {"error": str(e)}
        except Exception as ex:
            error_msg = f"Unexpected error listing switches for org {self.organization_id}: {ex}"
            return {"error": error_msg}

    def list_all_cameras_in_org(self):
        """
        Retrieve all Meraki cameras in the organization by calling getOrganizationCameraOnboardingStatuses,
        then returning them in a list.
        """
        try:
            camera_statuses = self.dashboard.camera.getOrganizationCameraOnboardingStatuses(self.organization_id)
            return camera_statuses
        except APIError as e:
            if e.status == 404:
                error_msg = (
                    f"404 Not Found: Possibly invalid org ID '{self.organization_id}' or no camera data. Error: {e}"
                )
                return {"error": error_msg}
            else:
                return {"error": str(e)}
        except Exception as ex:
            error_msg = f"Unexpected error retrieving cameras for org {self.organization_id}: {ex}"
            return {"error": error_msg}
