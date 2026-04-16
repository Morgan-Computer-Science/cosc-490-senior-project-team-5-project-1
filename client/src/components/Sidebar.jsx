import React from 'react';

const quickActions = [
  "What courses should a freshman take?",
  "How do I register for classes?",
  "Where can I get free tutoring?",
  "How do I find a CS internship?",
  "What clubs can I join in CS?",
  "How do I apply for financial aid?",
  "I'm struggling with Data Structures",
  "What are the CS degree requirements?",
  "When is the add/drop deadline?",
  "How do I prepare for tech interviews?",
  "What GPA do I need for grad school?",
  "Tell me about NSBE at Morgan"
];

const yearOptions = [
  { value: 'Freshman', emoji: '🌱', label: 'Freshman (0–29 credits)' },
  { value: 'Sophomore', emoji: '📚', label: 'Sophomore (30–59 credits)' },
  { value: 'Junior', emoji: '💻', label: 'Junior (60–89 credits)' },
  { value: 'Senior', emoji: '🎓', label: 'Senior (90+ credits)' },
];

export default function Sidebar({ studentYear, setStudentYear, onQuickAction, onNewChat }) {
  return (
    <div className="sidebar">
      {/* Header */}
      <div className="sidebar-header">
        <div className="sidebar-logo">
          <span className="sidebar-logo-bear">🐻</span>
          <div className="sidebar-logo-text">
            <h1>BearBot</h1>
            <span>Morgan State CS Advisor</span>
          </div>
        </div>
        <p className="sidebar-tagline">"The Truth" — Est. 1867</p>
      </div>

      {/* Year Selector */}
      <div className="sidebar-section">
        <p className="sidebar-section-title">Your Year</p>
        <div className="year-selector">
          {yearOptions.map(({ value, emoji, label }) => (
            <label
              key={value}
              className={`year-label ${studentYear === value ? 'active' : ''}`}
            >
              <input
                type="radio"
                name="studentYear"
                value={value}
                checked={studentYear === value}
                onChange={() => setStudentYear(value)}
              />
              <span className="year-emoji">{emoji}</span>
              {value}
            </label>
          ))}
        </div>
      </div>

      {/* Quick Questions */}
      <div className="sidebar-section">
        <p className="sidebar-section-title">Quick Questions</p>
        {quickActions.map((action, i) => (
          <button
            key={i}
            className="quick-action-btn"
            onClick={() => onQuickAction(action)}
          >
            {action}
          </button>
        ))}
      </div>

      {/* New Chat Button */}
      <button className="new-chat-btn" onClick={onNewChat}>
        ✨ New Conversation
      </button>

      {/* Footer with real contact info */}
      <div className="sidebar-footer">
        <p>
          <strong>Need official advising?</strong><br />
          📧 scmns.advising@morgan.edu<br />
          📍 Carnegie Hall<br />
          📞 443-885-3333<br />
          <br />
          <strong>Counseling Center:</strong><br />
          📞 443-885-3130
        </p>
      </div>
    </div>
  );
}
