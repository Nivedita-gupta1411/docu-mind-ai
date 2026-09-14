from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .api import upload, documents, search, chat

app = FastAPI(title='Document Intelligent System API', version='0.1.0')

# CORS (allow all for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Include routers
app.include_router(upload.router, prefix='/api', tags=['upload'])
app.include_router(documents.router, prefix='/api', tags=['documents'])
app.include_router(search.router, prefix='/api', tags=['search'])
app.include_router(chat.router, prefix='/api', tags=['chat'])

@app.get('/api/health')
async def health_check():
    return {'status': 'ok'}
