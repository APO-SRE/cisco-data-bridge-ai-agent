################################################################################
## cisco-data-bridge-domain-index/llm/llm_factory.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import logging
from app.llm.azure_openai import AzureOpenAIClient
from app.llm.llam3 import Llama3Client  # <-- updated import path

def get_llm_client():
    provider = os.getenv("LLM_PROVIDER", "azure").lower()
    logging.info(f"Initializing LLM Client, provider={provider}")

    if provider == "llama3":
        base_url = os.getenv("LLAMA3_BASE_URL")
        model_name = os.getenv("LLAMA3_MODEL_NAME", "llama3_default")
        return Llama3Client(base_url=base_url, model_name=model_name)

    elif provider == "azure":
        return AzureOpenAIClient(
            deployment=os.getenv("AZURE_OPENAI_MODEL"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
    
    else:
        raise ValueError(f"Unsupported LLM provider specified: {provider}")

