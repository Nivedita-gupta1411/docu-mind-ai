from fastapi import APIRouter, HTTPException
from ..schemas.schemas import ChatRequest, ChatResponse, SourceInfo
from ..services.rag import answer_question

router = APIRouter()

@router.post('/chat', response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        result = await answer_question(request.question, top_k=request.top_k, doc_ids=request.doc_ids)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        # Keep internal details in server logs; return a safe client-facing message.
        import logging
        logging.getLogger(__name__).exception('Chat request failed')
        raise HTTPException(status_code=502, detail='The AI service could not answer the request.') from exc
    return ChatResponse(answer=result['answer'], sources=result['sources'])
