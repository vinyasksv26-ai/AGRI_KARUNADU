import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_season.csv")

st.title("📈 Analytics")

crop_yield = df.groupby("Crops")["yeilds"].mean().reset_index()

fig = px.bar(
    crop_yield,
    x="Crops",
    y="yeilds",
    title="Average Yield by Crop"
)

st.plotly_chart(fig, use_container_width=True)
