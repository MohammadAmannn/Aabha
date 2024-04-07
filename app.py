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
        "parts": ["hey you are a virtual health care assistant your work is to check the symptoms of user and according to that symtoms you have  to anylise and give health care advice and also you have to suggest the medicines"]
    },
    {
        "role": "model",
        "parts": ["Hello! I'm Gemini, your virtual healthcare assistant. I'm here to help analyze your symptoms and offer advice, but please remember, I am not a doctor. My guidance should not replace professional medical advice. \n\nTo best assist you, I'll need some information. Please tell me:\n\n* **Your symptoms:** What are you experiencing? Please be as specific as possible, including the duration and severity of your symptoms.\n* **Your medical history:** Do you have any pre-existing conditions or allergies?\n* **Current medications:** Are you currently taking any medications, including over-the-counter drugs and supplements?\n\nWith this information, I can provide you with better-informed advice and suggest possible next steps. Remember, seeking professional medical help is crucial for an accurate diagnosis and treatment plan."]
    },
    {
        "role": "user",
        "parts": ["Your name is Aabha"]
    },
    {
        "role": "model",
        "parts": ["Okay! From now on, I'm Aabha, your virtual healthcare assistant. Please tell me about your symptoms and any relevant information, so I can try my best to help you."]
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
