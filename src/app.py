import streamlit as st
from rag import answer_question

st.set_page_config(
    page_title="Morgan CS AI Advising Assistant",
    page_icon="🐻",
    layout="centered"
)

st.markdown("""
<style>
body, p, li, span, div, label {
    color: #111111 !important;
}

.stApp {
    background-color: #f5f7fb;
}

/* Main header */
.header-box {
    background-color: #0c2340;
    color: white !important;
    padding: 1.2rem;
    border-radius: 12px;
    margin-bottom: 1rem;
}

.header-box h1, .header-box p {
    color: white !important;
}

/* Info card */
.card {
    background: white;
    color: #111111 !important;
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

/* Expander */
details {
    background: white !important;
    border-radius: 12px !important;
    padding: 0.4rem 0.8rem 0.8rem 0.8rem !important;
    margin-bottom: 1rem !important;
}

details summary {
    color: #0c2340 !important;
    font-weight: 700 !important;
}

details * {
    color: #111111 !important;
}

/* Agent tag */
.agent-tag {
    background-color: #f2a900;
    color: #111111 !important;
    padding: 0.3rem 0.7rem;
    border-radius: 20px;
    font-weight: bold;
}

/* Source chips */
.source-chip {
    display: inline-block;
    background: #e6edf7;
    color: #0c2340 !important;
    padding: 0.4rem 0.7rem;
    border-radius: 20px;
    margin: 0.2rem;
    font-size: 0.9rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-box">
    <h1>🐻 Morgan CS AI Advising Assistant</h1>
    <p>AI agent system for advising, prerequisites, policies, and student support.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<strong>Morgan State Computer Science Support Tool</strong><br>
This system helps students with course planning, prerequisites, advising, and support resources using Morgan CS materials.
</div>
""", unsafe_allow_html=True)

with st.expander("Example Questions"):
    st.markdown("""
- What is the prerequisite for COSC 112?
- How many credits are required to graduate?
- When do students take COSC 490?
- What courses are in the freshman year?
- Is tutoring available?
""")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Ask me about courses, prerequisites, planning, or support resources."
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a question")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    result = answer_question(prompt)

    with st.chat_message("assistant"):
        st.markdown(f"<span class='agent-tag'>{result['agent']}</span>", unsafe_allow_html=True)
        st.write(result["answer"])

        st.markdown("**Sources:**")
        if result["sources"]:
            chips = "".join([f"<span class='source-chip'>{src}</span>" for src in result["sources"]])
            st.markdown(chips, unsafe_allow_html=True)
        else:
            st.write("None")

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"]
    })
