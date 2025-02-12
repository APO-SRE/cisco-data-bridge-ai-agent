################################################################################
## cisco-data-bridge-domain-index/routers/spaces_routes.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
from fastapi import APIRouter
from cisco_integrations.unified_service import CiscoUnifiedService

router = APIRouter()

# Read the API key from the environment variable (adjust if needed).
# If your Spaces token is actually in "CISCO_SPACES_TOKEN", update accordingly.
SPACES_TOKEN = os.getenv("CISCO_SPACES_API_KEY", "")

@router.get("/devices")
async def get_spaces_devices():
    """
    GET /spaces/devices

    Returns a list of active devices from Cisco Spaces.
    """
    service = CiscoUnifiedService(spaces_token=SPACES_TOKEN)
    devices = service.get_spaces_active_devices()
    return devices

@router.get("/floor/{floor_id}")
async def get_spaces_floor_details(floor_id: str):
    """
    GET /spaces/floor/{floor_id}

    Returns floor details for a specific floor from Cisco Spaces.
    """
    service = CiscoUnifiedService(spaces_token=SPACES_TOKEN)
    floor_details = service.get_spaces_floor_details(floor_id)
    return floor_details