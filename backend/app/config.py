import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / '.env'
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)

class Settings:
    PROJECT_ROOT: Path = BASE_DIR
    DEBUG: bool = os.getenv('DEBUG', 'false').lower() == 'true'
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv('MAX_UPLOAD_SIZE_MB', '50'))
    ALLOWED_FILE_TYPES = {'.pdf', '.docx', '.txt', '.eml'}
    UPLOAD_DIR: Path = PROJECT_ROOT / 'data' / 'uploads'
    PROCESSED_DIR: Path = PROJECT_ROOT / 'data' / 'processed'
    VECTOR_STORE_DIR: Path = PROJECT_ROOT / 'data' / 'vector_store'
    for p in [UPLOAD_DIR, PROCESSED_DIR, VECTOR_STORE_DIR]:
        p.mkdir(parents=True, exist_ok=True)
    MONGODB_URI: str = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
    MONGODB_DB: str = os.getenv('MONGODB_DB', 'doc_intel')
    EMBEDDING_MODEL: str = os.getenv('EMBEDDING_MODEL','gemini-embedding-001')

    EMBEDDING_DIMENSION: int = int(os.getenv('EMBEDDING_DIMENSION','768'))
    LLM_PROVIDER: str = os.getenv('LLM_PROVIDER', 'gemini')
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    GEMINI_API_KEY: str = os.getenv('GEMINI_API_KEY', '')
    GEMINI_MODEL: str = os.getenv('GEMINI_MODEL', 'gemini-3.6-flash')
    CHUNK_SIZE_WORDS: int = int(os.getenv('CHUNK_SIZE_WORDS', '700'))
    CHUNK_OVERLAP_WORDS: int = int(os.getenv('CHUNK_OVERLAP_WORDS', '100'))
    TOP_K: int = int(os.getenv('TOP_K', '5'))

settings = Settings()
