from app.embeddings.local_embedding_model import LocalEmbeddingModel
from app.embeddings.embedding_service import EmbeddingService
from app.vector_store.vector_store import VectorStore


texts = ["Python is a programming language.",
"Python is widely used in artificial intelligence.",
"Pizza is a popular Italian food."]

local_model = LocalEmbeddingModel()
embedding_service = EmbeddingService(local_model)
vectors = embedding_service.embed_batch(texts)
vector_store = VectorStore()
for index, text in enumerate(texts):
    metadata = {"file_name": "python_intro.txt", "chunk_index":index}
    vector_store.add(text, vectors[index], metadata=metadata )

query = "What is Python used for?"

query_vector = embedding_service.embed(query)

print(vector_store.search(query_vector, top_k=2))