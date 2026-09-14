import logging
from typing import List

import numpy as np
from google import genai
from google.genai import types

from ..config import settings

logger = logging.getLogger(__name__)

_client = None


def get_embedding_client():
    global _client

    if _client is None:
        if not settings.GEMINI_API_KEY:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        _client = genai.Client(api_key=settings.GEMINI_API_KEY)

    return _client


def embed_chunks(
    texts: List[str],
    task_type: str = "RETRIEVAL_DOCUMENT"
) -> List[np.ndarray]:
    """
    Generate Gemini embeddings for document chunks or queries.

    RETRIEVAL_DOCUMENT -> use when indexing document chunks.
    RETRIEVAL_QUERY    -> use when embedding user queries.
    """

    if not texts:
        return []

    client = get_embedding_client()

    try:
        result = client.models.embed_content(
            model=settings.EMBEDDING_MODEL,
            contents=texts,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=settings.EMBEDDING_DIMENSION,
            ),
        )

        embeddings = []

        for embedding in result.embeddings:
            values = np.array(
                embedding.values,
                dtype=np.float32
            )

            # gemini-embedding-001 needs normalization
            # when using dimensions smaller than 3072.
            norm = np.linalg.norm(values)

            if norm > 0:
                values = values / norm

            embeddings.append(values)

        return embeddings

    except Exception as e:
        logger.exception("Gemini embedding generation failed")
        raise RuntimeError(
            f"Failed to generate embeddings: {e}"
        ) from e