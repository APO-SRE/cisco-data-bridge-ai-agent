################################################################################
## _app/main.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

# Routers
from app.routers.chat_routes import router as chat_router
from app.routers.catalyst_routes import router as catalyst_router
from app.routers.meraki_routes import router as meraki_router
from app.routers.spaces_routes import router as spaces_router

# Load environment variables
load_dotenv()

# Print environment configuration for debugging
print(f"AZURE_SEARCH_ENABLE_IN_DOMAIN: {os.getenv('AZURE_SEARCH_ENABLE_IN_DOMAIN', 'not set')}")
print(f"AZURE_OPENAI_MODEL: {os.getenv('AZURE_OPENAI_MODEL', 'not set')}")
print(f"EVENT_AZURE_OPENAI_MODEL: {os.getenv('EVENT_AZURE_OPENAI_MODEL', 'not set')}")

app = FastAPI()

# -------------------------------------------------------------------
# Compute the project root and get absolute paths for the "static" folder
# -------------------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))  # /path/to/app
PROJECT_ROOT = os.path.dirname(APP_DIR)               # /path/to

# Paths for static and assets directories
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
ASSETS_DIR = os.path.join(APP_DIR, "assets")

# -------------------------------------------------------------------
# Mount static + assets
# -------------------------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

@app.get("/")
async def root():
    """
    Return the index.html file as an HTML response.
    """
    try:
        index_path = os.path.join(STATIC_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        return HTMLResponse(content=content, status_code=200)
    except FileNotFoundError:
        return {"message": "index.html not found in 'static' directory."}

# -------------------------------------------------------------------
# Health Check Endpoint
# -------------------------------------------------------------------
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the application is running.
    """
    return {"status": "ok", "message": "Service is up and running."}

# -------------------------------------------------------------------
# Include Routers
# -------------------------------------------------------------------
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(catalyst_router, prefix="/catalyst", tags=["Catalyst"])
app.include_router(meraki_router, prefix="/meraki", tags=["Meraki"])
app.include_router(spaces_router, prefix="/spaces", tags=["Spaces"])
