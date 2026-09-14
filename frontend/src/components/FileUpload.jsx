// src/components/FileUpload.jsx
import React, { useState } from 'react';
import { Upload } from 'lucide-react';
import { uploadMultipleDocuments } from '../services/api';

export default function FileUpload({ onUploadComplete }) {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState({ completed: 0, total: 0 });
  const [error, setError] = useState(null);

  const handleFiles = (e) => {
    const selected = Array.from(e.target.files);
    setFiles(selected);
  };

  const startUpload = async () => {
    if (files.length === 0) return;
    setUploading(true);
    setError(null);
    try {
      await uploadMultipleDocuments(files, (completed, total) => {
        setProgress({ completed, total });
      });
      if (onUploadComplete) onUploadComplete();
    } catch (e) {
      setError(e);
    } finally {
      setUploading(false);
      setFiles([]);
      setProgress({ completed: 0, total: 0 });
    }
  };

  return (
    <div className="border border-dashed rounded p-6 text-center">
      <label className="flex flex-col items-center cursor-pointer">
        <Upload className="w-12 h-12 text-gray-500 mb-2" />
        <span className="text-gray-600 mb-2">Click or drag files to upload</span>
        <input type="file" multiple onChange={handleFiles} className="hidden" disabled={uploading} />
      </label>
      {files.length > 0 && (
        <div className="mt-4">
          <ul className="text-left space-y-1 max-h-40 overflow-y-auto mb-2">
            {files.map((f) => (
              <li key={f.name} className="text-sm truncate">
                {f.name} ({(f.size / (1024 * 1024)).toFixed(2)} MB)
              </li>
            ))}
          </ul>
          <button
            onClick={startUpload}
            disabled={uploading}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
          >
            {uploading ? `Uploading ${progress.completed}/${progress.total}` : 'Upload'}
          </button>
          {error && <p className="text-red-600 mt-2">{error.userMessage || error.response?.data?.detail || error.message}</p>}
        </div>
      )}
    </div>
  );
}
