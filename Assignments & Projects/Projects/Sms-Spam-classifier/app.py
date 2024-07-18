import streamlit as st
import joblib

# Load the model
model = joblib.load('sms_spam_model.joblib')

# Streamlit app
st.title("SMS Spam Classifier")
message = st.text_area("Enter your message:")

if st.button("Classify"):
  prediction = model.predict([message])
  if prediction[0] == 1:
    st.error("This message is classified as SPAM.")
  else:
    st.success("This message is classified as NOT SPAM.")