################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/meraki_sdk_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import meraki
import logging

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

    def get_networks(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationNetworks(organization_id)
    
    def get_network_by_id(self, organization_id: str, network_id: str):
        return self.dashboard.networks.getNetwork(network_id)
