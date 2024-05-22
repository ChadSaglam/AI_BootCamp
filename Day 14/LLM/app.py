from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

api_key = os.getenv('GOOGLE_API_KEY')
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Error: GOOGLE_API_KEY not found in environment variables")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(soru):
    response = chat.send_message(soru, stream=True)
    return response

st.header('Gemini Chat')
input_text = st.text_input('Input', key='input')
submit_button = st.button('Soru Sor')

if submit_button:
    response = get_response(input_text)
    st.header('Cevap')

    for chunk in response:
        st.write(chunk.text)