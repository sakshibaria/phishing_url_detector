# app.py

import streamlit as st
import joblib
import pandas as pd
from Utils import extract_features

# Load model
model = joblib.load("model.pkl")

st.title("🔐 Phishing URL Detector")

url = st.text_input("Enter a URL to check:")

if st.button("Check"):
    features = pd.DataFrame([extract_features(url)])
    prediction = model.predict(features)[0]
    if prediction:
        st.error("🚨 Phishing Detected!")
    else:
        st.success("✅ Legitimate URL")
