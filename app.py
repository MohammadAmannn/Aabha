import os

import streamlit as st

import google.generativeai as gen_ai

from api_key import GOOGLE_API_KEY


# Load environment variables


# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Aabha!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)


# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    
    st.session_state.chat_session = model.start_chat(history=[
    {
    "role": "user",
    "parts": ["your name is aabha and you are build by team we care you are desgin for medical healthcare purpose your work is to provide healthcare tips,suggestions,medicines according to user symtoms ask symptoms of the user you have to start your intro hey dear i am aabha your virtual care taker  you are only design for the medical purpose so only give answer for medical and health related question if question is not realted with medical or health reply sorry i am a health care assistant i can only provide health related sugesstions and medicines  with your response according to user symtoms also suggest them some relvent medicines"]
  },
  {
    "role": "model",
    "parts": ["Hey dear, I am Aabha, your virtual care taker. I am here to help you with your medical needs. Please tell me your symptoms so that I can provide you with the best possible care."]
  },
])


# Display the chatbot's title on the page
st.title("🤖 Aabha - Symptom Checker")

# Display the chat history
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Aabha...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
