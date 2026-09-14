from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient

from ..config import settings
from ..schemas.schemas import DocumentInfo, DocumentListResponse

router = APIRouter()
client = MongoClient(settings.MONGODB_URI, serverSelectionTimeoutMS=3000)
db = client[settings.MONGODB_DB]

def _object_id(doc_id: str) -> ObjectId:
    if not ObjectId.is_valid(doc_id):
        raise HTTPException(status_code=400, detail="Invalid document id")
    return ObjectId(doc_id)

@router.get('/documents', response_model=DocumentListResponse)
async def list_documents():
    docs = list(db.documents.find().sort('upload_date', -1))
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return DocumentListResponse(documents=[DocumentInfo(**doc) for doc in docs])

@router.get('/documents/{doc_id}', response_model=DocumentInfo)
async def get_document(doc_id: str):
    doc = db.documents.find_one({'_id': _object_id(doc_id)})
    if not doc:
        raise HTTPException(status_code=404, detail='Document not found')
    doc['_id'] = str(doc['_id'])
    return DocumentInfo(**doc)

@router.delete('/documents/{doc_id}')
async def delete_document(doc_id: str):
    result = db.documents.delete_one({'_id': _object_id(doc_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Document not found')
    return {'status': 'deleted'}
