import pathlib
from typing import Tuple

def process_text(file_path: pathlib.Path) -> Tuple[str, dict]:
    """Read plain text from a .txt or other simple text file.

    Returns a tuple of (text: str, metadata: dict). Metadata is currently empty.
    """
    try:
        text = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        text = file_path.read_text(encoding='latin-1')
    metadata = {}
    return text, metadata
