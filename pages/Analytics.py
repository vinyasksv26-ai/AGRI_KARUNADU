import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics")

df = pd.read_csv("data_season.csv")

crop_yield = df.groupby("Crops")["yeilds"].mean().reset_index()

fig1 = px.bar(
    crop_yield,
    x="Crops",
    y="yeilds",
    title="Average Yield by Crop"
)

st.plotly_chart(fig1, use_container_width=True)

season_yield = df.groupby("Season")["yeilds"].mean().reset_index()

fig2 = px.pie(
    season_yield,
    names="Season",
    values="yeilds",
    title="Yield by Season"
)

st.plotly_chart(fig2, use_container_width=True)
