from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class UploadResponse(BaseModel):
    filename: str = Field(..., description="Name of the uploaded file")
    status: str = Field(..., description="Upload processing status")

class DocumentInfo(BaseModel):
    id: str = Field(..., alias="_id", description="MongoDB document ID")
    filename: str
    file_type: str
    upload_date: float
    status: str
    total_chunks: int

class DocumentListResponse(BaseModel):
    documents: List[DocumentInfo]

class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = Field(None, ge=1, le=20, description="Number of results to return")
    doc_ids: Optional[List[str]] = Field(None, description="Filter to specific document IDs")

class SearchResultItem(BaseModel):
    text: str
    metadata: Dict
    score: float

class SearchResponse(BaseModel):
    results: List[SearchResultItem]

class ChatRequest(BaseModel):
    question: str
    top_k: Optional[int] = Field(None, ge=1, le=20)
    doc_ids: Optional[List[str]] = None

class SourceInfo(BaseModel):
    document_id: str
    filename: str
    chunk_id: str
    score: float

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceInfo]
