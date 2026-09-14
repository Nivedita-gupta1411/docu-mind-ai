from pydantic import BaseModel

class DocumentModel(BaseModel):
    filename: str
    file_type: str
    upload_date: float
    status: str
    total_chunks: int
