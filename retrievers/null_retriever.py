# retrievers/null_retriever.py

class NullRetriever:
    """
    A retriever that always returns an empty list (i.e., no documents).
    """

    def __init__(self):
        pass

    def retrieve_documents(self, query: str, top_k: int) -> list:
        """
        Always returns an empty list.
        :param query: The search query.
        :param top_k: The number of documents to 'retrieve'—in this case, none.
        :return: Empty list.
        """
        return []
