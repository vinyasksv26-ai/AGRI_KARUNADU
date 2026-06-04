import streamlit as st
import pandas as pd

df = pd.read_csv("data_season.csv")

st.title("📋 Dataset Explorer")

st.dataframe(df)

st.download_button(
    "Download Dataset",
    df.to_csv(index=False),
    "data_season.csv",
    "text/csv"
)
