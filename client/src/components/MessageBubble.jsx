import React from 'react';
import ReactMarkdown from 'react-markdown';

function formatTime(timestamp) {
  return new Date(timestamp).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit'
  });
}

export default function MessageBubble({ message }) {
  const isUser = message.role === 'user';

  return (
    <div className={`message-row ${isUser ? 'user' : ''}`}>
      <div className={`message-avatar ${isUser ? 'user-av' : 'bot'}`}>
        {isUser ? '👤' : '🐻'}
      </div>
      <div className="message-content">
        <div className={`message-bubble ${isUser ? 'user' : 'bot'}`}>
          {isUser ? (
            message.content
          ) : (
            <ReactMarkdown>{message.content}</ReactMarkdown>
          )}
        </div>
        <div className="message-time">{formatTime(message.timestamp)}</div>
      </div>
    </div>
  );
}
