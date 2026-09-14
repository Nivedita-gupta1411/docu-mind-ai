// src/components/ChatMessage.jsx
import React from 'react';
import { Bot, User } from 'lucide-react';

export default function ChatMessage({ sender, content }) {
  const isUser = sender === 'user';
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className={`flex items-start max-w-md ${isUser ? 'flex-row-reverse' : ''}`}>
        {isUser ? (
          <User className="w-6 h-6 text-blue-600 mr-2" />
        ) : (
          <Bot className="w-6 h-6 text-gray-600 mr-2" />
        )}
        <div className={`rounded-lg p-3 ${isUser ? 'bg-blue-100' : 'bg-gray-100'}`}>
          <p className="whitespace-pre-wrap">{content}</p>
        </div>
      </div>
    </div>
  );
}
