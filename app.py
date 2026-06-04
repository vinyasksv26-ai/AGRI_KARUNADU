import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AGRI KARUNADU",
    page_icon="🌾",
    layout="wide"
)

# Sidebar Logo
st.sidebar.image("assets/logo.png", width=150)
st.sidebar.title("🌾 AGRI KARUNADU")
st.sidebar.success("AI Powered Crop Yield Prediction System")

# Main Logo
st.image("assets/logo.png", width=200)

# Title
st.title("🌾 AGRI KARUNADU")
st.subheader("AI Powered Crop Yield Prediction System")

st.markdown("---")

# Welcome Section
st.markdown("""
## Welcome to AGRI KARUNADU

This application helps farmers and researchers predict crop yield using Machine Learning.

### Features

📊 **Dashboard**
- Total Records
- Total Crops
- Total Locations
- Average Yield

📈 **Analytics**
- Yield by Crop
- Yield by Season
- Rainfall Analysis
- Temperature Analysis

🤖 **Crop Yield Prediction**
- Location Selection
- Crop Selection
- Soil Type Selection
- Rainfall Input
- Temperature Input
- Yield Prediction

📋 **Dataset Explorer**
- View Dataset
- Search Records
- Download Dataset

### Navigation

Use the **sidebar menu** to access:

- Dashboard
- Analytics
- Prediction
- Dataset Explorer
""")

st.markdown("---")

# Footer
st.markdown(
    """
    <div style='text-align:center'>
        <h4>🌾 AGRI KARUNADU</h4>
        <p>Crop Yield Prediction System using Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)
