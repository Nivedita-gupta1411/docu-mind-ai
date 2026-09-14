import logging
from typing import List, Dict, Optional

from .embeddings import embed_chunks
from .vector_store import get_vector_store
from ..config import settings

logger = logging.getLogger(__name__)


def retrieve(
    query: str,
    top_k: int = None,
    doc_ids: Optional[List[str]] = None
) -> List[Dict]:
    """Retrieve relevant document chunks for a user query."""

    if top_k is None:
        top_k = settings.TOP_K

    vector_store = get_vector_store()

    if vector_store.index.ntotal == 0:
        return []

    # Query embedding
    query_emb = embed_chunks(
        [query],
        task_type="RETRIEVAL_QUERY"
    )[0]

    if doc_ids:
        search_k = vector_store.index.ntotal
    else:
        search_k = min(
            top_k,
            vector_store.index.ntotal
        )

    distances, indices = vector_store.search(
        query_emb,
        search_k
    )

    allowed = set(doc_ids or [])

    results = []

    for idx, dist in zip(indices[0], distances[0]):

        if idx < 0:
            continue

        chunk = vector_store.get_chunk(int(idx))

        document_id = chunk.get(
            "metadata",
            {}
        ).get("document_id")

        if allowed and document_id not in allowed:
            continue

        results.append({
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "score": float(dist),
        })

        if len(results) >= top_k:
            break

    logger.info(
        "Retrieved %d chunks for query",
        len(results)
    )

    return results