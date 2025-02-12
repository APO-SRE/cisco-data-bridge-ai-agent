################################################################################
## cisco-data-bridge-domain-index/llm/base_llm.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

from abc import ABC, abstractmethod
from typing import Any, List

class BaseLLM(ABC):
    """
    Abstract base class defining a common interface 
    for different LLM backends (Azure OpenAI, Ollama, etc.).
    """

    @abstractmethod
    def call_llm(self, messages: List[dict], functions: Any = None) -> Any:
        """
        Call the LLM with a list of messages (chat format).
        Optional 'functions' param for OpenAI function calling.
        Returns the raw response from the LLM.
        """
        pass

    @abstractmethod
    def get_embedding(self, text: str) -> List[float]:
        """
        Return the embedding vector for a given text string.
        """
        pass