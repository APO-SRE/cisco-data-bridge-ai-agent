################################################################################
## cisco-data-bridge-domain-index/routers/__init__.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################


from .catalyst_routes import router as catalyst_router
from .chat_routes import router as chat_router
from .meraki_routes import router as meraki_router
from .spaces_routes import router as spaces_router
from .webex_routes import router as webex_router

__all__ = [
    "catalyst_router",
    "chat_router",
    "meraki_router",
    "spaces_router",
    "webex_router",
]
