// src/components/LoadingState.jsx
import React from 'react';
import { Loader2 } from 'lucide-react';

export default function LoadingState({ message = 'Loading...' }) {
  return (
    <div className="flex items-center justify-center py-8">
      <Loader2 className="animate-spin mr-2 w-6 h-6 text-gray-600" />
      <span className="text-gray-600">{message}</span>
    </div>
  );
}
