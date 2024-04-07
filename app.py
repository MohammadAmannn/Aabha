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

    {
    "role": "user",
    "parts": ["do not proivde any other suggestion only proive medical realted suggestion suggest some medicne and give health tips"]
  },
   {
    "role": "model",
    "parts": ["**Medical Advice**\n\n**Symptoms:** Please provide me with your symptoms so I can offer specific medical advice. Including the duration and severity of your symptoms will help me give you more accurate information.\n\n**Medications:**\n\n* **Over-the-counter:** If your symptoms are mild, over-the-counter medications may provide relief. For example, acetaminophen or ibuprofen can help reduce pain and fever. For allergies, antihistamines such as loratadine or cetirizine can be effective.\n* **Prescription:** If your symptoms are more severe or persistent, prescription medications may be necessary. Your doctor can determine the best course of treatment based on your specific condition.\n\n**Health Tips:**\n\n* **Rest:** Getting enough rest can help your body heal and fight off infections. Aim for 7-9 hours of sleep each night.\n* **Hydration:** Staying hydrated is essential for overall health. Drink plenty of fluids, especially water, throughout the day.\n* **Healthy diet:** Eating a healthy diet can boost your immune system and support your overall well-being. Focus on consuming fruits, vegetables, and whole grains.\n* **Exercise:** Regular exercise can help improve your health and reduce the risk of chronic diseases. Aim for at least 30 minutes of moderate-intensity exercise most days of the week.\n* **Stress management:** Stress can have a negative impact on your health. Find healthy ways to manage stress, such as exercise, yoga, or meditation.\n\n**Important Note:** It's important to consult a medical professional for an accurate diagnosis and treatment plan. My advice is not intended to replace professional medical care."]
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
