import streamlit as st
from transformers import pipeline
import torch

@st.cache_resource
def load_model():
    # Check if CUDA is available and use it if possible
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection", device=device)

try:
    classifier = load_model()
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")
    st.stop()

def classify_text(text):
    try:
        result = classifier(text, max_length=512, truncation=True)[0]
        if result['score'] > 0.9:
            return "NOT SPAM"
        else:
            return "SPAM"
    except Exception as e:
        st.error(f"Error during classification: {str(e)}")
        return "CLASSIFICATION ERROR"

st.title("Multilingual Spam Classifier")
message = st.text_area("Enter your message (supports multiple languages):")

if st.button("Classify"):
    if message:
        result = classify_text(message)
        if result == "SPAM":
            st.error("This message is classified as SPAM.")
        elif result == "NOT SPAM":
            st.success("This message is classified as NOT SPAM.")
        else:
            st.warning("Unable to classify the message.")
    else:
        st.warning("Please enter a message to classify.")