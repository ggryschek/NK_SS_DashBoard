import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Descriptive Analytics")

st.markdown("# Descriptive Analytics")

st.sidebar.header("Descriptive Analytics")

st.write(
    """This demo illustrates the distribution of patients based on demographic characteristics.
"""
)

# Random data for demonstration
np.random.seed(42) 
n_patients = 100

data = {
    "Age": np.random.randint(50, 90, n_patients),
    "Gender": np.random.choice(['Male', 'Female'], size=n_patients),
    "Risk_Score": np.random.normal(0.5, 0.1, n_patients)
}

df = pd.DataFrame(data)

# Select feature for x axis
x_axis = st.selectbox(
    "Select a feature that you care", 
    options=["Age", "Gender"],  
)

# Distribution calculation
if x_axis == "Age":
    age_distribution = df['Age'].value_counts().sort_index()
    st.bar_chart(age_distribution)
elif x_axis == "Gender":
    gender_distribution = df['Gender'].value_counts()
    st.bar_chart(gender_distribution)

# Show raw data
st.write("### Patient Demographic Data", df)