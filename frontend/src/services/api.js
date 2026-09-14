// src/services/api.js
import axios from 'axios';

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || 'http://localhost:8001/api').replace(/\/$/, '');

// Development-only diagnostic. Never log secrets here.
if (import.meta.env.DEV) {
  console.info('[Document Intelligent System] API base URL:', API_BASE_URL);
}

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 120000,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (!error.response) {
      error.userMessage = `Cannot reach the FastAPI backend at ${API_BASE_URL}`;
    } else {
      const detail = error.response.data?.detail;
      error.userMessage = detail || `Backend request failed (${error.response.status})`;
    }
    return Promise.reject(error);
  },
);

export const healthCheck = async () => {
  const res = await api.get('/health');
  return res.data;
};

export const uploadDocument = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const res = await api.post('/upload', formData);
  return res.data;
};

// For multiple files, call uploadDocument repeatedly
export const uploadMultipleDocuments = async (files, onProgress) => {
  const results = [];
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const result = await uploadDocument(file);
    results.push(result);
    if (onProgress) onProgress(i + 1, files.length);
  }
  return results;
};

export const getDocuments = async () => {
  const res = await api.get('/documents');
  return res.data.documents;
};

export const getDocument = async (id) => {
  const res = await api.get(`/documents/${id}`);
  return res.data;
};

export const deleteDocument = async (id) => {
  const res = await api.delete(`/documents/${id}`);
  return res.data;
};

export const searchDocuments = async (query, top_k = null, doc_ids = null) => {
  const payload = { query };
  if (top_k !== null) payload.top_k = top_k;
  if (doc_ids) payload.doc_ids = doc_ids;
  const res = await api.post('/search', payload);
  return res.data.results;
};

export const chatQuery = async (question, top_k = null, doc_ids = null) => {
  const payload = { question };
  if (top_k !== null) payload.top_k = top_k;
  if (doc_ids) payload.doc_ids = doc_ids;
  const res = await api.post('/chat', payload);
  return res.data;
};

export default {
  healthCheck,
  uploadDocument,
  uploadMultipleDocuments,
  getDocuments,
  getDocument,
  deleteDocument,
  searchDocuments,
  chatQuery,
};
