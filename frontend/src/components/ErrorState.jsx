// src/components/ErrorState.jsx
import React from 'react';
import { AlertCircle } from 'lucide-react';

export default function ErrorState({ error, onRetry }) {
  return (
    <div className="flex flex-col items-center justify-center py-8 text-center text-red-600">
      <AlertCircle className="w-12 h-12 mb-4" />
      <p className="mb-2">{error?.message || 'An error occurred'}</p>
      {onRetry && (
        <button
          onClick={onRetry}
          className="mt-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
        >
          Retry
        </button>
      )}
    </div>
  );
}
