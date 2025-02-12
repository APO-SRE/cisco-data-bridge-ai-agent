################################################################################
## cisco-data-bridge-domain-index/routers/webex_routes.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################


from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging
import os

# Import the unified service that encapsulates Webex functionality.
from cisco_integrations.unified_service import CiscoUnifiedService

# Create a router instance for Webex endpoints.
router = APIRouter()

@router.get("/webex/meetings")
def get_webex_meetings():
    """
    Retrieve a list of Webex meetings.
    This stub endpoint uses the unified service to obtain a response.
    """
    try:
        service = CiscoUnifiedService(
            catalyst_username=os.getenv("CISCO_CATALYST_USERNAME", ""),
            catalyst_password=os.getenv("CISCO_CATALYST_PASSWORD", ""),
            catalyst_url=os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443"),
            catalyst_version=os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6"),
            meraki_api_key=os.getenv("CISCO_MERAKI_API_KEY", ""),
            spaces_token=os.getenv("CISCO_SPACES_API_KEY", ""),
            webex_token=os.getenv("CISCO_WEBEX_TOKEN", "")
        )
        # Call the stub method for Webex meetings.
        result = service.get_webex_meetings()
        return JSONResponse(content={"webex_meetings": result})
    except Exception as e:
        logging.error(f"Error retrieving Webex meetings: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webex/meetings/{meeting_id}")
def get_webex_meeting_by_id(meeting_id: str):
    """
    Retrieve details of a specific Webex meeting by its meeting ID.
    """
    try:
        service = CiscoUnifiedService(
            catalyst_username=os.getenv("CISCO_CATALYST_USERNAME", ""),
            catalyst_password=os.getenv("CISCO_CATALYST_PASSWORD", ""),
            catalyst_url=os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443"),
            catalyst_version=os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6"),
            meraki_api_key=os.getenv("CISCO_MERAKI_API_KEY", ""),
            spaces_token=os.getenv("CISCO_SPACES_API_KEY", ""),
            webex_token=os.getenv("CISCO_WEBEX_TOKEN", "")
        )
        result = service.get_webex_meeting_by_id(meeting_id)
        return JSONResponse(content={"webex_meeting": result})
    except Exception as e:
        logging.error(f"Error retrieving Webex meeting with ID {meeting_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))