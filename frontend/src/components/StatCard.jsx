// src/components/StatCard.jsx
import React from 'react';
import { TrendingUp } from 'lucide-react';

export default function StatCard({ title, value }) {
  return (
    <div className="bg-white rounded-lg shadow p-4 flex items-center">
      <TrendingUp className="w-6 h-6 text-blue-500 mr-3" />
      <div>
        <p className="text-sm text-gray-500">{title}</p>
        <p className="text-xl font-semibold">{value}</p>
      </div>
    </div>
  );
}
