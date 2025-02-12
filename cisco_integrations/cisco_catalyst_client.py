################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/cisco_catalyst_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

from .base_client import BaseCiscoClient
from dnacentersdk import DNACenterAPI, ApiError
import logging
import requests 

class CatalystCenterClient(BaseCiscoClient):
    """
    Client for Cisco Catalyst Center (DNA Center) that uses dnacentersdk.
    """
    def __init__(
        self,
        base_url: str,
        token: str = None,
        dnac_username: str = None,
        dnac_password: str = None,
        dnac_encoded_auth: str = None,
        dnac_verify: bool = False,
        dnac_version: str = "2.3.7.6"
    ):
        super().__init__(base_url, token)
        try:
            if dnac_encoded_auth:
                self.sdk = DNACenterAPI(
                    encoded_auth=dnac_encoded_auth,
                    base_url=base_url,
                    verify=dnac_verify,
                    version=dnac_version
                )
            elif dnac_username and dnac_password:
                self.sdk = DNACenterAPI(
                    username=dnac_username,
                    password=dnac_password,
                    base_url=base_url,
                    verify=dnac_verify,
                    version=dnac_version
                )
            else:
                self.sdk = DNACenterAPI(
                    base_url=base_url,
                    verify=dnac_verify,
                    version=dnac_version
                )
            logging.info("DNACenterAPI client successfully created.")
        except Exception as e:
            logging.error(f"Error creating DNACenterAPI client: {e}")
            self.sdk = None

    def get_all_devices(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return []
        try:
            devices = self.sdk.devices.get_device_list()
            return devices.response if hasattr(devices, 'response') else devices
        except ApiError as e:
            logging.error(f"API Error retrieving devices: {e}")
            return []
        except Exception as ex:
            logging.error(f"Unknown error retrieving devices: {ex}")
            return []

    def get_device_by_id(self, device_id):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return None
        try:
            return self.sdk.devices.get_device_by_id(id=device_id)
        except ApiError as e:
            logging.error(f"API Error retrieving device {device_id}: {e}")
            return None
        except Exception as ex:
            logging.error(f"Unknown error retrieving device {device_id}: {ex}")
            return None

    def run_cli_command(self, device_id: str, command: str):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            payload = {"commands": [command], "deviceUuids": [device_id]}
            response = self.sdk.command_runner.run_read_only_commands_on_devices(payload=payload)
            return {"message": "Command accepted. Check status with taskId.", "data": response}
        except Exception as e:
            logging.error(f"Error running CLI command: {e}")
            return {"error": str(e)}

    def get_task_status_by_id(self, task_id: str):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            return self.sdk.task.get_task_by_id(task_id=task_id)
        except ApiError as e:
            logging.error(f"API Error retrieving task {task_id}: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error retrieving task {task_id}: {ex}")
            return {"error": str(ex)}

    def fetch_command_output_by_file_id(self, file_id):
        try:
            url = f"/dna/intent/api/v1/file/{file_id}"
            return self.sdk.custom_caller.call_api("GET", url)
        except ApiError as e:
            return {"error": f"Failed to retrieve file: {e}"}

    def get_all_sites(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            response = self.sdk.sites.get_site()
            return response.get('response', [])
        except ApiError as e:
            logging.error(f"API Error retrieving sites: {e}")
            return {"error": f"Failed to retrieve sites: {e}"}
        except Exception as ex:
            logging.error(f"Unknown error retrieving sites: {ex}")
            return {"error": f"Unknown error: {ex}"}
    
    def get_all_ssids(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}

        try:
            ssid_list = self.sdk.wireless.get_enterprise_ssid()
            # Since this returns a list, just return it directly:
            return ssid_list

        except ApiError as e:
            logging.error(f"API Error retrieving SSIDs: {e}")
            return {"error": f"Failed to retrieve SSIDs: {e}"}
        except Exception as ex:
            logging.error(f"Unknown error retrieving SSIDs: {ex}")
            return {"error": f"Unknown error: {ex}"}


    def get_site_by_name_v1(self, site_name: str):
        """
        Uses DNA Center v1 endpoint /dna/intent/api/v1/site
        with the query param `name` = site_name
        Returns JSON data if available.
        """
        if not self.sdk and not self.token:
            logging.error("No DNACenterAPI client or token available.")
            return {"error": "DNACenterAPI client or token not initialized."}

        # Build the full URL. e.g. https://sandboxdnac.cisco.com
        url = f"{self.base_url}/dna/intent/api/v1/site"

        # Use the stored token or dnacentersdk's access token
        headers = {
            "Accept": "application/json",
            "X-Auth-Token": self.token if self.token else self.sdk.access_token
        }

        # Pass the site name hierarchy via query params
        # For v1, you use 'name' instead of 'groupNameHierarchy'
        params = {
            "name": site_name  # E.g. "Global/Antartica3"
        }

        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30, verify=False)
            resp.raise_for_status()
            # Convert response to JSON
            json_data = resp.json()
            # The v1 "get_site" response typically has a "response" key that is a list
            return json_data.get("response", json_data)
        except requests.RequestException as e:
            logging.error(f"Request error retrieving site by name '{site_name}': {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error retrieving site by name '{site_name}': {ex}")
            return {"error": str(ex)}

    def get_catalyst_system_info(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            response = self.sdk.custom_caller.call_api("GET", "/dna/intent/api/v1/nodes-config")
            return response.get("response", {})
        except ApiError as e:
            logging.error(f"API Error retrieving system info: {e}")
            return {"error": f"Failed to retrieve system info: {e}"}
        except Exception as ex:
            logging.error(f"Unknown error retrieving system info: {ex}")
            return {"error": f"Unknown error: {ex}"}

    def get_dnac_packages_summary(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            response = self.sdk.custom_caller.call_api("GET", "/dna/intent/api/v1/dnac-packages")
            return response.get("response", [])
        except ApiError as e:
            logging.error(f"API Error retrieving packages summary: {e}")
            return {"error": f"Failed to retrieve packages summary: {e}"}
        except Exception as ex:
            logging.error(f"Unknown error retrieving packages summary: {ex}")
            return {"error": f"Unknown error: {ex}"}

    def get_all_interfaces(self):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            response = self.sdk.custom_caller.call_api("GET", "/dna/intent/api/v1/interface")
            return response.get("response", [])
        except Exception as e:
            logging.error(f"Error retrieving interfaces: {e}")
            return {"error": f"Failed to retrieve interfaces: {e}"}

    def get_device_interfaces(self, device_id):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            endpoint = f"/dna/intent/api/v1/interface/network-device/{device_id}"
            response = self.sdk.custom_caller.call_api("GET", endpoint)
            return response.get("response", [])
        except Exception as e:
            logging.error(f"Error retrieving interfaces for device {device_id}: {e}")
            return {"error": f"Failed to retrieve interfaces for device {device_id}: {e}"}

    def get_interfaces_by_ip(self, ip_address: str):
        """
        Retrieve interfaces for a specific management IP address from DNA Center.
        Customized to provide clearer messages for 401/404 errors.
        """
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}

        endpoint = f"/dna/intent/api/v1/interface/ip-address/{ip_address}"

        try:
            response = self.sdk.custom_caller.call_api("GET", endpoint)
            return response.get("response", [])

        except ApiError as e:
            # The dnacentersdk ApiError often includes response details and status code.
            status_code = getattr(e, 'status_code', None)
            error_msg = str(e)

            if status_code == 404:
                # 404 usually means "resource not found"
                # Possibly the IP doesn't exist or isn't in DNAC inventory.
                user_friendly = (
                    f"404 Not Found: The IP '{ip_address}' may be spelled incorrectly, "
                    "or no device with that management IP is discovered in DNAC."
                )
                logging.error(user_friendly)
                return {"error": user_friendly, "details": error_msg}

            elif status_code == 401:
                # 401 usually means "unauthorized" or invalid token
                user_friendly = (
                    "401 Unauthorized: Authentication to DNAC failed or expired. "
                    "Check your token/credentials. If your environment returns 401 "
                    "for unknown IPs, ensure the IP is typed correctly."
                )
                logging.error(user_friendly)
                return {"error": user_friendly, "details": error_msg}

            else:
                # For other codes, just fallback to the generic message
                logging.error(f"API Error retrieving interfaces for IP {ip_address}: {error_msg}")
                return {"error": f"Failed to retrieve interfaces for IP {ip_address}: {error_msg}"}

        except Exception as ex:
            logging.error(f"Unknown error retrieving interfaces for IP {ip_address}: {ex}")
            return {"error": f"Failed to retrieve interfaces for IP {ip_address}: {ex}"}

    def initiate_path_trace(self, source_ip, destination_ip):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            payload = {"sourceIP": source_ip, "destIP": destination_ip}
            response = self.sdk.custom_caller.call_api("POST", "/dna/intent/api/v1/flow-analysis", json=payload)
            logging.debug(f"Path trace response: {response}")
            return response
        except Exception as e:
            logging.error(f"Error initiating path trace: {e}")
            return {"error": f"Failed to initiate path trace: {e}"}

    def get_path_trace_result(self, flow_analysis_id):
        if not self.sdk:
            logging.error("DNACenterAPI client not initialized.")
            return {"error": "DNACenterAPI client not initialized."}
        try:
            if not flow_analysis_id:
                raise ValueError("Flow Analysis ID must be provided.")
            endpoint = f"/dna/intent/api/v1/flow-analysis/{flow_analysis_id}"
            response = self.sdk.custom_caller.call_api("GET", endpoint)
            logging.debug(f"Path trace result response: {response}")
            return response
        except ValueError as ve:
            logging.error(f"Validation Error: {ve}")
            return {"error": str(ve)}
        except Exception as e:
            logging.error(f"Error retrieving path trace result: {e}")
            return {"error": f"Failed to retrieve path trace result: {e}"}

    def get_device_list_direct(self):
        if not self.sdk and not self.token:
            logging.error("No DNACenterAPI client or token.")
            return {"error": "No DNACenterAPI client or token."}

        url = f"{self.base_url}/dna/intent/api/v1/network-device"
        headers = {
            "Accept": "application/json",
            "X-Auth-Token": self.token if self.token else self.sdk.access_token
        }
        try:
            resp = requests.get(url, headers=headers, timeout=30, verify=False)
            resp.raise_for_status()
            json_data = resp.json()
            return json_data.get("response", json_data)
        except Exception as e:
            logging.error(f"Error retrieving device list: {e}")
            return {"error": str(e)}

    def get_device_detail_direct(self, identifier: str, search_by: str):
        """
        Calls /dna/intent/api/v1/device-detail?identifier={identifier}&searchBy={search_by}
        to retrieve device details (e.g. inventory or extended info).
        """
        if not self.token and not self.sdk:
            logging.error("No DNACenterAPI client or token available.")
            return {"error": "No DNACenterAPI client or token."}

        # Build the URL with query parameters
        url = f"{self.base_url}/dna/intent/api/v1/device-detail"
        params = {
            "identifier": identifier,
            "searchBy": search_by
        }

        # Use the stored token or dnacentersdk access token
        headers = {
            "Accept": "application/json",
            "X-Auth-Token": self.token if self.token else self.sdk.access_token
        }

        try:
            # Do the GET request
            response = requests.get(
                url, 
                headers=headers, 
                params=params, 
                timeout=30, 
                verify=False  # or True if you have valid certs
            )
            response.raise_for_status()
            json_data = response.json()
            return json_data.get("response", json_data)
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error retrieving device detail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error retrieving device detail: {ex}")
            return {"error": str(ex)}

    def get_device_detail_by_name(self, device_name: str):
        """
        Wraps get_device_detail_direct, specifying identifier="nwDeviceName"
        """
        return self.get_device_detail_direct("nwDeviceName", device_name)

    def get_device_detail_by_mac(self, mac_address: str):
        """
        Wraps get_device_detail_direct, specifying identifier="macAddress"
        """
        return self.get_device_detail_direct("macAddress", mac_address)

    def get_all_devices_by_site(self, site_id: str):
        """
        Retrieves all devices for the given site ID from DNAC v1 endpoint:
        /dna/intent/api/v1/network-device/site/{siteId}
        """
        if not self.token and not self.sdk:
            logging.error("No DNACenterAPI client or token available.")
            return {"error": "No DNACenterAPI client or token."}

        # Construct the endpoint
        base_url = self.base_url.rstrip("/")
        url = f"{base_url}/dna/intent/api/v1/network-device/site/{site_id}"

        headers = {
            "Accept": "application/json",
            "X-Auth-Token": self.token if self.token else self.sdk.access_token
        }

        try:
            resp = requests.get(url, headers=headers, timeout=30, verify=False)
            resp.raise_for_status()
            json_data = resp.json()
            # Typically returns {"response": [ {device1}, {device2}, ... ], ...}
            return json_data.get("response", json_data)
        except requests.RequestException as e:
            logging.error(f"Request error retrieving devices by site '{site_id}': {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error retrieving devices by site '{site_id}': {ex}")
            return {"error": str(ex)}
