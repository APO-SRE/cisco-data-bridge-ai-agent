# /retrievers/elastic_retriever.py

import os
from typing import List
from elasticsearch import Elasticsearch
from app.llm.azure_openai import AzureOpenAIClient

class ElasticRetriever:
    """
    A retriever that uses Elasticsearch for vector-based (and/or hybrid) retrieval.
    """

    def __init__(self):
        self.elastic_host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.elastic_user = os.getenv("ELASTIC_USERNAME", "elastic")
        self.elastic_pass = os.getenv("ELASTIC_PASSWORD", "changeme")
        self.elastic_index = os.getenv("ELASTIC_INDEX", "cisco_docs")
        self.elastic_vector_field = os.getenv("ELASTIC_VECTOR_FIELD", "embedding")
        # For hybrid, you might store the text in a field named "content" and the vector in "embedding".
        self.es = Elasticsearch(
            self.elastic_host,
            basic_auth=(self.elastic_user, self.elastic_pass),
            verify_certs=False
        )

        # For embeddings
        self.llm_client = AzureOpenAIClient()

    def retrieve_documents(self, user_input: str, top_k: int = 5) -> List[str]:
        """
        1) Get embedding for user_input
        2) Query Elasticsearch (k-NN or hybrid)
        3) Return doc chunks
        """
        embedding = self.llm_client.get_embedding(user_input)

        # EXAMPLE: a simple vector query in ES 8.x
        # If you want strictly vector search:
        # (Note: the field "embedding" must be mapped as a dense_vector or similar.)
        query = {
            "size": top_k,
            "query": {
                "knn": {
                    self.elastic_vector_field: {
                        "vector": embedding,
                        "k": top_k
                    }
                }
            }
        }

        # If you want a hybrid approach (BM25 + vector), you can do something like:
        # query = {
        #   "size": top_k,
        #   "query": {
        #       "bool": {
        #           "should": [
        #               { "match": { "content": user_input } },
        #               {
        #                   "script_score": {
        #                       "query": {"match_all": {}},
        #                       "script": {
        #                           "source": f"cosineSimilarity(params.queryVector, '{self.elastic_vector_field}') + 1.0",
        #                           "params": {"queryVector": embedding}
        #                       }
        #                   }
        #               }
        #           ]
        #       }
        #   }
        # }

        response = self.es.search(index=self.elastic_index, body=query)

        docs = []
        hits = response["hits"]["hits"]
        for hit in hits:
            # If your document content is stored in e.g. "content" field:
            doc_text = hit["_source"].get("content", "")
            docs.append(doc_text.strip())

        return docs
