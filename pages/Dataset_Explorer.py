import streamlit as st
import pandas as pd

st.title("📋 Dataset Explorer")

df = pd.read_csv("data_season.csv")

st.dataframe(df)

st.download_button(
    "Download Dataset",
    df.to_csv(index=False),
    file_name="data_season.csv",
    mime="text/csv"
)
