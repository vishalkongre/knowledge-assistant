from app.models.document import Document
from app.chunking.text_chunker import TextChunker
from app.loaders.document_loader import DocumentLoader
from app.embeddings.local_embedding_model import LocalEmbeddingModel
from app.embeddings.embedding_service import EmbeddingService


# loader = DocumentLoader()
# document = loader.load('data/python_intro.txt')

# chunker = TextChunker(20)

# text = document.get_text()

# chunks = chunker.chunk(text)

# for chunk in chunks:
#     print(chunk)



local_model = LocalEmbeddingModel()
embedding_service = EmbeddingService(local_model)
vector = embedding_service.embed("Python is used in AI.")

print(type(vector))
print(len(vector))
# print(vector)