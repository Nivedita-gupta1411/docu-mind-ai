import React from 'react';
import FileUpload from '../components/FileUpload';

export default function Upload() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Upload Documents</h2>
      <FileUpload />
      <p className="text-sm text-gray-500">After processing completes, open Documents to see the stored document and chunk count.</p>
    </div>
  );
}
