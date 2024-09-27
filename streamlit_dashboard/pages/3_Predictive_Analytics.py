import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

st.set_page_config(page_title="Predictive Analytics")


st.markdown("# Predictive Analytics")


st.write(
    """This predictive analytics demo explores how demographic characteristics can be used to predict health outcomes.
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

# Hot-coding
df['Gender_Code'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Show raw data
st.write("### Patient Demographic Data", df)

### Q1: Predicting Risk Score based on Age and Gender ###
st.subheader("1. Predicting Risk Score based on Age and Gender")


X = df[['Age', 'Gender_Code']]
y = df['Risk_Score']

# Divide training and tes set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict by linear regression
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Prediction and Mean squared error
y_pred = reg_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Visualization
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, label="Predictions", color="b")
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label="Perfect Prediction")
ax.set_xlabel("True Risk Score")
ax.set_ylabel("Predicted Risk Score")
ax.set_title("True vs Predicted Risk Score (MSE: {:.2f})".format(mse))
ax.legend()
st.pyplot(fig)

### Q2: Predicting Blood Pressure based on Age？ ###
st.subheader("2. Predicting Blood Pressure based on Age")

# Predict by linear regression
X_bp = df[['Age']]
y_bp = df['Blood_Pressure']

X_train_bp, X_test_bp, y_train_bp, y_test_bp = train_test_split(X_bp, y_bp, test_size=0.2, random_state=42)
bp_model = LinearRegression()
bp_model.fit(X_train_bp, y_train_bp)

# Prediction and Mean squared error
y_pred_bp = bp_model.predict(X_test_bp)
mse_bp = mean_squared_error(y_test_bp, y_pred_bp)

# Visualization
fig, ax = plt.subplots()
ax.scatter(y_test_bp, y_pred_bp, label="Predictions", color="g")
ax.plot([y_test_bp.min(), y_test_bp.max()], [y_test_bp.min(), y_test_bp.max()], 'r--', lw=2, label="Perfect Prediction")
ax.set_xlabel("True Blood Pressure")
ax.set_ylabel("Predicted Blood Pressure")
ax.set_title("True vs Predicted Blood Pressure (MSE: {:.2f})".format(mse_bp))
ax.legend()
st.pyplot(fig)

### Q3: Predicting High Risk Status using Age, Gender, and Blood Pressure(Classification) ###
st.subheader("3. Predicting High Risk Status using Age, Gender, and Blood Pressure")

# Define high risk
df['High_Risk'] = (df['Risk_Score'] > 0.6).astype(int)

# Divide training and test set
X_class = df[['Age', 'Gender_Code', 'Blood_Pressure']]
y_class = df['High_Risk']

X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

# DT
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_class, y_train_class)

# Prediction and accuracy
y_pred_class = clf.predict(X_test_class)
accuracy = accuracy_score(y_test_class, y_pred_class)

# Visualization
fig, ax = plt.subplots()
sns.barplot(x=['True Negative', 'True Positive'], y=[(y_test_class == y_pred_class).sum(), (y_test_class != y_pred_class).sum()], ax=ax)
ax.set_title(f"High Risk Prediction Accuracy: {accuracy * 100:.2f}%")
st.pyplot(fig)
