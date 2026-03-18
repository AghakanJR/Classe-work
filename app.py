import streamlit as st
import pandas as pd


st.title("CSV File Uploader")

uploaded_file = st.file_uploader ("Upload a CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data:")
    st.dataframe(df.head())