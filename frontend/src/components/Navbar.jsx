// src/components/Navbar.jsx
import React from 'react';
import { Calendar } from 'lucide-react';

export default function Navbar() {
  return (
    <header className="bg-white border-b border-gray-200 px-4 py-2 flex items-center justify-between">
      <h1 className="text-2xl font-semibold flex items-center">
        <Calendar className="w-6 h-6 mr-2" />
        Document Intelligent System
      </h1>
    </header>
  );
}
