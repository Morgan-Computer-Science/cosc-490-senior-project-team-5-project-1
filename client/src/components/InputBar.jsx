import React, { useState, useRef } from 'react';

const MAX_CHARS = 2000;

export default function InputBar({ onSend, disabled }) {
  const [text, setText] = useState('');
  const textareaRef = useRef(null);

  const canSend = text.trim().length > 0 && !disabled && text.length <= MAX_CHARS;

  const handleSubmit = () => {
    if (canSend) {
      onSend(text.trim());
      setText('');
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
      }
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleChange = (e) => {
    setText(e.target.value);
    const ta = textareaRef.current;
    if (ta) {
      ta.style.height = 'auto';
      ta.style.height = Math.min(ta.scrollHeight, 140) + 'px';
    }
  };

  return (
    <div className="input-area">
      <div className="input-row">
        <textarea
          ref={textareaRef}
          className="input-textarea"
          value={text}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder="Ask BearBot anything about Morgan State CS..."
          disabled={disabled}
          rows={1}
          aria-label="Chat message input"
        />
        <button
          className="send-btn"
          onClick={handleSubmit}
          disabled={!canSend}
          aria-label="Send message"
          title="Send message (Enter)"
        >
          ➤
        </button>
      </div>
      <div className="input-footer">
        <span className="input-hint">Enter to send · Shift+Enter for new line</span>
        <span className={`char-count ${text.length > MAX_CHARS * 0.9 ? 'warn' : ''}`}>
          {text.length}/{MAX_CHARS}
        </span>
      </div>
    </div>
  );
}
