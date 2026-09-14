// src/components/SourceCitation.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import { BookOpen } from 'lucide-react';

export default function SourceCitation({ source }) {
  const { filename, chunk_id, score, document_id } = source;
  return (
    <div className="flex items-center text-sm text-gray-600 border-t pt-2 mt-2">
      <BookOpen className="w-4 h-4 mr-1" />
      <span className="mr-2">{filename}</span>
      {chunk_id && <span className="mr-2">{chunk_id}</span>}
      <span className="mr-2">Score: {score.toFixed(4)}</span>
      {/* link to document details */}
      <Link to={`/documents/${document_id}`} className="text-blue-500 hover:underline">
        View
      </Link>
    </div>
  );
}
