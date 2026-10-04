class EmbeddingModel:
    def __init__(self):
        pass

    

    def to_vector(self, text):
        return self.__local_embedding_model.encode(text)