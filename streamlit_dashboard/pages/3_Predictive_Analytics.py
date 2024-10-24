import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
    result = name + " is at risk of Alzheimer's disease" if prediction[0] else name + " is not at risk of Alzheimer's disease"
    st.write(f"**Prediction Result:** {result}")

# SHAP explanation section
st.subheader("Prescriptive Analytics using SHAP")

## Load data
df_ml = pd.read_csv("analysis/df_ml.csv")

## Select feature and target
x = df_ml[['ADL','MMSE']]
y = df_ml['Diagnosis']

## Splite train and test set
RANDOM_SEED = 42
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=RANDOM_SEED)

## Normalization
x_train_scaled = pd.DataFrame(scaler.transform(x_train), columns=x_train.columns)
x_test_scaled = pd.DataFrame(scaler.transform(x_test), columns=x_train.columns)

## Define explainer
explainer = shap.TreeExplainer(best_model)

shap_values = explainer(x_test_scaled)

## Visualize SHAP values
if st.button("Show SHAP Analysis"):
    st.write("SHAP Waterfall Plot:")
    shap_values_class1 = shap_values[..., 1]
    
    
    fig, ax = plt.subplots()
    shap.plots.waterfall(shap_values_class1[0], show=False)
    st.pyplot(fig)
    plt.close(fig)

# Feature importance
st.subheader("* Feature importance analysis")

st.image("assets/Permutation_Feature_Importances.png")

st.write("Describe feature importance")
