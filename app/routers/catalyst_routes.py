################################################################################
## cisco-data-bridge-domain-index/routers/catalyst_routes.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################


import os
from fastapi import APIRouter, FastAPI # type: ignore
from cisco_integrations.unified_service import CiscoUnifiedService

router = APIRouter()

# Read environment variables for Catalyst Center
CATALYST_USERNAME = os.getenv("CISCO_CATALYST_USERNAME", "")
CATALYST_PASSWORD = os.getenv("CISCO_CATALYST_PASSWORD", "")
CATALYST_URL = os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443")
CATALYST_VERSION = os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6")

@router.get("/devices")
async def get_catalyst_devices():
    """
    GET /catalyst/devices

    Returns a list of all devices managed by the Catalyst Center (DNA Center).
    """
    service = CiscoUnifiedService(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION
    )
    data = service.get_all_catalyst_devices()
    return data

@router.get("/devices/{device_id}")
async def get_catalyst_device_by_id(device_id: str):
    """
    GET /catalyst/devices/{device_id}

    Returns details for a single device, by device_id in Catalyst Center (DNA Center).
    """
    service = CiscoUnifiedService(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION
    )
    data = service.get_catalyst_device_by_id(device_id)
    return data
