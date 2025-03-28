################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/unified_service.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging
import os
from dotenv import load_dotenv

load_dotenv()
# Read integration flags from environment
ENABLE_CATALYST_CENTER = os.getenv("ENABLE_CATALYST_CENTER", "false").lower() == "true"
print("ENABLE_CATALYST_CENTER HERE: ", ENABLE_CATALYST_CENTER)
ENABLE_MERAKI = os.getenv("ENABLE_MERAKI", "true").lower() == "true"
print("ENABLE_MERAKI: ", ENABLE_MERAKI)
ENABLE_CISCO_SPACES = os.getenv("ENABLE_CISCO_SPACES", "true").lower() == "true"
print("ENABLE_CISCO_SPACES: ", ENABLE_CISCO_SPACES)
ENABLE_CISCO_WEBEX = os.getenv("ENABLE_CISCO_WEBEX", "false").lower() == "true"
print("ENABLE_CISCO_WEBEX: ", ENABLE_CISCO_WEBEX)

# Import platform-specific clients only if enabled
if ENABLE_CATALYST_CENTER:
    from cisco_integrations.cisco_catalyst_client import CatalystCenterClient
if ENABLE_MERAKI:
    from cisco_integrations.cisco_meraki_client import CiscoMerakiClient
if ENABLE_CISCO_SPACES:
    from cisco_integrations.cisco_spaces_client import CiscoSpacesClient
if ENABLE_CISCO_WEBEX:
    from cisco_integrations.cisco_webex_client import CiscoWebexClient

class CiscoUnifiedService:
    def __init__(
        self,
        catalyst_username=None,
        catalyst_password=None,
        catalyst_url=None,
        catalyst_version=None,
        meraki_api_key=None,
        spaces_token=None,
        webex_token=None,
    ):
        # -------------------------
        # Catalyst Center Integration
        # -------------------------
        if ENABLE_CATALYST_CENTER:
            self.catalyst_client = CatalystCenterClient(
                base_url=catalyst_url,
                token=None,
                dnac_username=catalyst_username,
                dnac_password=catalyst_password,
                dnac_encoded_auth=None,
                dnac_verify=False,
                dnac_version=catalyst_version
            )
        else:
            self.catalyst_client = None
            logging.info("Catalyst Center integration is disabled.")

        # -------------------------
        # Meraki Integration
        # -------------------------
        if ENABLE_MERAKI:
            # Always use the organization ID from the environment; user cannot override it.
            self.meraki_org_id = os.getenv("MERAKI_ORG_ID", "")
            logging.info(f"MERAKI_ORG_ID from environment: '{self.meraki_org_id}'")
            if not self.meraki_org_id:
                logging.warning("MERAKI_ORG_ID is not set in the environment.")
            self.meraki_client = CiscoMerakiClient(
                api_key=meraki_api_key,
                organization_id=self.meraki_org_id
            ) if meraki_api_key else None
        else:
            self.meraki_client = None
            logging.info("Meraki integration is disabled.")

        # -------------------------
        # Cisco Spaces Integration
        # -------------------------
        if ENABLE_CISCO_SPACES:
            self.spaces_client = CiscoSpacesClient(
                base_url=None,  # Will use CISCO_SPACES_BASE_URL from environment if not provided.
                api_key=spaces_token
            )
        else:
            self.spaces_client = None
            logging.info("Cisco Spaces integration is disabled.")

        # -------------------------
        # Cisco Webex Integration
        # -------------------------
        if ENABLE_CISCO_WEBEX:
            self.webex_client = CiscoWebexClient(token=webex_token)
        else:
            self.webex_client = None
            logging.info("Cisco Webex integration is disabled or token not provided.")

        logging.info("CiscoUnifiedService initialized with enabled integrations: "
                     "Catalyst: {}, Meraki: {}, Spaces: {}, Webex: {}."
                     .format(ENABLE_CATALYST_CENTER, ENABLE_MERAKI, ENABLE_CISCO_SPACES, ENABLE_CISCO_WEBEX))

    # ================================
    # Meraki Methods
    # ================================

    def list_all_clients_in_org(self, timespan=60 * 60 * 24 * 14):
        """
        Lists all Meraki clients across all networks in the organization,
        optionally limited by a timespan (default 14 days).
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # This calls the method you defined in cisco_meraki_client.py
        return self.meraki_client.list_all_clients_in_org(timespan=timespan)
    
    def list_all_clients_in_org_by_name(self, name_substring: str, timespan=60 * 60 * 24 * 14):
        """
        Delegate to the Meraki client. Lists all clients in the org, 
        filters them by substring match against description/hostname.
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # Call the function you defined in cisco_meraki_client.py
        return self.meraki_client.list_all_clients_in_org_by_name(name_substring, timespan=timespan)

    def get_network_alerts_history(self, network_id: str):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}
        return self.meraki_client.get_network_alerts_history(network_id)

    def get_all_access_points(self):
        """
        Return all access points from the Meraki wireless controllers.
        """
        if not self.meraki_client:
            return {"error": "Meraki client not configured or Meraki is disabled."}

        return self.meraki_client.get_all_access_points()


    def list_all_switches_in_org(self):
        """
        Lists all Meraki switch devices (models starting with 'MS') in the org.
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # Delegate to the new method in CiscoMerakiClient
        return self.meraki_client.list_all_switches_in_org()

    def list_all_cameras_in_org(self):
        """
        Lists all Meraki cameras in the organization (onboarding statuses).
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        return self.meraki_client.list_all_cameras_in_org()
    

    # ================================
    # Meraki SDK Methods
    # ================================









    # ================================
    # Catalyst Methods (DNA Center)
    # ================================
    def get_all_catalyst_devices(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_devices()

    def get_catalyst_device_by_id(self, device_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_device_by_id(device_id)

    def run_cli_command_on_catalyst_device(self, device_id: str, command: str):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.run_cli_command(device_id, command)

    def get_catalyst_task_status_by_id(self, task_id: str):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_task_status_by_id(task_id)

    def get_command_output(self, file_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.fetch_command_output_by_file_id(file_id)

    def get_all_sites(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_sites()

    def get_all_ssids(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_ssids()

    def get_catalyst_system_info(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_catalyst_system_info()

    def get_dnac_packages_summary(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_dnac_packages_summary()

    def get_all_interfaces(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_interfaces()

    def get_device_interfaces(self, device_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_device_interfaces(device_id)

    def get_interfaces_by_ip(self, ip_address):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_interfaces_by_ip(ip_address)

    def initiate_path_trace(self, source_ip, destination_ip):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.initiate_path_trace(source_ip, destination_ip)

    def get_path_trace_result(self, flow_analysis_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_path_trace_result(flow_analysis_id)
 
    def get_catalyst_device_list_direct(self):
        if self.catalyst_client:
            return self.catalyst_client.get_device_list_direct()
        return {"error": "Catalyst client not available"}

    def get_catalyst_device_detail_by_name(self, device_name: str):
        """ Retrieve device detail by hostname. """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_device_detail_by_name(device_name)

    def get_catalyst_device_detail_by_mac_address(self, mac_address: str):
        """ Retrieve device detail by MAC address. """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_device_detail_by_mac(mac_address)
    

    def get_site_by_name(self, site_name: str):
        """
        Wraps the CatalystCenterClient's get_site_by_name_v2 method.
        """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_site_by_name_v2(site_name)

    def get_all_devices_by_site(self, site_id: str):
        """
        Calls CatalystCenterClient.get_all_devices_by_site
        to retrieve all devices for a given site ID.
        """
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_devices_by_site(site_id)

    # ================================
    # Catalyst Methods SDK (DNA Center)
    # ================================
















    # ================================
    # Cisco Spaces Methods
    # ================================
    
    def get_spaces_location_hierarchy(self, tenant_id=None):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_location_hierarchy(tenant_id)

    def get_organization_inventory_devices(self):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        return self.meraki_client.get_organization_inventory_devices()

    def get_organization_networks(self):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}
        return self.meraki_client.get_organization_networks()
    
    def get_spaces_floor_details(self, floor_id: str):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_floor_details(floor_id)

    def get_spaces_floor_image(self, tenant_id: str, image_path: str, image_type: str):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_floor_image(tenant_id, image_path, image_type)

    def get_spaces_devices(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)

    def get_spaces_devices_count(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_count(**kwargs)

    def get_spaces_devices_floors(self):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_floors()

    def export_history_csv(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.export_history_csv(**kwargs)

    def export_history_gz(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.export_history_gz(**kwargs)

    def get_history_record_count(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_count(**kwargs)

    def get_history_devices(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)

    def get_history_for_device(self, device_id: str, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)
    
    def get_spaces_location_subtree(self, location_id: str) -> dict:
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_location_subtree(location_id)


    # ================================
    # Cisco Webex Methods (Stubs)
    # ================================
    def get_webex_meetings(self):
        if not self.webex_client:
            return {"message": "Webex integration is disabled or not configured."}
        return self.webex_client.get_meetings()

    def get_webex_meeting_by_id(self, meeting_id):
        if not self.webex_client:
            return {"message": "Webex integration is disabled or not configured."}
        return self.webex_client.get_meeting_by_id(meeting_id)