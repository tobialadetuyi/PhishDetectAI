import streamlit as st
import joblib

# Load model
model = joblib.load('model/phishing_classifier.pkl')

# App title
st.title("📡 PhishDetectAI")
st.subheader("Detect phishing or scam messages using AI")

# Text input
user_input = st.text_area("📝 Paste your email or message content here:")

# Prediction
if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == 1:
            st.error("🚨 This message is likely *Phishing*!")
        else:
            st.success("✅ This message is likely *Safe*.")
