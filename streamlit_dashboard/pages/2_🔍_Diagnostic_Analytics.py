import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Diagnostic Analysis", 
    page_icon="🔍"
)

# Sidebar configuration
st.sidebar.image("assets/Neurologisk_Klinik_Logo.jpg")
st.sidebar.success("Powered by *Neurologisk Klinik*")

# Main content
st.title("Diagnostic Analysis", help="Find out association among features")

# Load data
df = pd.read_csv("analysis/df_dataviz.csv")

# Define Chi-Square Test function
def chi_square_test(df, var1, var2):
    contingency_table = pd.crosstab(df[var1], df[var2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return chi2, p

# Correlation of AD diagnosis and any other feature
st.header("Relationship with Diagnosis", divider="blue")

## Define feature by type
numerical_features = ['Age', 'BMI', 'MMSE', 'ADL', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'PhysicalActivity', 'AlcoholConsumption']
categorical_features = ['Gender', 'EducationLevel', 'Ethnicity', 'ImpairmentLevel', 'DependencyLevel', 'WeightStatus', 'Smoking', 'AgeRange', 'FamilyHistoryAlzheimers', 'Depression', 'Hypertension', 'Diabetes']

## Select feature
selected_feature = st.selectbox("Choose a variable to analyze its relationship with Diagnosis:", numerical_features + categorical_features)

## Analyse and plot base on feature type
### Numerical variable
if selected_feature in numerical_features:
    # Box plot
    fig, ax = plt.subplots()
    sns.boxplot(x='Diagnosis', y=selected_feature, data=df, ax=ax)
    st.pyplot(fig)
    
    # T-test
    group1 = df[df['Diagnosis'] == True][selected_feature]
    group2 = df[df['Diagnosis'] == False][selected_feature]
    t_stat, p_val = ttest_ind(group1, group2, nan_policy='omit')
    st.write(f"**T-Test between {selected_feature} and Diagnosis:** T-Statistic = {t_stat:.2f}, P-Value = {p_val:.4f}")

### Categorical variable
elif selected_feature in categorical_features:
    # Stacked bar chart
    contingency_table = pd.crosstab(df[selected_feature], df['Diagnosis'])
    fig, ax = plt.subplots()
    contingency_table.plot(kind='bar', stacked=True, ax=ax)
    st.pyplot(fig)
    
    # Chi-Square test
    chi2, p = chi_square_test(df, selected_feature, 'Diagnosis')
    st.write(f"**Chi-Square Test between {selected_feature} and Diagnosis:** Chi2 = {chi2:.2f}, P-Value = {p:.4f}")

# Correlation of features in patients
st.subheader("Relationships Between Variables (Patients Only)")

## Get patient data
patient_data = df[df['Diagnosis'] == True]

## Numerical variable correlation analysis
st.subheader("Numerical Variable Correlation Analysis")

num_var1 = st.selectbox("Choose first numerical variable:", numerical_features, key='num1')
num_var2 = st.selectbox("Choose second numerical variable:", numerical_features, key='num2')

if num_var1 and num_var2 and num_var1 != num_var2:
    correlation = patient_data[num_var1].corr(patient_data[num_var2], method='pearson')
    st.write(f"**Pearson Correlation Coefficient between {num_var1} and {num_var2} (Patients Only):** {correlation:.2f}")
    
    fig, ax = plt.subplots()
    sns.regplot(x=num_var1, y=num_var2, data=patient_data, ax=ax, scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
    st.pyplot(fig)

## Categorical variable correlation analysis
st.subheader("Categorical Variable Correlation Analysis")

cat_var1 = st.selectbox("Choose first categorical variable:", categorical_features, key='cat1')
cat_var2 = st.selectbox("Choose second categorical variable:", categorical_features, key='cat2')

if cat_var1 and cat_var2 and cat_var1 != cat_var2:
    chi2, p = chi_square_test(patient_data, cat_var1, cat_var2)
    st.write(f"**Chi-Square Test Results between {cat_var1} and {cat_var2} (Patients Only):** Chi2 = {chi2:.2f}, P-Value = {p:.4f}")
    
    contingency_table = pd.crosstab(patient_data[cat_var1], patient_data[cat_var2])
    fig, ax = plt.subplots()
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='coolwarm', ax=ax)
    st.pyplot(fig)

## Clustering
st.subheader("Clustering Analysis (KMeans on ADL and MMSE)")

### Normalization
cluster_data = patient_data[['MMSE', 'ADL']].dropna()
scaler = MinMaxScaler()
cluster_data[['MMSE', 'ADL']] = scaler.fit_transform(cluster_data[['MMSE', 'ADL']])

### KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_data['Cluster'] = kmeans.fit_predict(cluster_data[['MMSE', 'ADL']])

### Plot
fig = px.scatter(cluster_data, x='MMSE', y='ADL', color='Cluster', title='KMeans Clustering on ADL and MMSE (Patients Only)')
st.plotly_chart(fig)
