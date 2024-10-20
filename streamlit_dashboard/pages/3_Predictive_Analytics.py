import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# Load model & scaler
best_model = joblib.load("analysis/best_model.pkl")
scaler = joblib.load("analysis/scaler.pkl")

# General page settings
st.set_page_config(page_title="Predictive & Prescriptive Analytics")
st.markdown("# Predictive & Prescriptive Analytics")
st.write(
    """This page allows users to input patient information and get predictive insights, 
    along with prescriptive analytics using SHAP visualizations for model interpretability."""
)

# Input
st.subheader("Patient Information Input")

# Default input
name = st.text_input("Patient Name", value="Maria")
adl = st.number_input("ADL Score", min_value=0.0, max_value=10.0, value=3.0)
mmse = st.number_input("MMSE Score", min_value=0, max_value=30, value=20)

# Convert input to DataFrame
input_data = pd.DataFrame({'ADL': [adl], 'MMSE': [mmse]})

# Standardize input data using the loaded scaler
input_data_scaled = scaler.transform(input_data) 

# Prediction section
if st.button("Predict Diagnosis"):
    prediction = best_model.predict(input_data_scaled)
    result = name + " is at risk of Alzheimer's disease" if prediction[0] else name + " is  unlikely to have Alzheimer's disease"
    st.write(f"**Patient Name:** {name}")
    st.write(f"**ADL Score:** {adl}")
    st.write(f"**MMSE Score:** {mmse}")
    st.write(f"**Prediction Result:** {result}")

# SHAP explanation section
st.subheader("Prescriptive Analytics using SHAP")