// src/pages/Search.jsx
import React, { useState } from 'react';
import { searchDocuments } from '../services/api';
import SearchResult from '../components/SearchResult';
import LoadingState from '../components/LoadingState';
import ErrorState from '../components/ErrorState';
import EmptyState from '../components/EmptyState';

export default function Search() {
  const [query, setQuery] = useState('');
  const [topK, setTopK] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const top = topK ? parseInt(topK, 10) : null;
      const data = await searchDocuments(query, top);
      setResults(data);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Semantic Search</h2>
      <form onSubmit={handleSearch} className="flex flex-col sm:flex-row gap-2">
        <input
          type="text"
          placeholder="Enter your query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 border rounded p-2"
          required
        />
        <input
          type="number"
          placeholder="Top K (1-20)"
          min={1}
          max={20}
          value={topK}
          onChange={(e) => setTopK(e.target.value)}
          className="w-32 border rounded p-2"
        />
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
        >
          Search
        </button>
      </form>
      {loading && <LoadingState />}
      {error && <ErrorState error={error} onRetry={() => handleSearch({ preventDefault: () => {}, })} />}
      {!loading && !error && results.length === 0 && <EmptyState message="No results" />}
      {!loading && !error && results.length > 0 && (
        <div className="space-y-4 mt-4">
          {results.map((item, idx) => (
            <SearchResult key={idx} result={item} />
          ))}
        </div>
      )}
    </div>
  );
}
