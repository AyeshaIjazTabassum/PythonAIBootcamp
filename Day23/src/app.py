import streamlit as st
from google import genai  # Corrected import for the new SDK
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Study Helper", page_icon="📚")

# --- API CONFIGURATION ---
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please set GEMINI_API_KEY in Hugging Face Secrets.")
    st.stop()

# Initialize the new GenAI Client
client = genai.Client(api_key=api_key)

# --- PERSONA DEFINITIONS ---
PERSONAS = {
    "Teacher 🍎": {
        "system_prompt": "You are a strict Teacher. Your goal is to explain complex concepts in simple terms. Be concise and academic. Avoid giving answers directly; instead, guide the user to the solution.",
        "welcome": "Hello! I'm your Teacher. What topic shall we break down today?"
    },
    "Peer Mentor 💡": {
        "system_prompt": "You are a friendly career mentor. Explain gently. Give simple real-world examples to explain concepts.",
        "welcome": "Hey there. I'm your Peer Mentor. Let's talk about your progress and how this fits into the bigger picture."
    },
    "Critic ⚖️": {
        "system_prompt": "You are a harsh code reviewer. Point out flaws. Be strict with your words. Motivate the user by giving reality-check.",
        "welcome": "I am your Critic. Present your argument or concept, and I will find the weak points you need to fix."
    }
}

# --- UI LAYOUT ---
st.title("📚 AI Study Helper")
st.sidebar.title("Configuration")

selected_persona = st.sidebar.selectbox("Choose your guide:", list(PERSONAS.keys()))
st.sidebar.info(f"Current Persona: **{selected_persona}**")

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("What are we studying today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        try:
            # New SDK syntax for generating content
            response = client.models.generate_content(
                model="gemini-2.0-flash", # Note: gemini-3 is current, but ensure model name is exact
                config=genai.types.GenerateContentConfig(
                    system_instruction=PERSONAS[selected_persona]["system_prompt"]
                ),
                contents=prompt
            )
            
            response_text = response.text
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"Error: {e}")