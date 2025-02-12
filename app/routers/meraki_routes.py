################################################################################
## cisco-data-bridge-domain-index/routers/meraki_routes.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################


from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Optional
from cisco_integrations.unified_service import CiscoUnifiedService
import os

router = APIRouter()

# Pull Meraki API key from env (or pass it from top-level config)
MERAKI_API_KEY = os.getenv("CISCO_MERAKI_API_KEY", "")

# Suppose you also need Catalyst info or other tokens:
CATALYST_USERNAME = os.getenv("CISCO_CATALYST_USERNAME", "")
CATALYST_PASSWORD = os.getenv("CISCO_CATALYST_PASSWORD", "")
CATALYST_URL = os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443")
CATALYST_VERSION = os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6")

SPACES_TOKEN = os.getenv("CISCO_SPACES_TOKEN", "")
WEBEX_TOKEN = os.getenv("CISCO_WEBEX_TOKEN", "")

@router.get("/meraki/networks")
def list_meraki_networks():
    """
    Return all Meraki networks in the org (requires your unified_service implementing get_meraki_networks).
    """
    if not MERAKI_API_KEY:
        raise HTTPException(status_code=400, detail="MERAKI_API_KEY is missing.")

    service = CiscoUnifiedService(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION,
        meraki_api_key=MERAKI_API_KEY,
        spaces_token=SPACES_TOKEN,
        webex_token=WEBEX_TOKEN
    )
    try:
        networks_data = service.get_meraki_networks()
        return JSONResponse(content={"networks": networks_data})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/meraki/networks/{network_id}")
def get_meraki_network(network_id: str):
    """
    Return details of a single Meraki network by ID.
    """
    if not MERAKI_API_KEY:
        raise HTTPException(status_code=400, detail="MERAKI_API_KEY is missing.")

    service = CiscoUnifiedService(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION,
        meraki_api_key=MERAKI_API_KEY,
        spaces_token=SPACES_TOKEN,
        webex_token=WEBEX_TOKEN
    )
    try:
        network_data = service.get_meraki_network_by_id(network_id)
        return JSONResponse(content={"network": network_data})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
