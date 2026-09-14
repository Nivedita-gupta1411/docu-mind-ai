import os
from typing import List, Dict

import faiss
import numpy as np

from ..config import settings


class VectorStore:
    """
    FAISS vector store wrapper.

    Embeddings are persisted to disk along with their
    corresponding chunk metadata.
    """

    def __init__(self):
        self.dimension = settings.EMBEDDING_DIMENSION

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.metadata: List[Dict] = []

        self._load()

    def add_embeddings(
        self,
        embeddings: List[np.ndarray],
        chunks: List[Dict]
    ):
        if not embeddings:
            return

        vectors = np.vstack(
            embeddings
        ).astype("float32")

        if vectors.shape[1] != self.dimension:
            raise ValueError(
                f"Embedding dimension mismatch: "
                f"expected {self.dimension}, "
                f"got {vectors.shape[1]}"
            )

        self.index.add(vectors)

        self.metadata.extend(chunks)

        self._save()

    def search(
        self,
        query_vec: np.ndarray,
        k: int = 5
    ):
        query = np.asarray(
            query_vec,
            dtype="float32"
        ).reshape(1, -1)

        if query.shape[1] != self.dimension:
            raise ValueError(
                f"Query dimension mismatch: "
                f"expected {self.dimension}, "
                f"got {query.shape[1]}"
            )

        k = min(k, self.index.ntotal)

        return self.index.search(
            query,
            k
        )

    def get_chunk(self, idx: int) -> Dict:
        return self.metadata[idx]

    def save(self):
        self._save()

    def _store_path(self) -> str:
        return os.path.join(
            settings.VECTOR_STORE_DIR,
            "faiss.index"
        )

    def _metadata_path(self) -> str:
        return os.path.join(
            settings.VECTOR_STORE_DIR,
            "metadata.npy"
        )

    def _save(self):
        os.makedirs(
            settings.VECTOR_STORE_DIR,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            self._store_path()
        )

        np.save(
            self._metadata_path(),
            np.array(
                self.metadata,
                dtype=object
            )
        )

    def _load(self):
        try:
            if os.path.exists(
                self._store_path()
            ):
                self.index = faiss.read_index(
                    self._store_path()
                )

                self.metadata = np.load(
                    self._metadata_path(),
                    allow_pickle=True
                ).tolist()

        except Exception as e:
            print(
                f"[VectorStore] "
                f"Failed to load persisted store: {e}"
            )

            self.index = faiss.IndexFlatL2(
                self.dimension
            )

            self.metadata = []


_vector_store = None


def get_vector_store() -> VectorStore:
    global _vector_store

    if _vector_store is None:
        _vector_store = VectorStore()

    return _vector_store