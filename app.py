import streamlit as st
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

st.title("🌾 AGRI KARUNADU - Crop Yield Prediction")

# Load dataset
df = pd.read_csv("data_season.csv")

# Train model
X = df.drop("yeilds", axis=1)
y = df["yeilds"]

categorical_cols = [
    "Location",
    "Soil type",
    "Irrigation",
    "Crops",
    "Season"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

model.fit(X, y)

st.success("Model trained successfully!")

st.header("Enter Crop Details")

year = st.number_input("Year", value=2024)

location = st.selectbox(
    "Location",
    sorted(df["Location"].unique())
)

area = st.number_input("Area", value=1000.0)

rainfall = st.number_input("Rainfall", value=1000.0)

temperature = st.number_input("Temperature", value=25.0)

soil = st.selectbox(
    "Soil Type",
    sorted(df["Soil type"].unique())
)

irrigation = st.selectbox(
    "Irrigation",
    sorted(df["Irrigation"].unique())
)

humidity = st.number_input("Humidity", value=60.0)

crop = st.selectbox(
    "Crop",
    sorted(df["Crops"].unique())
)

price = st.number_input("Price", value=1000.0)

season = st.selectbox(
    "Season",
    sorted(df["Season"].unique())
)

if st.button("Predict Yield"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Location": [location],
        "Area": [area],
        "Rainfall": [rainfall],
        "Temperature": [temperature],
        "Soil type": [soil],
        "Irrigation": [irrigation],
        "Humidity": [humidity],
        "Crops": [crop],
        "price": [price],
        "Season": [season]
    })

    prediction = model.predict(input_data)

    st.success(
        f"🌾 Predicted Yield: {prediction[0]:.2f}"
    )
