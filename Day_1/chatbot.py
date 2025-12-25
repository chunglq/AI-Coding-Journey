import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatSession:
    def __init__(self, system_prompt="You are a helpful assistant.", model="gpt-4o-mini"):
        self.messages = [{"role": "system", "content": system_prompt}]
        self.model = model

    def send_message(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
        )
        assistant_message = response.choices[0].message.content.strip()
        self.messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message

# Initialize session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = ChatSession()
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})