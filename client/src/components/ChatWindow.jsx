import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';

const welcomeChips = [
  "What classes should a freshman take?",
  "How do I find a CS internship?",
  "Where's the tutoring center?",
  "Explain Data Structures to me",
  "What GPA do I need for grad school?",
  "Tell me about NSBE at Morgan",
  "How do I prepare for tech interviews?",
  "What support services are available?"
];

export default function ChatWindow({ messages, isLoading, onChipClick }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  if (messages.length === 0) {
    return (
      <div className="chat-window">
        <div className="welcome-screen">
          <span className="welcome-bear">🐻</span>
          <div className="welcome-msu-bar">
            <span>🏫</span> Morgan State University · HBCU
          </div>
          <h2>Hello, Morgan Bear!</h2>
          <p>
            I'm BearBot, your AI academic advisor for Morgan State's
            Computer Science program. Ask me about courses, advising,
            resources, internships, study tips, or anything CS-related!
          </p>
          <div className="welcome-chips">
            {welcomeChips.map((chip, i) => (
              <button key={i} className="chip" onClick={() => onChipClick(chip)}>
                {chip}
              </button>
            ))}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="chat-window">
      {messages.map((msg, i) => (
        <MessageBubble key={i} message={msg} />
      ))}
      {isLoading && <TypingIndicator />}
      <div ref={bottomRef} />
    </div>
  );
}
