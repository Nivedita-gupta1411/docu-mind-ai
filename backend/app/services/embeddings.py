from sentence_transformers import SentenceTransformer
from ..config import settings

# Load model once at import time
_model = SentenceTransformer(settings.EMBEDDING_MODEL)


def embed_chunks(texts):
    """Return a list of embedding vectors for the given list of texts."""
    return _model.encode(
        texts,
        show_progress_bar=False
    ).tolist()