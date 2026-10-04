from .embedding_model import EmbeddingModel
from sentence_transformers import SentenceTransformer


class LocalEmbeddingModel(EmbeddingModel):
    def __init__(self):
        super().__init__()
        self.__local_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


    def to_vector(self, text):
        return self.__local_embedding_model.encode(text)