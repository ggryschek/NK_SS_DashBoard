import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# Load model
best_model = joblib.load("analysis/best_model.pkl")

# General page settings
st.set_page_config(page_title="Predictive & Prescriptive Analytics")
st.markdown("# Predictive & Prescriptive Analytics")
st.write(
    """This page allows users to input patient information and get predictive insights, 
    along with prescriptive analytics using SHAP visualizations for model interpretability."""
)

# Input
st.subheader("Patient Information Input")

## Default input
age = st.number_input("Age", min_value=0, max_value=120, value=65)
ethnicity = st.selectbox("Ethnicity", ["Caucasian", "Black", "Asian", "Other"], index=2)
mmse = st.number_input("MMSE Score", min_value=0, max_value=30, value=20)
adl = st.number_input("ADL Score", min_value=0.0, max_value=10.0, value=3.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=21.3)
cholesterol = st.number_input("Cholesterol (mmol/L)", min_value=0.0, max_value=10.0, value=6.2)
blood_pressure = st.text_input("Blood Pressure (e.g., 150/95)", value="150/95")

## Handle BP
bp_systolic, bp_diastolic = map(int, blood_pressure.split("/"))

## Convert input format
def prepare_input(age, ethnicity, mmse, adl, bmi, cholesterol, bp_systolic, bp_diastolic):
    ethnicity_mapping = {
        "Caucasian": [1, 0, 0, 0],
        "Black": [0, 1, 0, 0],
        "Asian": [0, 0, 1, 0],
        "Other": [0, 0, 0, 1]
    }
    input_data = [
        age, bmi, mmse, adl, cholesterol, bp_systolic, bp_diastolic
    ] + ethnicity_mapping.get(ethnicity, [0, 0, 0, 1])
    return np.array(input_data).reshape(1, -1)

## Load input
input_features = prepare_input(age, ethnicity, mmse, adl, bmi, cholesterol, bp_systolic, bp_diastolic)

## Prediction
if st.button("Predict Diagnosis"):
    prediction = best_model.predict(input_features)
    result = "Alzheimer's disease likely" if prediction[0] else "Alzheimer's disease unlikely"
    st.write(f"**Prediction Result:** {result}")

# Add SHAP
st.subheader("Prescriptive Analytics using SHAP")

## Initiate SHAP model
explainer = shap.TreeExplainer(best_model)  # Adjust based on actual model type
shap_values = explainer.shap_values(input_features)

## SHAP visualization
st.write("### Single-instance Explanation")
shap.initjs()
fig, ax = plt.subplots()
shap.force_plot(explainer.expected_value, shap_values[0], input_features, matplotlib=True, show=False)
st.pyplot(fig)

## Visualizaition of SHAP on test set
if st.button("Show Global Feature Importance (Test Set)"):
    
    X_test = pd.read_csv("analysis/df_ml.csv").drop("Diagnosis", axis=1)  # Replace with actual test data
    shap_values_global = explainer.shap_values(X_test)
    
    st.write("### Global Feature Importance")
    shap.summary_plot(shap_values_global, X_test)
    st.pyplot()
