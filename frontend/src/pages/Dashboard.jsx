// src/pages/Dashboard.jsx
import React from 'react';
import StatCard from '../components/StatCard';
import DocumentCard from '../components/DocumentCard';
import useDocuments from '../hooks/useDocuments';
import LoadingState from '../components/LoadingState';
import EmptyState from '../components/EmptyState';

export default function Dashboard() {
  const { documents, loading, error } = useDocuments();

  if (loading) return <LoadingState />;
  if (error) return <div className='text-red-600'>Error loading documents</div>;

  const totalDocs = documents.length;
  const processedDocs = documents.filter((d) => d.status === 'processed').length;
  const totalChunks = documents.reduce((sum, d) => sum + (d.total_chunks || 0), 0);
  const recent = [...documents]
    .sort((a, b) => b.upload_date - a.upload_date)
    .slice(0, 5);

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Dashboard</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <StatCard title="Total Documents" value={totalDocs} />
        <StatCard title="Processed" value={processedDocs} />
        <StatCard title="Total Chunks" value={totalChunks} />
      </div>
      <h3 className="text-xl font-semibold mt-6">Recent Uploads</h3>
      {recent.length === 0 ? (
        <EmptyState message="No recent uploads" />
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {recent.map((doc) => (
            <DocumentCard key={doc.id} doc={doc} />
          ))}
        </div>
      )}
    </div>
  );
}
