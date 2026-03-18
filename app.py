import streamlit as st
import pandas as pd

st.title("CSV File Viewer")

df = pd.read_csv("Datasets/trips_data_1000.csv")


col1, col2, col3, col4 = st.columns(4)

col1.metric("Number of Trips", df.shape[0])
col2.metric("Unique Customers", df["customer_email"].nunique())
with col3 : 
    total_distance = df["distance"].sum() / 1000
    st.metric("Total Distance", value=f"{total_distance:.2f} K")
with col4:
    average_revenue = df["revenue"].mean()
    st.metric("Average Revenue Per Trip", value = f"{average_revenue:.2f} €")

st.write("Preview Uploaded Data:")
st.dataframe(df.head())