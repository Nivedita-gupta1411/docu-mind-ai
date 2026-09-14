// src/components/EmptyState.jsx
import React from 'react';
import { Smile } from 'lucide-react';

export default function EmptyState({ message = 'No data found' }) {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center text-gray-500">
      <Smile className="w-12 h-12 mb-4" />
      <p className="text-lg">{message}</p>
    </div>
  );
}
