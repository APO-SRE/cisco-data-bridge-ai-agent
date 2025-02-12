################################################################################
## cisco-data-bridge-domain-index/llm/__init__.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

from .azure_openai import AzureOpenAIClient
from .base_llm import BaseLLM
from .function_definitions import FUNCTION_DEFINITIONS
from .function_dispatcher import dispatch_function_call
from .prompt_templates import (
    BASE_SYSTEM_PROMPT_DOCS_ONLY,
    BASE_SYSTEM_PROMPT_GENERAL,
    BASE_SYSTEM_PROMPT_EVENT,
    BASE_SYSTEM_PROMPT_LOB,
    USER_PROMPT_TEMPLATE
)

__all__ = [
    "AzureOpenAIClient",
    "BaseLLM",
    "FUNCTION_DEFINITIONS",
    "dispatch_function_call",
    "BASE_SYSTEM_PROMPT_DOCS_ONLY",
    "BASE_SYSTEM_PROMPT_GENERAL",
    "BASE_SYSTEM_PROMPT_EVENT",
    "BASE_SYSTEM_PROMPT_LOB",
    "USER_PROMPT_TEMPLATE",
]
