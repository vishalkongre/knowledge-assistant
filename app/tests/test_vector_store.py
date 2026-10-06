from app.vector_store.vector_store import VectorStore
import numpy as np

# Test vector store
vector_store = VectorStore()
vector_store.add("Python is a high-level programming language.", [0.1, 0.2, 0.3], {
        "filename": "python_intro.txt",
        "chunk_index": 0
    })
vector_store.add("Python is widely used for artificial intelligence and machine learning.", [0.4, 0.5, 0.6], {
        "filename": "python_intro.txt",
        "chunk_index": 1
    })

# print(vector_store.get_all_records())

query_vector = np.array([0.15, 0.25, 0.35])
print(vector_store.search(query_vector, top_k=2))
