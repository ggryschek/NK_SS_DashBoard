import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Descriptive Analytics", 
    page_icon="📈"
)

# Sidebar configuration
st.sidebar.image("assets/Neurologisk_Klinik_Logo.jpg")
st.sidebar.success("Powered by *Neurologisk Klinik*")

# Main content
st.title("Descriptive Analytics", help="Learn about feature distribution")

# Load data
df = pd.read_csv("analysis/df_dataviz.csv")

# Overview
st.header("Overview",divider="blue")

## Patients vs. non-patients
total_patients = df[df['Diagnosis'] == True].shape[0]
total_non_patients = df[df['Diagnosis'] == False].shape[0]
st.subheader("Non-AD and AD Patients Distribution", divider=False)
st.write(f"**Total Non-AD Patients:** {total_non_patients}")
st.write(f"**Total AD Patients:** {total_patients}")


## Preliminary analysis of patients
### Feature selection and calculation
patient_data = df[df['Diagnosis'] == True]
avg_age = patient_data['Age'].mean()
avg_MMSE = patient_data['MMSE'].mean()
avg_ADL = patient_data['ADL'].mean()
male_count = patient_data[patient_data['Gender'] == 'Male'].shape[0]
female_count = patient_data[patient_data['Gender'] == 'Female'].shape[0]

### Display
st.subheader("Basic AD Patient Statistics", divider=False)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("**Average Age**", f"{avg_age:.1f}")
col2.metric("**Average MMSE**", f"{avg_MMSE:.1f}")
col3.metric("**Average ADL**", f"{avg_ADL:.1f}")
col4.metric("**Male Patients**", male_count)
col5.metric("**Female Patients**", female_count)

# Customized analysis
st.header("Feature distribution", divider="blue")
st.write("Find out how selected feature distributed among AD patients.")

## Define selectable features
features = [
    'Gender', 'Ethnicity', 'ImpairmentLevel', 'DependencyLevel', 'WeightStatus', 'Confusion',
    'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks',
    'Forgetfulness', 'AgeRange', 'MemoryComplaints', 'BehavioralProblems',
    'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression', 'HeadInjury', 
    'Hypertension', 'EducationLevel', 'Smoking', 
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
