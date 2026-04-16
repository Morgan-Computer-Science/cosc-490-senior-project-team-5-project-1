import React, { useState, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import InputBar from './components/InputBar';

const SESSION_KEY = 'bearbot_session_id';

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

      const botMsg = {
        role: 'assistant',
        content: response.data.message,
        timestamp: response.data.timestamp || new Date().toISOString()
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      const errText = err.response?.data?.error
        || 'BearBot is temporarily unavailable. Please try again.';
      setError(errText);
      // Remove the user message on error so they can retry
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
        setStudentYear={setStudentYear}
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
              <h2>BearBot — CS Academic Advisor</h2>
              <p>Morgan State University · {studentYear} Mode · Powered by Groq AI</p>
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
        />

        <InputBar onSend={sendMessage} disabled={isLoading} />
      </div>
    </div>
  );
}
