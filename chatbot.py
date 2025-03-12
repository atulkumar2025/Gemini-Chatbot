import os
import google.generativeai as genai
import streamlit as st

# Configure API key
API_KEY = "Your API Key"
genai.configure(api_key=API_KEY)

# Function to get response from Gemini Pro
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-pro-exp")  # Use latest available model
    response = model.generate_content(prompt)
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="💬", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E;
            color: white;
        }
        .stChatMessage {
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user {
            background-color: #0078D4;
            color: white;
            text-align: left;
        }
        .assistant {
            background-color: #2E2E2E;
            color: white;
            text-align: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Chat UI
st.title("💬 Gemini Pro Chatbot")
st.subheader("🚀 Powered by Google's Gemini AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role_class = "user" if message["role"] == "user" else "assistant"
    st.markdown(f'<div class="stChatMessage {role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# User Input
user_input = st.text_input("Type your message here...", key="user_input")

if st.button("Send"):
    if user_input:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.markdown(f'<div class="stChatMessage user">{user_input}</div>', unsafe_allow_html=True)

        # Show typing indicator
        with st.spinner("Thinking..."):
            response = get_gemini_response(user_input)

        # Append assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(f'<div class="stChatMessage assistant">{response}</div>', unsafe_allow_html=True)