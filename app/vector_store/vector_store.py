from app.utility.similarity import cosine_similarity

class VectorStore:
    def __init__(self):
        self.__records = []

    def add(self, chunk, vector, metadata):
        vector_record = {"chunk": chunk, "vector": vector, "metadata": metadata}
        self.__records.append(vector_record)

    def get_all_records(self):
        return self.__records

    def search(self, query_vector, top_k):
        results = []
        for record in self.__records:
            results.append((record["chunk"], cosine_similarity(query_vector, record["vector"]), record["metadata"]))
        sorted_results = sorted(results, key=lambda x:x[1], reverse=True)
        return sorted_results[:top_k]
