// src/components/DocumentCard.jsx
import React from 'react';
import { FileText } from 'lucide-react';
import { NavLink } from 'react-router-dom';

export default function DocumentCard({ doc }) {
  return (
    <NavLink to={`/documents/${doc.id}`} className="block border rounded-lg p-4 hover:bg-gray-50 transition">
      <div className="flex items-center space-x-3">
        <FileText className="w-5 h-5 text-gray-600" />
        <div className="flex-1">
          <p className="font-medium text-gray-800 truncate">{doc.filename}</p>
          <p className="text-sm text-gray-500">{doc.file_type.toUpperCase()} • {new Date(doc.upload_date * 1000).toLocaleDateString()}</p>
        </div>
        <span className="text-xs bg-gray-200 rounded px-2 py-0.5">{doc.status}</span>
      </div>
    </NavLink>
  );
}
