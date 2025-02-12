################################################################################
## cisco-data-bridge-domain-index/cisco_integrations/base_client.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import requests
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from typing import Any, Optional

class BaseCiscoClient:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        :param base_url: The base URL for the Cisco API endpoint (e.g., "https://api.ciscospaces.com")
        :param token: The API or bearer token for authentication. If None, must be handled by subclasses.
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.session = requests.Session()

    def _headers(self) -> dict:
        """
        Return common headers including authentication.
        Override in subclasses if needed.
        """
        if not self.token:
            raise ValueError("API token is not set. Please provide a valid token or set an environment variable.")
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    @retry(
        wait=wait_exponential(min=1, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def _get(self, endpoint: str, params: dict = None, return_json: bool = True) -> Any:
        """
        Internal GET request with retries.
        :param endpoint: Endpoint path (e.g., "occupancy?locationId=123")
        :param params: Optional query parameters
        :param return_json: Whether to return JSON (True) or raw bytes (False)
        :return: Parsed JSON response or raw response content.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        return response.json() if return_json else response.content

    @retry(
        wait=wait_exponential(min=1, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def _post(self, endpoint: str, data: dict = None) -> Any:
        """
        Internal POST request with retries.
        :param endpoint: Endpoint path
        :param data: JSON payload
        :return: Parsed JSON response
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, headers=self._headers(), json=data)
        response.raise_for_status()
        return response.json()