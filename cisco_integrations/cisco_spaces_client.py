################################################################################
## cisco_integrations/cisco_spaces_client.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import logging
from typing import Any, Dict, Optional
from urllib.parse import quote

from .base_client import BaseCiscoClient

def _build_query(params: Dict[str, Any]) -> str:
    valid_items = []
    for k, v in params.items():
        if v is not None:
            if isinstance(v, bool):
                v = str(v).lower()
            valid_items.append(f"{k}={v}")
    if not valid_items:
        return ""
    return "?" + "&".join(valid_items)

class CiscoSpacesClient(BaseCiscoClient):
    def __init__(self, base_url: str = None, api_key: str = None):
        if base_url is None:
            base_url = os.getenv("CISCO_SPACES_BASE_URL", "https://dnaspaces.io")
        base_url = base_url.rstrip('/')
        if not api_key:
            api_key = os.getenv("CISCO_SPACES_API_KEY")
        if not api_key:
            raise ValueError("Missing Cisco Spaces API Key. "
                             "Set 'CISCO_SPACES_API_KEY' environment variable.")
        super().__init__(base_url=base_url, token=api_key)
        logging.info(f"CiscoSpacesClient initialized with base URL: {self.base_url}")

    def get_location_hierarchy(self, tenant_id: str = None) -> dict:
        endpoint = "api/location/v2/map/locationhierarchy"
        params = {"tenantId": tenant_id} if tenant_id else {}
        query_str = _build_query(params)
        try:
            return self._get(endpoint + query_str)
        except Exception as e:
            logging.error(f"Error retrieving location hierarchy: {e}")
            return {"error": "Failed to retrieve location hierarchy."}

    def get_floor_details(self, floor_id: str) -> dict:
        if not floor_id:
            return {"error": "Invalid floor ID provided."}
        
        encoded_floor_id = quote(floor_id, safe='')
        endpoint = f"api/location/v2/map/floor/{encoded_floor_id}"
        try:
            response = self._get(endpoint)
            if not response:
                return {"error": f"No details found for floor ID: {floor_id}"}
            return response
        except Exception as e:
            logging.error(f"Error retrieving floor details for {floor_id}: {e}")
            return {"error": "Failed to retrieve floor details. Please check if the floor ID is correct."}

    def get_floor_image(
        self,
        tenant_id: str,
        image_path: str,
        image_type: str,
        *,
        save_local: bool = False,
        local_filename: Optional[str] = None
    ) -> Any:
        """
        Fetch the floor image bytes from Cisco Spaces.
        If save_local=True, also write the file under app/assets/<local_filename>.
        Returns raw bytes if successful, or dict with {'error': ...} if failure.
        """
        endpoint = "api/location/v2/map/floor/image"
        params = {"tenantId": tenant_id, "imagePath": image_path, "imageType": image_type}
        query_str = _build_query(params)

        try:
            result = self._get(endpoint + query_str, return_json=False)
            # 'result' is either bytes or a dict with an error. Check:
            if isinstance(result, dict) and "error" in result:
                return result

            if save_local:
                # Default name if none given
                if not local_filename:
                    local_filename = f"floor_image_{tenant_id}.{image_type}"

                # We'll store in "app/assets"
                base_dir = os.path.dirname(__file__)   # cisco_integrations/
                assets_dir = os.path.join(base_dir, "..", "app", "assets")
                os.makedirs(assets_dir, exist_ok=True)

                output_path = os.path.join(assets_dir, local_filename)
                with open(output_path, "wb") as f:
                    f.write(result)

                abs_path = os.path.abspath(output_path)
                logging.info(f"Saved floor image to: {abs_path}")

            return result  # Return the raw bytes
        except Exception as e:
            logging.error(f"Error retrieving floor image: {e}")
            return {"error": "Failed to retrieve floor image."}

    def get_devices(self, **kwargs) -> dict:
        endpoint = "api/location/v2/devices"
        query_str = _build_query(kwargs)
        try:
            response = self._get(endpoint + query_str)
            if not response:
                return {"message": "No devices found."}
            return response
        except Exception as e:
            logging.error(f"Error retrieving devices: {e}")
            return {"error": "Failed to retrieve devices."}

    def get_devices_count(self, **kwargs) -> dict:
        endpoint = "api/location/v2/devices/count"
        query_str = _build_query(kwargs)
        try:
            return self._get(endpoint + query_str)
        except Exception as e:
            logging.error(f"Error retrieving device count: {e}")
            return {"error": "Failed to retrieve device count."}

    def get_devices_floors(self) -> dict:
        endpoint = "api/location/v2/devices/floors"
        try:
            return self._get(endpoint)
        except Exception as e:
            logging.error(f"Error retrieving device floors: {e}")
            return {"error": "Failed to retrieve device floors."}

    def export_history_csv(self, **kwargs) -> Any:
        endpoint = "api/location/v2/history/record/export"
        query_str = _build_query(kwargs)
        try:
            return self._get(endpoint + query_str, return_json=False)
        except Exception as e:
            logging.error(f"Error exporting history CSV: {e}")
            return {"error": "Failed to export history CSV."}

    def export_history_gz(self, **kwargs) -> Any:
        endpoint = "api/location/v2/history/record/export"
        query_str = _build_query(kwargs)
        try:
            return self._get(endpoint + query_str, return_json=False)
        except Exception as e:
            logging.error(f"Error exporting history GZ: {e}")
            return {"error": "Failed to export history GZ."}
        
    def get_location_subtree(self, location_id: str) -> dict:
        """
        Return the subtree of the location hierarchy for the given location_id,
        including all of its children (recursively).
        """
        # Step 1: Get the entire hierarchy
        full_hierarchy = self.get_location_hierarchy()

        # Step 2: Define a recursive search function
        def find_subtree(node, search_id):
            if node.get("id") == search_id:
                return node
            children = node.get("children", [])
            for child in children:
                result = find_subtree(child, search_id)
                if result:
                    return result
            return None

        # Step 3: Search for the node in the full hierarchy
        subtree = find_subtree(full_hierarchy, location_id)

        if not subtree:
            return {"error": f"Location ID '{location_id}' not found in hierarchy."}
        return subtree
