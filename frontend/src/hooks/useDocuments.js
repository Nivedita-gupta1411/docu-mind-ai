import { useState, useEffect, useCallback } from 'react';
import { getDocuments, deleteDocument } from '../services/api';

export default function useDocuments() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchDocs = useCallback(async () => {
    setLoading(true);
    try {
      const docs = await getDocuments();
      // Normalize document ID for UI components
      const normalized = docs.map(doc => ({ ...doc, id: doc._id }));
      setDocuments(normalized);
      setError(null);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchDocs();
  }, [fetchDocs]);

  const removeDocument = async (id) => {
    await deleteDocument(id);
    // Optimistically remove from state
    setDocuments((prev) => prev.filter((doc) => doc.id !== id));
  };

  return { documents, loading, error, refresh: fetchDocs, removeDocument };
}
