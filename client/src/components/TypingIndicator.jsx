import React from 'react';

export default function TypingIndicator() {
  return (
    <div className="typing-indicator">
      <div className="message-avatar bot">🐻</div>
      <div className="typing-bubble">
        <span className="typing-text">BearBot is typing</span>
        <div className="typing-dot" />
        <div className="typing-dot" />
        <div className="typing-dot" />
      </div>
    </div>
  );
}
