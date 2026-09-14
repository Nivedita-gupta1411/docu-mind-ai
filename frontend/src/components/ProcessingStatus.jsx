// src/components/ProcessingStatus.jsx
import React from 'react';
import { Clock } from 'lucide-react';

export default function ProcessingStatus({ filename, status }) {
  return (
    <div className="flex items-center space-x-2 p-2 bg-gray-50 rounded">
      <Clock className="w-5 h-5 text-gray-600" />
      <span className="font-medium">{filename}</span>
      <span className="text-sm text-gray-500">{status}</span>
    </div>
  );
}
