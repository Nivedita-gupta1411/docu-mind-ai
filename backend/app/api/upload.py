from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
import shutil
from pathlib import Path
from ..config import settings
from ..services.document_processor import process_document

router = APIRouter()

@router.post('/upload')
async def upload_file(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    if not file.filename:
        raise HTTPException(status_code=400, detail='A filename is required')
    ext = Path(file.filename).suffix.lower()
    if ext not in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail='Unsupported file type')
    upload_path = settings.UPLOAD_DIR / file.filename
    with open(upload_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    size_mb = upload_path.stat().st_size / (1024 * 1024)
    if size_mb > settings.MAX_UPLOAD_SIZE_MB:
        upload_path.unlink()
        raise HTTPException(status_code=400, detail='File too large')
    if background_tasks:
        background_tasks.add_task(process_document, upload_path)
    else:
        process_document(upload_path)
    return {'filename': file.filename, 'size_mb': round(size_mb, 2), 'status': 'uploaded'}
