import streamlit as st
import pandas as pd

df = pd.read_csv("data_season.csv")

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Total Crops", df["Crops"].nunique())
col3.metric("Locations", df["Location"].nunique())
col4.metric("Average Yield", int(df["yeilds"].mean()))
