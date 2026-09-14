// src/pages/DocumentDetails.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getDocument } from '../services/api';
import LoadingState from '../components/LoadingState';
import ErrorState from '../components/ErrorState';
import EmptyState from '../components/EmptyState';

export default function DocumentDetails() {
  const { id } = useParams();
  const [doc, setDoc] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDoc = async () => {
      try {
        const data = await getDocument(id);
        setDoc(data);
        setError(null);
      } catch (e) {
        setError(e);
      } finally {
        setLoading(false);
      }
    };
    fetchDoc();
  }, [id]);

  if (loading) return <LoadingState />;
  if (error) return <ErrorState error={error} onRetry={() => window.location.reload()} />;
  if (!doc) return <EmptyState message="Document not found" />;

  return (
    <div className="max-w-3xl mx-auto p-4 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Document Details</h2>
      <dl className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <dt className="font-medium text-gray-600">Filename</dt>
          <dd className="text-gray-800">{doc.filename}</dd>
        </div>
        <div>
          <dt className="font-medium text-gray-600">File Type</dt>
          <dd className="text-gray-800">{doc.file_type}</dd>
        </div>
        <div>
          <dt className="font-medium text-gray-600">Upload Date</dt>
          <dd className="text-gray-800">{new Date(doc.upload_date).toLocaleString()}</dd>
        </div>
        <div>
          <dt className="font-medium text-gray-600">Status</dt>
          <dd className="text-gray-800">{doc.status}</dd>
        </div>
        <div>
          <dt className="font-medium text-gray-600">Total Chunks</dt>
          <dd className="text-gray-800">{doc.total_chunks ?? 'N/A'}</dd>
        </div>
        <div>
          <dt className="font-medium text-gray-600">Size (MB)</dt>
          <dd className="text-gray-800">{doc.size_mb?.toFixed(2) ?? 'N/A'}</dd>
        </div>
      </dl>
    </div>
  );
}
