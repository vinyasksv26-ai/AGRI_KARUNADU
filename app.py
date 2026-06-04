import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("🌾 Crop Yield Prediction System")

year = st.number_input("Year", 2000, 2050, 2024)

location = st.text_input("Location")

area = st.number_input("Area")

rainfall = st.number_input("Rainfall")

temperature = st.number_input("Temperature")

soil = st.text_input("Soil Type")

irrigation = st.text_input("Irrigation")

humidity = st.number_input("Humidity")

crop = st.text_input("Crop")

price = st.number_input("Price")

season = st.text_input("Season")

if st.button("Predict Yield"):

    input_df = pd.DataFrame({
        "Year":[year],
        "Location":[location],
        "Area":[area],
        "Rainfall":[rainfall],
        "Temperature":[temperature],
        "Soil type":[soil],
        "Irrigation":[irrigation],
        "Humidity":[humidity],
        "Crops":[crop],
        "price":[price],
        "Season":[season]
    })

    prediction = model.predict(input_df)

    st.success(
        f"Predicted Yield = {prediction[0]:.2f}"
    )
