import streamlit as st
import pandas as pd

st.title("🌾 AGRI KARUNADU")

# Load Dataset
df = pd.read_csv("data_season.csv")

# Show columns
st.subheader("Dataset Columns")
st.write(df.columns.tolist())

# Display dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Check if target column exists
if "yeilds" not in df.columns:
    st.error(
        "Column 'yeilds' not found in dataset. Please check the column name shown above."
    )
    st.stop()

# ML Part
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

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
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_cols
        )
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
