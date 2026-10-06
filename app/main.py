from app.models.document import Document
from app.chunking.text_chunker import TextChunker
from app.loaders.document_loader import DocumentLoader
from app.embeddings.local_embedding_model import LocalEmbeddingModel
from app.embeddings.embedding_service import EmbeddingService
from app.vector_store.vector_store import VectorStore


# loader = DocumentLoader()
# document = loader.load('data/python_intro.txt')

# chunker = TextChunker(20)

# text = document.get_text()

# chunks = chunker.chunk(text)

# for chunk in chunks:
#     print(chunk)


# texts = ["Python is a programming language.",
# "Python is widely used in artificial intelligence.",
# "Pizza is a popular Italian food."]

# local_model = LocalEmbeddingModel()
# embedding_service = EmbeddingService(local_model)
# vectors = embedding_service.embed_batch(texts)
# vector_store = VectorStore()
# for index, text in enumerate(texts):
#     metadata = {"file_name": "python_intro.txt", "chunk_index":index}
#     vector_store.add(text, vectors[index], metadata=metadata )

# query = "What is Python used for?"

# query_vector = embedding_service.embed(query)

# print(vector_store.search(query_vector, top_k=2))

# print(type(vector))
# print(len(vector))
# # print(vector)


chunker = TextChunker(200, 40)
loader = DocumentLoader()
vector_store = VectorStore()
local_model = LocalEmbeddingModel()
embedding_service = EmbeddingService(local_model)

def ingest(file_path):
    document = loader.load(file_path)
    text = document.get_text()
    chunks = chunker.chunk(text)
    vectors = embedding_service.embed_batch(chunks)

    for index, text in enumerate(chunks):
         metadata = {"file_name": document.filename, "chunk_index":index}
         vector_store.add(text, vectors[index], metadata=metadata)



ingest("data/ai_engineering_notes.txt")
print(len(vector_store.get_all_records()))



def print_query_result(query):
     query_vector = embedding_service.embed(query)
     query_results = vector_store.search(query_vector, top_k=2) 
     for chunks, score, metadata in query_results:
        print(f'Query: {query} \n Score: {score} \n Chunk: {chunks} \n Metadata:{metadata}')


print_query_result("What is approximate nearest neighbor search?")
print_query_result("How does RAG reduce hallucinations?")
print_query_result("Why is metadata filtering useful?")
print_query_result("Why would we use asynchronous document processing?")
print_query_result("What is method overriding in Python?")


