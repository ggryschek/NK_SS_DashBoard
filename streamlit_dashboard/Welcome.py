import streamlit as st

# Page configuration
st.set_page_config(
    page_title = "Alzheimer's Disease Exploration Dashboard",
    page_icon = "🧠"
)

# Sidebar configuration
st.sidebar.image("assets/Neurologisk_Klinik_Logo.jpg")
st.sidebar.success("Powered by *Neurologisk Klinik*")

# Main content
st.title("Welcome to Alzheimer's Disease Exploration Dashboard")
st.header("Introduction", divider="blue")
st.write(
    """
    **End Users**: The dashboard is designed for **specialists (neurologists)** and other **healthcare professionals** at Neurologisk Klinik (NK).
    
    **Objectives**: This platform aims to provide valuable insights into Alzheimer's Disease (AD) by utilizing data from NK to facilitate **early detection, risk prevention, and personalized care**.

    """
)

st.header("Analytics Tab Description", divider="blue")
st.write(
    """

    **Descriptive Analytics** provides a comprehensive **overview** of patient demographics and clinical data.

    **Diagnostic Analytics** focuses on exploring the **association** between individual features and diagnosis outcomes, as well as uncovering the **internal associations** between features within AD patients.

    **Predictive Analytics** leverages machine learning models to **predict** the risk of developing AD in individuals. Additionally, it includes **prescriptive analytics** to interpret the results for single instance.

    """
)