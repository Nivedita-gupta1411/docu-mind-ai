import pathlib
import docx

def process_docx(file_path: pathlib.Path):
    """Extract raw text from a DOCX file.
    Returns a tuple of (text: str, metadata: dict).
    """
    doc = docx.Document(str(file_path))
    paragraphs = [p.text for p in doc.paragraphs if p.text]
    text = "\n".join(paragraphs)
    metadata = {}
    return text, metadata
