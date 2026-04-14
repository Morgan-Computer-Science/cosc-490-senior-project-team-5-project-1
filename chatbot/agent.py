import google.generativeai as genai
import streamlit as st

class MSUAgent:
    def __init__(self):
        # 1. AI Configuration
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel("gemini-3-flash-preview")
        
        # 2. MSU Agent Instructions (The Persona)
        self.system_instructions = """
        You are the 'MSU Bear Advisor', the digital face of Morgan State University CS. 
        IDENTITY: Helpful, energetic, and extremely knowledgeable about Richardson Hall.
        CORE MISSIONS:
        1. Course Guidance: Recommend COSC 111/112 (Freshman), 220/241/281 (Sophomore).
        2. Advising: Under 30 credits -> CASA; Over 30 credits -> CS Dept.
        3. Culture: Use 'Bears' and 'Richardson Hall' frequently. Always offer to create a sample 4-year graduation map.
        """

    def get_response(self, user_input):
        full_prompt = f"System Context: {self.system_instructions}\nUser Query: {user_input}"
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Bear Advisor encountered a temporary technical hurdle: {e}"