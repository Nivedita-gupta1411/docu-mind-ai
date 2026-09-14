import os
import faiss
import numpy as np
from typing import List, Dict
from ..config import settings

class VectorStore:
    """FAISS vector store wrapper that stores embeddings and associated chunk metadata.
    The index is persisted to disk under settings.VECTOR_STORE_DIR.
    """
    def __init__(self):
        # Determine embedding dimension; fallback to 384 if not set
        self.dimension = getattr(settings, 'EMBEDDING_DIMENSION', 384)
        self.index = faiss.IndexFlatL2(self.dimension)
        self.metadata: List[Dict] = []  # parallel list to vectors
        self._load()

    def add_embeddings(self, embeddings: List[np.ndarray], chunks: List[Dict]):
        """Add a batch of embeddings and their chunk metadata.
        Args:
            embeddings: list of numpy arrays with shape (dim,)
            chunks: list of dicts, each containing at least 'text' and 'metadata'
        """
        if not embeddings:
            return
        vectors = np.vstack(embeddings).astype('float32')
        self.index.add(vectors)
        self.metadata.extend(chunks)
        self._save()

    def search(self, query_vec: np.ndarray, k: int = 5):
        """Search for the top‑k most similar vectors.
        Returns:
            distances (np.ndarray): shape (1, k)
            indices (np.ndarray): shape (1, k)
        """
        query = np.asarray(query_vec, dtype='float32').reshape(1, -1)
        distances, indices = self.index.search(query, k)
        return distances, indices

    def get_chunk(self, idx: int) -> Dict:
        """Retrieve the stored chunk (text + metadata) for a given index."""
        return self.metadata[idx]

    def save(self) -> None:
        """Public method to persist the FAISS index and metadata to disk."""
        self._save()

    # ---------------------------------------------------------------------
    # Persistence helpers
    # ---------------------------------------------------------------------
    def _store_path(self) -> str:
        return os.path.join(settings.VECTOR_STORE_DIR, 'faiss.index')

    def _metadata_path(self) -> str:
        return os.path.join(settings.VECTOR_STORE_DIR, 'metadata.npy')

    def _save(self):
        os.makedirs(settings.VECTOR_STORE_DIR, exist_ok=True)
        faiss.write_index(self.index, self._store_path())
        # Save metadata list as numpy object array for simplicity
        np.save(self._metadata_path(), np.array(self.metadata, dtype=object))

    def _load(self):
        try:
            if os.path.exists(self._store_path()):
                self.index = faiss.read_index(self._store_path())
                self.metadata = np.load(self._metadata_path(), allow_pickle=True).tolist()
        except Exception as e:
            # If loading fails, start with a fresh index
            print(f"[VectorStore] Failed to load persisted store: {e}")
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

# Singleton accessor
_vector_store: VectorStore = None

def get_vector_store() -> VectorStore:
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStore()
    return _vector_store
