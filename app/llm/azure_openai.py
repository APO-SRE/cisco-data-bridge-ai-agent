################################################################################
## cisco-data-bridge-domain-index/llm/azure_openai.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import openai
from typing import List, Any
from dotenv import load_dotenv
from .base_llm import BaseLLM

load_dotenv()

class AzureOpenAIClient(BaseLLM):
    """
    A client for Azure OpenAI, implementing the BaseLLM interface.
    Supports separate configurations for general and event-specific queries.
    """
    def __init__(self, is_event: bool = False):
        # Choose appropriate settings based on whether this is for an event query
        if is_event:
            self.endpoint = os.getenv("EVENT_AZURE_OPENAI_ENDPOINT", "")
            self.api_key = os.getenv("EVENT_AZURE_OPENAI_KEY", "")
            self.model = os.getenv("EVENT_AZURE_OPENAI_MODEL", "gpt-4-event")
            self.temperature = float(os.getenv("EVENT_AZURE_OPENAI_TEMPERATURE", "0.5"))
            self.top_p = float(os.getenv("EVENT_AZURE_OPENAI_TOP_P", "0.9"))
            self.max_tokens = int(os.getenv("EVENT_AZURE_OPENAI_MAX_TOKENS", "2048"))
            self.system_message = os.getenv("EVENT_AZURE_OPENAI_SYSTEM_MESSAGE", "")
        else:
            self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
            self.api_key = os.getenv("AZURE_OPENAI_KEY", "")
            self.model = os.getenv("AZURE_OPENAI_MODEL", "gpt-4")
            self.temperature = float(os.getenv("AZURE_OPENAI_TEMPERATURE", "0"))
            self.top_p = float(os.getenv("AZURE_OPENAI_TOP_P", "1.0"))
            self.max_tokens = int(os.getenv("AZURE_OPENAI_MAX_TOKENS", "4096"))
            self.system_message = os.getenv("AZURE_OPENAI_SYSTEM_MESSAGE", "")

        # Embedding configuration
        self.embedding_name = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
        self.embedding_endpoint = self.endpoint
        self.embedding_key = self.api_key

        # Configure Azure OpenAI for chat
        openai.api_type = "azure"
        openai.api_base = self.endpoint
        openai.api_key = self.api_key
        openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")

    def get_embedding(self, text: str) -> List[float]:
        """
        Generate embeddings for a given text string.
        """
        try:
            response = openai.Embedding.create(
                input=text,
                engine=self.embedding_name,
                api_base=self.embedding_endpoint,
                api_key=self.embedding_key,
            )
            return response["data"][0]["embedding"]
        except Exception as e:
            raise RuntimeError(f"Error generating embeddings: {e}")

    def call_llm(self, messages: List[dict], functions: Any = None) -> Any:
        """
        Calls the Azure OpenAI ChatCompletion endpoint 
        with optional function definitions.
        """
        try:
            response = openai.ChatCompletion.create(
                engine=self.model,
                messages=[{"role": "system", "content": self.system_message}] + messages,
                functions=functions,
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens
            )
            return response
        except Exception as e:
            raise RuntimeError(f"Error calling the LLM: {e}")



