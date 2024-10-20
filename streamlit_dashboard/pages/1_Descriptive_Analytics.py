import streamlit as st
import pandas as pd
import plotly.express as px

# General page settings
st.set_page_config(page_title="Descriptive Analytics")
st.markdown("# Descriptive Analytics")
st.write(
    """This demo illustrates the distribution of patients based on demographic characteristics."""
)

# Load data
df = pd.read_csv("analysis/df_dataviz.csv")

# Overview
st.subheader("Overview")

## Patients vs. non-patients
total_patients = df[df['Diagnosis'] == True].shape[0]
total_non_patients = df[df['Diagnosis'] == False].shape[0]
st.write(f"**Total Patients:** {total_patients}")
st.write(f"**Total Non-Patients:** {total_non_patients}")

## Preliminary analysis of patients
### Feature selection and calculation
patient_data = df[df['Diagnosis'] == True]
avg_age = patient_data['Age'].mean()
avg_bmi = patient_data['BMI'].mean()
male_count = patient_data[patient_data['Gender'] == 'Male'].shape[0]
female_count = patient_data[patient_data['Gender'] == 'Female'].shape[0]

### Display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Age", f"{avg_age:.1f}")
col2.metric("Average BMI", f"{avg_bmi:.1f}")
col3.metric("Male Patients", male_count)
col4.metric("Female Patients", female_count)

# Customized analysis
st.subheader("Feature distribution")
st.write("Select a feature to view its distribution among patients.")

## Define selectable features
features = [
    'Gender', 'Ethnicity', 'ImpairmentLevel', 'DependencyLevel', 'WeightStatus', 'Confusion',
    'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks',
    'Forgetfulness', 'AgeRange', 'MemoryComplaints', 'BehavioralProblems',
    'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression', 'HeadInjury', 
    'Hypertension'
]

## Feature selection
selected_feature = st.selectbox("Select a feature:", features)

## Plot pie chart and histogram
if selected_feature:
    feature_data = patient_data[selected_feature].value_counts().reset_index()
    feature_data.columns = [selected_feature, 'Count']

    # Pie chart
    pie_chart = px.pie(
        feature_data, 
        names=selected_feature, 
        values='Count', 
        title=f"Distribution of {selected_feature} (Pie Chart)",
        labels={selected_feature: selected_feature, 'Count': 'Number'}
    )
    pie_chart.update_traces(textinfo='percent+label', hoverinfo='label+percent+value')

    # Histogram
    bar_chart = px.bar(
        feature_data, 
        x=selected_feature, 
        y='Count', 
        title=f"Distribution of {selected_feature} (Histogram)",
        text='Count',
        labels={selected_feature: selected_feature, 'Count': 'Number'}
    )
    bar_chart.update_traces(textposition='outside')

    st.plotly_chart(pie_chart)
    st.plotly_chart(bar_chart)
