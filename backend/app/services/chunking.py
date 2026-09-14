import re
from typing import List, Dict
from ..config import settings

def chunk_text(text: str, document_name: str, extra_metadata: Dict = None) -> List[Dict]:
    """Split the given text into overlapping word chunks.
    Args:
        text: The full text to split.
        document_name: Identifier for the source document (e.g., filename).
        extra_metadata: Additional metadata to attach to each chunk.
    Returns:
        A list of dicts, each with keys 'text' and 'metadata'.
    """
    if extra_metadata is None:
        extra_metadata = {}
    # Tokenize by whitespace (word level)
    words = re.findall(r"\S+", text)
    size = settings.CHUNK_SIZE_WORDS
    overlap = settings.CHUNK_OVERLAP_WORDS
    chunks = []
    i = 0
    chunk_idx = 0
    while i < len(words):
        chunk_words = words[i : i + size]
        chunk_str = " ".join(chunk_words)
        metadata = {
            "document_id": document_name,
            "filename": document_name,
            "chunk_id": f"{document_name}_chunk_{chunk_idx}",
            **extra_metadata,
        }
        chunks.append({"text": chunk_str, "metadata": metadata})
        i += size - overlap
        chunk_idx += 1
    return chunks
