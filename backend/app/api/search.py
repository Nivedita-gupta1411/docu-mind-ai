from fastapi import APIRouter, HTTPException
from ..schemas.schemas import SearchRequest, SearchResponse, SearchResultItem
from ..services.retriever import retrieve
from ..config import settings

router = APIRouter()

@router.post('/search', response_model=SearchResponse)
async def search_endpoint(request: SearchRequest):
    top_k = request.top_k if request.top_k is not None else settings.TOP_K
    results = retrieve(request.query, top_k=top_k, doc_ids=request.doc_ids)
    items = [SearchResultItem(**res) for res in results]
    return SearchResponse(results=items)
