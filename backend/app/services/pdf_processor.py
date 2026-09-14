import pathlib
from typing import Tuple

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise ImportError('PyPDF2 is required for PDF processing. Install it via pip install PyPDF2.')

def process_pdf(file_path: pathlib.Path) -> Tuple[str, dict]:
    """Extract raw text from a PDF file.

    Returns a tuple of (text: str, metadata: dict).
    """
    reader = PdfReader(str(file_path))
    text_pages = []
    for page in reader.pages:
        try:
            text_pages.append(page.extract_text() or '')
        except Exception:
            continue
    text = "\n".join(text_pages)
    metadata = {}
    return text, metadata
