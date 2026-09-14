import os
from pathlib import Path

from pymongo import MongoClient

from .docx_processor import process_docx
from .text_processor import process_text
from .chunking import chunk_text
from .embeddings import embed_chunks
from .vector_store import get_vector_store
from ..config import settings

client = MongoClient(settings.MONGODB_URI, serverSelectionTimeoutMS=3000)
db = client[settings.MONGODB_DB]

def process_document(file_path: Path):
    """Extract, chunk, embed and persist one uploaded document.

    A MongoDB record is created first so the UI can observe processing status.
    The generated MongoDB id is also attached to every vector chunk, making RAG
    citations link back to the real document instead of the filename.
    """
    ext = file_path.suffix.lower()
    doc_doc = {
        'filename': file_path.name,
        'file_type': ext,
        'upload_date': os.path.getctime(file_path),
        'status': 'processing',
        'total_chunks': 0,
    }
    inserted = db.documents.insert_one(doc_doc)
    document_id = str(inserted.inserted_id)

    try:
        if ext == '.pdf':
            from .pdf_processor import process_pdf
            raw_text, metadata = process_pdf(file_path)
        elif ext == '.docx':
            raw_text, metadata = process_docx(file_path)
        else:
            raw_text, metadata = process_text(file_path)

        cleaned = raw_text.replace('\n', ' ').strip()
        if not cleaned:
            raise ValueError('No readable text was found in the document')

        chunks = chunk_text(cleaned, file_path.name, {
            **metadata,
            'document_id': document_id,
        })
        embeddings = embed_chunks([c['text'] for c in chunks])

        vector_store = get_vector_store()
        vector_store.add_embeddings(embeddings, chunks)
        vector_store.save()

        db.documents.update_one(
            {'_id': inserted.inserted_id},
            {'$set': {'status': 'processed', 'total_chunks': len(chunks)}}
        )
    except Exception:
        db.documents.update_one(
            {'_id': inserted.inserted_id},
            {'$set': {'status': 'failed'}}
        )
        raise
