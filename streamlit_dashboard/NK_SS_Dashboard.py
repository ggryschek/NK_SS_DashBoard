import streamlit as st

st.set_page_config(
    page_title = "NK_SS_Dashboard",
    page_icon = "🧠", 
)

st.write("# Welcome to Alzheimer's Battlefield")

st.sidebar.success(" Select a Rabbit Hole to Jump in")

st.markdown(
    """
  Here at **Alzheimer's Battlefield**, you will explore unrevealed mystery to help your patients fight against **Alzheimer's Disease**
"""
)

col1, col2 = st.columns([1, 1])

with col1:
    st.image("./assets/Neurologisk_Klinik_Logo.jpg", caption="Neurologisk Klinik", use_column_width=True)

with col2:
    st.image("./assets/Synapse_Solutions_Logo.jpg", caption="Synapse Solutions", use_column_width=True)
