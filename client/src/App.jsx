import React, { useState, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import InputBar from './components/InputBar';

const SESSION_KEY = 'bearbot_session_id';

// Default agent info shown before the first message is sent
const AGENT_DEFAULTS = {
  Freshman:  { name: 'Coach Bear',  emoji: '🌱', tagline: 'Your Freshman Guide' },
  Sophomore: { name: 'Dev Bear',    emoji: '💻', tagline: 'Career & Skills Coach' },
  Junior:    { name: 'Dev Bear',    emoji: '💻', tagline: 'Career & Skills Coach' },
  Senior:    { name: 'Cap Bear',    emoji: '🎓', tagline: 'Your Senior Strategist' },
};

function getOrCreateSession() {
  let id = sessionStorage.getItem(SESSION_KEY);
  if (!id) {
    id = uuidv4();
    sessionStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

export default function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [studentYear, setStudentYear] = useState('Freshman');
  const [sessionId] = useState(getOrCreateSession);
  const [activeAgent, setActiveAgent] = useState(AGENT_DEFAULTS['Freshman']);

  // When the year changes update the displayed agent immediately
  const handleYearChange = (year) => {
    setStudentYear(year);
    setActiveAgent(AGENT_DEFAULTS[year] || AGENT_DEFAULTS['Freshman']);
  };

  const sendMessage = useCallback(async (text) => {
    setError(null);

    const userMsg = {
      role: 'user',
      content: text,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, userMsg]);
    setIsLoading(true);

    try {
      const response = await axios.post('/api/chat/message', {
        message: text,
        sessionId,
        studentYear
      });

      // Update active agent from response
      if (response.data.agent) {
        setActiveAgent(response.data.agent);
      }

      const botMsg = {
        role: 'assistant',
        content: response.data.message,
        timestamp: response.data.timestamp || new Date().toISOString(),
        agent: response.data.agent,
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      const errText = err.response?.data?.error
        || 'BearBot is temporarily unavailable. Please try again.';
      setError(errText);
      setMessages(prev => prev.slice(0, -1));
    } finally {
      setIsLoading(false);
    }
  }, [sessionId, studentYear]);

  const handleNewChat = async () => {
    try {
      await axios.post('/api/chat/clear', { sessionId });
    } catch (_) {
      // Ignore clear errors
    }
    setMessages([]);
    setError(null);
  };

  return (
    <div className="app-container">
      <Sidebar
        studentYear={studentYear}
        setStudentYear={handleYearChange}
        onQuickAction={sendMessage}
        onNewChat={handleNewChat}
      />

      <div className="chat-main">
        <div className="chat-header">
          <div className="chat-header-info">
            <div className="status-indicator">
              <div className="status-dot" />
            </div>
            <div className="chat-header-text">
              <h2>
                {activeAgent.emoji} {activeAgent.name}
                <span className="agent-tagline"> — {activeAgent.tagline}</span>
              </h2>
              <p>Morgan State University · {studentYear} · Powered by Groq AI</p>
            </div>
          </div>
          <div className="header-badge">🐻 HBCU Proud</div>
        </div>

        {error && (
          <div className="error-toast">
            ⚠️ {error}
          </div>
        )}

        <ChatWindow
          messages={messages}
          isLoading={isLoading}
          onChipClick={sendMessage}
          activeAgent={activeAgent}
        />

        <InputBar onSend={sendMessage} disabled={isLoading} />
      </div>
    </div>
  );
}
