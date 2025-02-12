################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/cisco_meraki_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging
from cisco_integrations.meraki_sdk_client import MerakiSDKClient
from meraki.exceptions import APIError

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

    def get_networks(self):
        return self.client.get_networks(organization_id=self.organization_id)

    def get_organization_networks(self):
        return self.dashboard.organizations.getOrganizationNetworks(self.organization_id)

    def get_network_by_id(self, network_id: str):
        return self.client.get_network_by_id(
            organization_id=self.organization_id,
            network_id=network_id
        )

    def get_organization_inventory_devices(self):
        """
        Retrieve all devices in the organization's inventory.
        If there's a 404 (invalid org?), return a JSON error.
        """
        try:
            return self.dashboard.organizations.getOrganizationInventoryDevices(self.organization_id)
        except APIError as e:
            if e.status == 404:
                logging.error(f"404 Not Found from Meraki while listing inventory for org {self.organization_id}. Error: {e}")
                return {
                    "error": (
                        "404 Not Found: Possibly invalid organization ID or no inventory found "
                        f"for org '{self.organization_id}'."
                    )
                }
            else:
                logging.error(f"Meraki API error for org {self.organization_id}: {e}")
                return {"error": str(e)}

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
        from meraki.exceptions import APIError

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
        all_clients = self.list_all_clients_in_org(timespan=timespan)
        # Convert search to lowercase for case-insensitive matching
        name_substring = name_substring.lower()
        
        matched = [
            c for c in all_clients
            if name_substring in (c.get("description") or "").lower() 
            or name_substring in (c.get("dhcpHostname") or "").lower()
        ]
        return matched

    def get_organization_licenses_overview(self):
        """
        Retrieve license usage/overview data for the org.
        Official method: getOrganizationLicensesOverview(organizationId)
        """
        from meraki.exceptions import APIError

        try:
            overview = self.dashboard.organizations.getOrganizationLicensesOverview(self.organization_id)
            return overview
        except APIError as e:
            if e.status == 404:
                # Fallback or return a friendlier message
                return {"error": "404: Organization does not support co-term license overview."}
            else:
                raise

    def get_network_alerts_history(self, network_id: str):
        """
        Retrieve alert history for a specific network (GET /networks/{networkId}/alerts/history).

        - First checks if the network_id is valid/exists under the current organization.
        - If not found or 404 occurs, logs an error and returns a more descriptive message.
        """
        from meraki.exceptions import APIError

        # 1) Check if the network_id actually belongs to this organization
        try:
            org_networks = self.dashboard.organizations.getOrganizationNetworks(self.organization_id)
        except APIError as e:
            logging.error(f"Failed to list networks for org {self.organization_id}: {e}")
            return {"error": f"Cannot list networks for org {self.organization_id}: {e}"}

        # 2) See if network_id is in that list
        valid_network_ids = [net["id"] for net in org_networks]
        if network_id not in valid_network_ids:
            error_msg = (
                f"Network ID '{network_id}' not found in org '{self.organization_id}'. "
                f"Check that you have the correct network ID and organization."
            )
            logging.warning(error_msg)
            return {"error": error_msg}

        # 3) If it’s valid, attempt to retrieve alerts
        try:
            alerts_history = self.dashboard.networks.getNetworkAlertsHistory(network_id)
            return alerts_history

        except APIError as e:
            if e.status == 404:
                # Could be no alert history or brand-new network
                logging.error(
                    f"404 Not Found from Meraki (getNetworkAlertsHistory). Possibly no alert "
                    f"history yet or invalid network. Error: {e}"
                )
                return {
                    "error": (
                        "404 from Meraki getNetworkAlertsHistory. Possibly no alerts exist yet for "
                        f"network '{network_id}' or it’s brand-new. Details: {e}"
                    )
                }
            else:
                # If different error code, re-raise or handle as needed
                logging.error(f"Meraki API error: {e}")
                return {"error": str(e)}
            
    def get_network_clients(self, network_id: str):
        """
        Retrieve a list of clients for a given network.
        Official method: getNetworkClients(networkId, timespan=..., etc.)
        """
        return self.dashboard.networks.getNetworkClients(network_id)

    def get_organization_wireless_ssids(self):
        """
        Retrieves SSIDs across all Meraki networks in the organization that have 'wireless' product type.
        Internally calls getNetworkWirelessSsids(network_id) for each wireless-capable network.
        
        Returns a dict keyed by network_id, with the value being the list of SSIDs for that network:
        {
            "<net_id_1>": [{...}, {...}, ...],  # SSID dictionaries
            "<net_id_2>": [...],
            ...
        }
        """
        from meraki.exceptions import APIError

        results = {}
        try:
            # 1) Fetch all networks in the org
            org_networks = self.dashboard.organizations.getOrganizationNetworks(self.organization_id)

            # 2) Filter networks that have wireless
            for net in org_networks:
                net_id = net["id"]
                product_types = net.get("productTypes", [])
                if "wireless" in product_types:
                    # 3) Attempt to get SSIDs for this *wireless* network
                    try:
                        ssids = self.dashboard.wireless.getNetworkWirelessSsids(net_id)
                        results[net_id] = ssids
                    except APIError as e:
                        # Possibly a 404 if newly created or no SSIDs
                        logging.error(f"Error retrieving SSIDs for network {net_id}: {e}")
                        results[net_id] = {"error": str(e)}
                else:
                    # Not a wireless network, skip or store empty
                    results[net_id] = {"message": "Not a wireless-capable network"}

        except APIError as e:
            logging.error(f"Meraki API error listing networks for org {self.organization_id}: {e}")
            return {"error": str(e)}
        except Exception as e:
            logging.error(f"Unexpected error listing networks in org {self.organization_id}: {e}")
            return {"error": str(e)}

        return results

    def get_organization_inventory_device(self, device_id: str):
        """
        Retrieve details for a single device from the org inventory.
        Note: device_id must be the **Serial** number, not the MAC address.
        """
        try:
            return self.dashboard.organizations.getOrganizationInventoryDevice(
                self.organization_id,
                device_id
            )
        except APIError as e:
            if e.status == 404:
                logging.error(
                    f"404 Not Found: Device '{device_id}' not found in inventory for org '{self.organization_id}' "
                    f"or invalid device_id (remember to use the device serial). Error: {e}"
                )
                return {
                    "error": (
                        "Device not found or invalid device_id. Make sure you're using the device's SERIAL, "
                        "not the MAC address."
                    )
                }
            else:
                logging.error(f"Meraki API error retrieving device {device_id}: {e}")
                return {"error": str(e)}

    def get_all_access_points(self):
        """
        Retrieves all access points from the organization's inventory by filtering
        for devices whose model string starts with 'MR' (Meraki access point).
        Returns a JSON-like dict that includes a message for your chat interface.
        """
        from meraki.exceptions import APIError

        print("Retrieving all APs from the Meraki inventory. This may take a few seconds...")

        try:
            # Let the chat UI know the operation may take a bit
            info_message = "Retrieving all APs from the Meraki inventory. This may take a few seconds..."

            # 1) List all devices in the organization
            devices = self.dashboard.organizations.getOrganizationInventoryDevices(
                self.organization_id,
                total_pages="all"  # Automatically handle pagination
            )

            # 2) Filter for models starting with 'MR'
            access_points = [
                d for d in devices
                if d.get("model", "").startswith("MR")
            ]

            # Return a JSON-like structure with a message and results
            return {
                "status": "success",
                "message": info_message,
                "access_points": access_points
            }

        except APIError as e:
            # Handle Meraki API errors
            logging.error(f"Meraki API error retrieving inventory for org {self.organization_id}: {e}")
            return {
                "status": "error",
                "message": str(e),
                "access_points": []
            }
        except Exception as ex:
            # Catch any unexpected exceptions
            error_msg = f"Unexpected error retrieving APs for org {self.organization_id}: {ex}"
            logging.error(error_msg)
            return {
                "status": "error",
                "message": error_msg,
                "access_points": []
            }

    def get_organization_login_security(self):
        """
        Retrieve login security settings for the org.
        Official method: getOrganizationLoginSecurity(organizationId)
        """
        try:
            login_security = self.dashboard.organizations.getOrganizationLoginSecurity(self.organization_id)
            return login_security
        except APIError as e:
            if e.status == 404:
                # The org doesn't support or hasn't initialized the loginSecurity endpoint
                return {
                    "error": (
                        "404 Not Found: This organization either does not "
                        "support loginSecurity or isn't fully provisioned."
                    )
                }
            else:
                raise

    def list_all_switches_in_org(self):
        """
        Retrieve all Meraki switch devices (models starting with 'MS') 
        in the organization's inventory using the official Meraki library.
        """
        from meraki.exceptions import APIError

        try:
            # 1) List all devices in the org’s inventory (auto-paginated)
            inventory_devices = self.dashboard.organizations.getOrganizationInventoryDevices(
                self.organization_id,
                total_pages="all"
            )

            # 2) Filter out only the devices whose model starts with 'MS'
            switches = [dev for dev in inventory_devices if dev.get("model", "").startswith("MS")]
            return switches

        except APIError as e:
            if e.status == 404:
                # Org not found or no inventory
                error_msg = (
                    f"404 Not Found: Possibly invalid organization ID or no devices found "
                    f"for org '{self.organization_id}'. Error: {e}"
                )
                return {"error": error_msg}
            else:
                # Some other Meraki API error
                return {"error": str(e)}
        except Exception as ex:
            # Catch-all for unexpected exceptions
            error_msg = f"Unexpected error listing switches for org {self.organization_id}: {ex}"
            return {"error": error_msg}

    def list_all_cameras_in_org(self):
        """
        Retrieve all Meraki camera devices in the organization using the
        'getOrganizationCameraOnboardingStatuses' endpoint.
        Returns a list of camera onboarding status objects, e.g.:
        [
            {
                "networkId": "N_12345",
                "serial": "Q2AB-CDEF-GHIJ",
                "status": "pending onboarding",
                "updatedAt": "2021/03/24 15:23:47.101068 -0700"
            },
            ...
        ]
        """
        from meraki.exceptions import APIError

        try:
            # Call the official Meraki camera endpoint
            camera_statuses = self.dashboard.camera.getOrganizationCameraOnboardingStatuses(
                self.organization_id
            )
            return camera_statuses

        except APIError as e:
            if e.status == 404:
                # Possibly invalid org ID or no cameras
                error_msg = (
                    f"404 Not Found: Possibly invalid organization ID '{self.organization_id}' "
                    f"or no camera data available. Error: {e}"
                )
                return {"error": error_msg}
            else:
                return {"error": str(e)}
        except Exception as ex:
            # Catch-all for unexpected exceptions
            error_msg = f"Unexpected error retrieving cameras for org {self.organization_id}: {ex}"
            return {"error": error_msg}

    def get_meraki_network_devices(self, network_id: str):
        """
        GET /networks/{networkId}/devices
        """
        return self.dashboard.networks.getNetworkDevices(network_id)

    def get_meraki_device_switch_ports(self, serial: str):
        """
        GET /devices/{serial}/switchPorts
        Uses the Meraki Python library's 'switch' group 
        to retrieve all switch ports for the given device.
        """
        try:
            return self.dashboard.switch.getDeviceSwitchPorts(serial)
        except APIError as e:
            if e.status == 404:
                # The device serial was not found in Meraki’s inventory
                return {
                    "error": (
                        f"404 Not Found: Could not find device with serial '{serial}'. "
                        "Please check the serial number and try again."
                    )
                }
            else:
                # For any other Meraki API error, you can either re-raise or handle differently
                return {"error": f"Meraki API error: {str(e)}"}

    def get_meraki_network_wireless_ssids(self, network_id: str):
        """
        GET /networks/{networkId}/wireless/ssids
        """
        return self.dashboard.wireless.getNetworkWirelessSsids(network_id)

    def list_all_devices_in_org(self):
        """
        Retrieves all Meraki devices in the inventory for the organization
        (GET /organizations/{organizationId}/inventory/devices).
        """
        from meraki.exceptions import APIError
        
        try:
            # Official method from the Meraki Python library:
            # getOrganizationInventoryDevices(org_id, total_pages='all', ...)
            devices = self.dashboard.organizations.getOrganizationInventoryDevices(
                self.organization_id,
                total_pages='all'  # auto-paginates for large orgs
            )
            return devices
        except APIError as e:
            # If Meraki returns an error (invalid org, etc.), handle it
            error_msg = f"Meraki API error listing devices for org {self.organization_id}: {e}"
            logging.error(error_msg)
            return {"error": error_msg}
        except Exception as ex:
            # Catch-all for unexpected exceptions
            error_msg = f"Unexpected error listing devices for org {self.organization_id}: {ex}"
            logging.error(error_msg)
            return {"error": error_msg}
