class Document:
    def __init__(self,filename, content):
        self.filename = filename
        self.content = content
        pass

    def get_text(self):
        return self.content