import streamlit as st
from chatbot.agent import MSUAgent

# Set Page Config (Important for layout)
st.set_page_config(page_title="MSU Bear Advisor", layout="wide")

# --- CUSTOM CSS (The Brand New Aesthetic) ---
st.markdown("""
    <style>
    /* 1. Global Page: Morgan Blue Background */
    .stApp {
        background-color: #002D62 !important; /* Morgan Blue */
    }
    
    /* 2. Hide standard Streamlit header/footer */
    header, footer {visibility: hidden;}

    /* 3. Style the "Floating" Chat Card on the right */
    .interactive-card {
        background-color: #F8F9FA; /* Light Gray */
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        margin-top: 60px;
        height: 600px;
        overflow-y: auto;
    }
    
    /* 4. Large Text on the Left Panel */
    .brand-text {
        color: white;
        text-align: center;
        margin-top: 150px;
    }
    .brand-text h1 {
        font-size: 70px !important;
        font-weight: 800 !important;
        line-height: 1.1;
    }
    .brand-text p {
        font-size: 24px;
        margin-top: 20px;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "agent" not in st.session_state:
    st.session_state.agent = MSUAgent()
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome back, Bear! 🐻 Ready to conquer your CS degree? Ask me anything!"}]

# --- TWO-COLUMN LAYOUT (The Idea from Screenshot) ---
left_col, right_col = st.columns([1.2, 1])

# --- LEFT PANEL: The Morgan Spirit (Large & Center) ---
with left_col:
    st.markdown('<div class="brand-text">', unsafe_allow_html=True)
    st.image("https://www.morgan.edu/Images/News/MorganLogo-Horizontal.png", width=350)
    st.write("# **Bear Advisor**")
    st.write("<p>Your digital guide through Richardson Hall and beyond.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANEL: The Modern Interactive Card ---
with right_col:
    # Adding spacing to center the card vertically
    st.write("##")
    st.write("##")
    
    # Create the floating chat window
    with st.container():
        st.markdown('<div class="interactive-card">', unsafe_allow_html=True)
        
        # Morgan Orange Header like a web app
        st.markdown("<h2 style='color:#FF6B00; text-align:center;'>Morgan State CS Chat</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # 1. DISPLAY CHAT HISTORY
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. CHAT INPUT AT THE BOTTOM
    if prompt := st.chat_input("COSC graduation plans..."):
        # Store user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.write(prompt)
            
        # 3. GET AI RESPONSE
        with st.chat_message("assistant"):
            with st.spinner("🐻 Consultant is consulting..."):
                response = st.session_state.agent.get_response(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})