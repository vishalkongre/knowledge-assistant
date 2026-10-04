class TextChunker:
    def __init__(self, chunk_size, overlap):
        self.__chunk_size = chunk_size
        self.__overlap = overlap

    def chunk(self, text):
        chunks =[]
        start = 0 
        while start < len(text):
            end = start + self.__chunk_size
            chunk = text[start:end]
            if len(chunk) == self.__chunk_size:
                chunks.append(chunk)
            start = start + self.__chunk_size - self.__overlap
        return chunks

