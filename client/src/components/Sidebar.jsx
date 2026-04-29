import React from 'react';

// ── Agent metadata (mirrors backend agents.py) ──────────────────────────────
const AGENTS = [
  {
    name: 'Coach Bear',
    emoji: '🌱',
    tagline: 'Your Freshman Guide',
    years: ['Freshman'],
    description: 'Patient, encouraging, and here to help you survive (and love) your first year at Morgan.',
  },
  {
    name: 'Dev Bear',
    emoji: '💻',
    tagline: 'Career & Skills Coach',
    years: ['Sophomore', 'Junior'],
    description: 'Focused on leveling up your skills, landing internships, and crushing technical interviews.',
  },
  {
    name: 'Cap Bear',
    emoji: '🎓',
    tagline: 'Your Senior Strategist',
    years: ['Senior'],
    description: 'Helping you close out strong — graduation requirements, job offers, and everything in between.',
  },
];

// ── Year-specific quick actions ──────────────────────────────────────────────
const QUICK_ACTIONS = {
  Freshman: [
    "What courses should I take first?",
    "How do I meet my academic advisor?",
    "Where is the tutoring center?",
    "What is FAFSA and how do I apply?",
    "What clubs should I join in CS?",
    "I'm struggling in COSC 111 — help!",
    "How do I navigate Banner?",
    "What gen ed classes do I need?",
  ],
  Sophomore: [
    "How do I survive Data Structures?",
    "How do I start looking for internships?",
    "What should my first GitHub project be?",
    "When should I start LeetCode?",
    "What CS concentration should I pick?",
    "What summer research programs exist?",
    "How do I build my first portfolio?",
    "What's the deal with Discrete Math?",
  ],
  Junior: [
    "How do I land a summer internship?",
    "What's a realistic LeetCode study plan?",
    "What conferences should I attend?",
    "How do I prep for technical interviews?",
    "Should I apply to grad school?",
    "What electives should I take?",
    "How do I build a strong GitHub profile?",
    "What is system design and do I need it?",
  ],
  Senior: [
    "Am I on track to graduate?",
    "How do I apply for graduation?",
    "How do I manage my capstone project?",
    "How do I negotiate a job offer?",
    "Should I go to grad school?",
    "How do I write a statement of purpose?",
    "What's left on my degree audit?",
    "How do I polish my resume for full-time roles?",
  ],
};

const yearOptions = [
  { value: 'Freshman',  emoji: '🌱', label: 'Freshman  (0–29 credits)' },
  { value: 'Sophomore', emoji: '📚', label: 'Sophomore (30–59 credits)' },
  { value: 'Junior',    emoji: '💻', label: 'Junior    (60–89 credits)' },
  { value: 'Senior',    emoji: '🎓', label: 'Senior    (90+ credits)' },
];

function getAgentForYear(year) {
  return AGENTS.find(a => a.years.includes(year)) || AGENTS[0];
}

export default function Sidebar({ studentYear, setStudentYear, onQuickAction, onNewChat }) {
  const agent = getAgentForYear(studentYear);
  const quickActions = QUICK_ACTIONS[studentYear] || QUICK_ACTIONS['Freshman'];

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

      {/* Active Agent Card */}
      <div className="sidebar-section">
        <p className="sidebar-section-title">Active Agent</p>
        <div className="agent-card">
          <div className="agent-card-header">
            <span className="agent-card-emoji">{agent.emoji}</span>
            <div>
              <div className="agent-card-name">{agent.name}</div>
              <div className="agent-card-tagline">{agent.tagline}</div>
            </div>
          </div>
          <p className="agent-card-desc">{agent.description}</p>
        </div>
      </div>

      {/* Year-specific Quick Questions */}
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

      {/* Footer */}
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
