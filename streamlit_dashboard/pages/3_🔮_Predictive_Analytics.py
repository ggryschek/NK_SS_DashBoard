import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Page configuration
st.set_page_config(
    page_title="Predictive & Prescriptive Analytics",
    page_icon="🔮"
)


# Sidebar configuration
st.sidebar.image("assets/Neurologisk_Klinik_Logo.jpg")
st.sidebar.success("Powered by *Neurologisk Klinik*")

# Main content
st.title("Predictive Analytics", help="Predict AD risk for certain patient.")
st.write(
    """
    You may input patient information and get predictive insights, 
    along with prescriptive analytics using SHAP visualizations for model interpretability.
    """
)
# Input
st.subheader("Patient Information Input", divider="blue")

# Load model & scaler
best_model = joblib.load("analysis/best_model.pkl")
scaler = joblib.load("analysis/scaler.pkl")

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
    result = name + " is **at risk** of Alzheimer's disease" if prediction[0] else name + " is **not at risk** of Alzheimer's disease"
    st.write(f"**Prediction Result:** {result}")

# SHAP explanation section
st.subheader("Prescriptive Analytics using SHAP", divider="blue")

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
    st.markdown("""
    SHAP single instance analysis explains how a machine learning model makes a specific prediction for a single data point. 
    It shows the contribution of each feature to the prediction, helping to understand the final result.

    In this example, **E[f(X)] = 0.5** is the baseline value, which represents the model’s average output when no specific feature values are considered.

    **ADL = 0.68** means that the normalized value of ADL for the selected instance is 0.68. The blue bar indicates a negative contribution, valued at **-0.23**, which lowers the prediction. 

    The instance’s **MMSE** normalized value is **0.467**, and the red bar indicates a positive contribution, valued at **+0.13**, which raises the prediction. 

    The final result is **0.401**.
    """)

# Feature importance
st.subheader("Feature importance analysis", divider="blue")

st.image("assets/Permutation_Feature_Importances.png")

st.markdown(
    """
Conducting feature importance analysis after selecting the best model enhances the model’s interpretability by highlighting the roles of MMSE and ADL in making predictions. 
This process also allows for optimizing the final model, leading to improved performance, faster loading times, and fewer input requirements, ultimately enhancing the user experience.
""")
