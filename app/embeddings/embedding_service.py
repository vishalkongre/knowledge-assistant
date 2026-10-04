class EmbeddingService:
    def __init__(self, model):
        self.__model = model


    def embed(self, text):
        vector = self.__model.to_vector(text)
        return vector

    def embed_batch(self, texts):
        vectors = []
        for text in texts:
            vectors.append(self.embed(text))
        return vectors