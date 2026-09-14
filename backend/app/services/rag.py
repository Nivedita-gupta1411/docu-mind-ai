import logging
from typing import List, Dict
from .retriever import retrieve
from .llm import get_llm_provider
from ..config import settings

logger = logging.getLogger(__name__)

async def answer_question(question: str, top_k: int = None, doc_ids: List[str] = None) -> Dict:
    """Answer a user question using Retrieval-Augmented Generation (RAG).
    Steps:
    1. Retrieve relevant chunks.
    2. Build a prompt that includes the context and the question.
    3. Generate answer via LLM.
    Returns a dict with 'answer' and 'sources' (list of metadata).
    """
    if top_k is None:
        top_k = settings.TOP_K
    # Retrieve relevant chunks
    chunks = retrieve(question, top_k=top_k, doc_ids=doc_ids)
    if not chunks:
        answer = "I couldn't find sufficient information in the uploaded documents."
        sources = []
    else:
        # Build context string
        context_parts = []
        sources = []
        for i, chunk in enumerate(chunks, start=1):
            ctx = f"[{i}] {chunk['text']} (source: {chunk['metadata'].get('filename', 'unknown')}, chunk_id: {chunk['metadata'].get('chunk_id')})"
            context_parts.append(ctx)
            sources.append({
                "document_id": chunk['metadata'].get('document_id'),
                "filename": chunk['metadata'].get('filename'),
                "chunk_id": chunk['metadata'].get('chunk_id'),
                "score": chunk.get('score')
            })
        context_str = "\n".join(context_parts)
        prompt = f"You are a helpful assistant. Answer the user's question using only the provided context. Cite sources using the information in parentheses.\n\nContext:\n{context_str}\n\nQuestion: {question}\n"
        llm = get_llm_provider()
        # generate may be async or sync; handle both
        try:
            answer = await llm.generate(prompt)
        except TypeError:
            # sync implementation fallback
            answer = llm.generate(prompt)
    logger.info("RAG answered question: %s", question)
    return {"answer": answer, "sources": sources}
