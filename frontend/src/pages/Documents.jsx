// src/pages/Documents.jsx
import React, { useState } from 'react';
import useDocuments from '../hooks/useDocuments';
import DocumentTable from '../components/DocumentTable';
import LoadingState from '../components/LoadingState';
import ErrorState from '../components/ErrorState';
import EmptyState from '../components/EmptyState';

export default function Documents() {
  const { documents, loading, error, refresh, removeDocument } = useDocuments();
  const [deletingId, setDeletingId] = useState(null);

  const handleDelete = async (id) => {
    setDeletingId(id);
    try {
      await removeDocument(id);
    } catch (e) {
      console.error(e);
    } finally {
      setDeletingId(null);
    }
  };

  if (loading) return <LoadingState />;
  if (error) return <ErrorState error={error} onRetry={refresh} />;
  if (documents.length === 0) return <EmptyState message="No documents uploaded" />;

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-bold">Documents</h2>
      <DocumentTable documents={documents} onDelete={handleDelete} />
    </div>
  );
}
