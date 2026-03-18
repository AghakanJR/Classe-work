import streamlit as st
import pandas as pd


st.title("CSV File Viewer")

df = pd.read_csv("Datasets/trips_data_1000.csv")
st.write("Preview Uploaded Data:")
st.dataframe(df.head())