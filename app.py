import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

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
        ("cat",
         OneHotEncoder(handle_unknown="ignore"),
         categorical_cols)
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

st.title("🌾 Crop Yield Prediction")

st.write("Model trained successfully!")
st.dataframe(df.head())
