// src/components/DocumentTable.jsx
import React from 'react';
import { Trash2 } from 'lucide-react';

export default function DocumentTable({ documents, onDelete }) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white border rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-4 py-2 text-left">Filename</th>
            <th className="px-4 py-2 text-left">Type</th>
            <th className="px-4 py-2 text-left">Upload Date</th>
            <th className="px-4 py-2 text-left">Status</th>
            <th className="px-4 py-2 text-left">Chunks</th>
            <th className="px-4 py-2 text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          {documents.map((doc) => (
            <tr key={doc.id} className="border-t">
              <td className="px-4 py-2">
                <a href={`/documents/${doc.id}`} className="text-blue-600 hover:underline">
                  {doc.filename}
                </a>
              </td>
              <td className="px-4 py-2 text-sm">{doc.file_type.toUpperCase()}</td>
              <td className="px-4 py-2 text-sm">
                {new Date(doc.upload_date * 1000).toLocaleDateString()}
              </td>
              <td className="px-4 py-2 text-sm capitalize">{doc.status}</td>
              <td className="px-4 py-2 text-sm">{doc.total_chunks ?? 0}</td>
              <td className="px-4 py-2 text-center">
                <button
                  onClick={() => onDelete(doc.id)}
                  className="text-red-600 hover:text-red-800"
                  title="Delete"
                >
                  <Trash2 className="w-5 h-5" />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
