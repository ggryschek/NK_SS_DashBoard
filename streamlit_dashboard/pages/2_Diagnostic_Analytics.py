import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Interactive Feature Exploration")


st.markdown("# Interactive Feature Exploration")


st.write(
    """This interactive demo allows users to select two features to explore their relationship visually.
    """
)

# Random data for demonstration
np.random.seed(42)
n_patients = 100
data = {
    "Age": np.random.randint(50, 90, n_patients), 
    "Gender": np.random.choice(['Male', 'Female'], size=n_patients), 
    "Risk_Score": np.random.normal(0.5, 0.1, n_patients), 
    "Blood_Pressure": np.random.randint(100, 180, n_patients)
}


df = pd.DataFrame(data)

# Select feature
st.sidebar.header("Choose Features")
feature_x = st.sidebar.selectbox("Choose feature for X-axis", options=df.columns)
feature_y = st.sidebar.selectbox("Choose feature for Y-axis", options=df.columns)


if feature_x == feature_y:
    st.error("Please choose two different features.")
else:
    st.subheader(f"Exploring relationship between {feature_x} and {feature_y}")

    
    fig, ax = plt.subplots()

    # Choose proper plot

    if df[feature_x].dtype == 'object' or df[feature_y].dtype == 'object':
        
        sns.boxplot(x=feature_x, y=feature_y, data=df, ax=ax)
        ax.set_title(f"{feature_y} by {feature_x}")
    else:
        
        sns.scatterplot(x=feature_x, y=feature_y, data=df, ax=ax)
        ax.set_title(f"{feature_x} vs {feature_y}")

    st.pyplot(fig)

# Show raw data
st.write("### Patient Demographic Data")
st.dataframe(df)