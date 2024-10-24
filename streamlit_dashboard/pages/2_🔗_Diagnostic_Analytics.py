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
    page_icon="🔗"
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
    significance = "Significant" if p < 0.05 else "Not Significant"
    return chi2, p, significance

# Correlation of AD diagnosis and any other feature
st.header("Relationship of Selected Feature with Diagnosis", divider="blue")
st.write("The **graph type may change** due to different feaure types.")

## Define feature by type
numerical_features = ['Age', 'BMI', 'MMSE', 'ADL', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'PhysicalActivity', 'AlcoholConsumption']
categorical_features = ['Gender', 'EducationLevel', 'Ethnicity', 'ImpairmentLevel', 'DependencyLevel', 'WeightStatus', 'Smoking', 'AgeRange', 'FamilyHistoryAlzheimers', 'Depression', 'Hypertension', 'Diabetes']

## Select feature
selected_feature = st.selectbox("Choose a feature to analyze its relationship with Diagnosis:", numerical_features + categorical_features)

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
    significance_numerical = "Significant" if p_val < 0.05 else "Not Significant"
    st.subheader(f"T-Test between {selected_feature} and Diagnosis:")
    st.write(f"T-Statistic = {t_stat:.2f}, P-Value = {p_val:.4f} (**{significance_numerical}**)")
    st.write("P-Value is the key result. A significant result indicates a significant difference in the distribution of the selected feature between AD and non-AD patients, suggesting an association with AD.")

### Categorical variable
elif selected_feature in categorical_features:
    # Stacked bar chart
    contingency_table = pd.crosstab(df[selected_feature], df['Diagnosis'])
    fig, ax = plt.subplots()
    contingency_table.plot(kind='bar', stacked=True, ax=ax)
    st.pyplot(fig)
    
    # Chi-Square test
    chi2, p, significance = chi_square_test(df, selected_feature, 'Diagnosis')
    st.subheader(f"Chi-Square Test between {selected_feature} and Diagnosis:")
    st.write(f"Chi2 = {chi2:.2f}, P-Value = {p:.4f} (**{significance}**)")
    st.write("P-Value is the key result. A significant result indicates a significant difference in the distribution of the selected feature between AD and non-AD patients, suggesting an association with AD.")

    # Show heatmap for all categorical variables when a categorical variable is selected
    st.subheader("P-Value Heatmap for Categorical Variables", help="Categorical variablesare usually represent discrete groups or categories, such as gender, or education level.")
    heatmap_data = pd.DataFrame(index=categorical_features, columns=['P-Value'])

    for var in categorical_features:
        _, p_val, _ = chi_square_test(df, var, 'Diagnosis')
        heatmap_data.at[var, 'P-Value'] = p_val

    fig, ax = plt.subplots(figsize=(8, len(categorical_features) * 0.5))
    sns.heatmap(heatmap_data.astype(float), annot=True, cmap='coolwarm', ax=ax, cbar_kws={'label': 'P-Value'})
    ax.set_title("P-Value Heatmap for Diagnosis Relationship")
    st.pyplot(fig)         

# Correlation of features in patients
st.header("Relationships Between Variables of AD Patients", divider="blue")

## Get patient data
patient_data = df[df['Diagnosis'] == True]

## Numerical variable correlation analysis
st.subheader("Numerical Variable Correlation Analysis", help="Numerical variable usually represent measurable quantities, such as age, or blood pressure.")
st.write("Find out corelation of two numerical variable")
num_var1 = st.selectbox("Choose first numerical variable:", numerical_features, key='num1')
num_var2 = st.selectbox("Choose second numerical variable:", numerical_features, key='num2')

if num_var1 and num_var2 and num_var1 != num_var2:
    correlation = patient_data[num_var1].corr(patient_data[num_var2], method='pearson')
    st.subheader(f"**Pearson Correlation Coefficient between {num_var1} and {num_var2} in AD Patients:**")
    st.write(f"{correlation:.2f}")
    st.markdown("""
    The **Pearson Correlation Coefficient** measures the strength and direction of a linear relationship between two variables. It ranges from -1 to 1:
    - **1**: Strong positive correlation (as one variable increases, the other also increases).
    - **-1**: Strong negative correlation (as one variable increases, the other decreases).
    - **0**: No linear correlation (no consistent pattern between the variables).
    """)
    
    fig, ax = plt.subplots()
    sns.regplot(x=num_var1, y=num_var2, data=patient_data, ax=ax, scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
    st.pyplot(fig)

## Categorical variable correlation analysis
st.subheader("Categorical Variable Correlation Analysis", help="Categorical variablesare usually represent discrete groups or categories, such as gender, or education level.")

cat_var1 = st.selectbox("Choose first categorical variable:", categorical_features, key='cat1')
cat_var2 = st.selectbox("Choose second categorical variable:", categorical_features, key='cat2')

if cat_var1 and cat_var2 and cat_var1 != cat_var2:
    chi2, p, significance = chi_square_test(patient_data, cat_var1, cat_var2)
    st.subheader(f"**Chi-Square Test Results between {cat_var1} and {cat_var2} (Patients Only):**")
    st.write(f"Chi2 = {chi2:.2f}, P-Value = {p:.4f} (**{significance}**)")
    st.write("P-Value is the key result. A significant result indicates a significant difference in the distribution of the selected feature between AD and non-AD patients, suggesting an association with AD.")

    
    contingency_table = pd.crosstab(patient_data[cat_var1], patient_data[cat_var2])
    fig, ax = plt.subplots()
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Clustering
st.header("Clustering Analysis (KMeans on ADL and MMSE)", divider="blue")

## Normalization
cluster_data = patient_data[['MMSE', 'ADL']].dropna()
scaler = MinMaxScaler()
cluster_data[['MMSE', 'ADL']] = scaler.fit_transform(cluster_data[['MMSE', 'ADL']])

## KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_data['Cluster'] = kmeans.fit_predict(cluster_data[['MMSE', 'ADL']])

## Plot
cluster_data['Cluster'] = cluster_data['Cluster'].astype(str)
fig = px.scatter(
    cluster_data, 
    x='MMSE', 
    y='ADL', 
    color='Cluster', 
    title='KMeans Clustering on ADL and MMSE in AD Patients',
    color_discrete_sequence=['#0038A8', '#005CE6', '#89b7f7']
)
st.plotly_chart(fig)