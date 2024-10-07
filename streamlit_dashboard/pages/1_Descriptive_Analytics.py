import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from streamlit_tags import st_tags

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

# Get the column names (variables) as tags to display
available_vars = df.columns.tolist()

# Create a set to keep track of selected variables
selected_vars = set()

# Display variables as small tags (buttons) that can be clicked to select or deselect
st.markdown("### Available Variables (Click to Select or Deselect):")
for var in available_vars:
    # Use st.button for each variable to act as a tag
    if st.button(var, key=var):
        if var in selected_vars:
            selected_vars.remove(var)  # Deselect if already selected
        else:
            selected_vars.add(var)  # Select if not already selected

# Display selected variables in the top box (mimics the display of selected tags)
st.markdown("### Selected Variables:")
if selected_vars:
    st.text(", ".join(selected_vars))  # Display selected variables as a comma-separated string
else:
    st.text("No variables selected yet.")  # Display when no variables are selected

# Function to render histograms for the selected variables
def render_histogram(selected_vars):
    if selected_vars:
        for var in selected_vars:
            chart = alt.Chart(df).mark_bar().encode(
                alt.X(var, bin=True),
                y='count()'
            ).properties(
                width=600,
                height=400,
                title=f"Distribution of {var}"
            )
            st.altair_chart(chart)

# Generate histograms for the selected variables
render_histogram(selected_vars)

# Show raw data
st.write("### Patient Demographic Data", df)