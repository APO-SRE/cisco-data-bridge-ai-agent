# /retrievers/chroma_retriever.py

import os
from typing import List
from chromadb import Client
from chromadb.config import Settings

# For embeddings, you can use your LLM or a local embedding approach.
# You might import from your existing AzureOpenAIClient or a separate embedding class:
from app.llm.azure_openai import AzureOpenAIClient

class ChromaRetriever:
    """
    A retriever that uses Chroma as the vector store.
    """

    def __init__(self):
        # Load from .env if needed
        self.chroma_db_path = os.getenv("CHROMA_DB_PATH", "chroma_db/")
        self.collection_name = os.getenv("CHROMA_COLLECTION_NAME", "cisco_docs")

        # Initialize Chroma client (persistent or in-memory)
        self.chroma_client = Client(
            Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=self.chroma_db_path
            )
        )

        # Create or get the collection
        self.collection = self.chroma_client.get_or_create_collection(self.collection_name)

        # We'll use Azure OpenAI for embeddings, or you can use local embeddings
        self.llm_client = AzureOpenAIClient()

    def retrieve_documents(self, user_input: str, top_k: int = 5) -> List[str]:
        """
        1) Get embedding for user_input
        2) Query the local Chroma DB for the top_k nearest vectors
        3) Return doc chunks
        """
        user_embedding = self.llm_client.get_embedding(user_input)

        results = self.collection.query(
            query_embeddings=[user_embedding],
            n_results=top_k
        )

        # `results` structure: { "ids": [...], "documents": [...], "metadatas": [...], "embeddings": [...] }
        # We'll return documents
        docs = []
        if "documents" in results:
            for doc_list in results["documents"]:
                for chunk in doc_list:
                    docs.append(chunk.strip())

        return docs
