// src/pages/Chat.jsx
import React, { useState } from 'react';
import ChatMessage from '../components/ChatMessage';
import ChatInput from '../components/ChatInput';
import SourceCitation from '../components/SourceCitation';
import LoadingState from '../components/LoadingState';
import ErrorState from '../components/ErrorState';
import { chatQuery } from '../services/api';

export default function Chat() {
  const [messages, setMessages] = useState([]); // {sender: 'user'|'assistant', content: string, sources?: []}
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSend = async (text) => {
    const userMsg = { sender: 'user', content: text };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);
    setError(null);
    try {
      const resp = await chatQuery(text);
      const assistantMsg = { sender: 'assistant', content: resp.answer, sources: resp.sources };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  };

  const renderMessage = (msg, idx) => (
    <div key={idx}>
      <ChatMessage sender={msg.sender} content={msg.content} />
      {msg.sender === 'assistant' && msg.sources && msg.sources.length > 0 && (
        <div className="ml-8">
          {msg.sources.map((src, i) => (
            <SourceCitation key={i} source={src} />
          ))}
        </div>
      )}
    </div>
  );

  return (
    <div className="flex flex-col h-full">
      <h2 className="text-2xl font-bold mb-4">AI Document Assistant</h2>
      <div className="flex-1 overflow-y-auto mb-4">
        {messages.map(renderMessage)}
        {loading && <LoadingState message="Thinking..." />}
        {error && <ErrorState error={error} onRetry={() => {}} />}
      </div>
      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
}
