################################################################################
## cisco-data-bridge-domain-index/llm/llam3.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import requests
import logging

class Llama3Client:
    def __init__(self, base_url: str, model_name: str):
        self.base_url = base_url
        self.model_name = model_name
        logging.info(f"Llama3Client initialized with base_url={base_url}, model={model_name}")

    def call_llm(self, messages, functions=None):
        payload = {
            "model": self.model_name,
            "messages": messages,
            "functions": functions or []
        }
        response = requests.post(f"{self.base_url}/generate", json=payload)
        if response.ok:
            logging.debug(f"Llama3 Response: {response.json()}")
            return response.json()
        else:
            logging.error(f"Llama3 request failed: {response.text}")
            response.raise_for_status()
