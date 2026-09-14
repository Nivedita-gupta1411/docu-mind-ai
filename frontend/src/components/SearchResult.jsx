// src/components/SearchResult.jsx
import React from 'react';
import { FileText } from 'lucide-react';

export default function SearchResult({ result }) {
  const { text, metadata, score } = result;
  const filename = metadata?.filename || 'Unknown';
  const chunkId = metadata?.chunk_id || '';

  return (
    <div className="border rounded p-4 mb-4 bg-white shadow-sm">
      <div className="flex items-center mb-2">
        <FileText className="w-5 h-5 mr-2 text-gray-600" />
        <span className="font-medium text-gray-800">{filename}</span>
        {chunkId && <span className="ml-2 text-sm text-gray-500">{chunkId}</span>}
      </div>
      <p className="text-gray-700 mb-2 whitespace-pre-wrap">{text}</p>
      <p className="text-sm text-gray-500">Score: {score.toFixed(4)}</p>
    </div>
  );
}
