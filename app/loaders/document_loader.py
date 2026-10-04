from pathlib import Path
from app.models.document import Document


class DocumentLoader:
    def __init__(self):
        pass

    def load(self, file_path):
        file_path = Path(file_path)
        filename = file_path.name
        content = file_path.read_text("utf-8")
        return Document(filename, content)


        