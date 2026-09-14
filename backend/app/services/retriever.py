import logging
from typing import List, Dict, Optional

from .embeddings import embed_chunks
from .vector_store import get_vector_store
from ..config import settings

logger = logging.getLogger(__name__)

def retrieve(query: str, top_k: int = None, doc_ids: Optional[List[str]] = None) -> List[Dict]:
    """Retrieve the most relevant stored chunks, optionally restricted to documents."""
    if top_k is None:
        top_k = settings.TOP_K
    vector_store = get_vector_store()
    if vector_store.index.ntotal == 0:
        return []

    query_emb = embed_chunks([query])[0]
    search_k = vector_store.index.ntotal if doc_ids else min(top_k, vector_store.index.ntotal)
    distances, indices = vector_store.search(query_emb, search_k)
    allowed = set(doc_ids or [])
    results = []
    for idx, dist in zip(indices[0], distances[0]):
        if idx < 0:
            continue
        chunk = vector_store.get_chunk(int(idx))
        if allowed and chunk.get('metadata', {}).get('document_id') not in allowed:
            continue
        results.append({
            'text': chunk['text'],
            'metadata': chunk['metadata'],
            'score': float(dist),
        })
        if len(results) >= top_k:
            break
    logger.info('Retrieved %d chunks for query', len(results))
    return results
