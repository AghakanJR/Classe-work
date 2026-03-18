import streamlit as st
import pandas as pd

st.title("Import a CSV File and visualize with Streamlit Charts")

df = pd.read_csv("Datasets/trips_data_1000.csv")
st.write("Preview Uploaded Data:")
st.dataframe(df.head())

car_brand = st.sidebar.selectbox("Select the car brand", df["car_brand"].unique())
df = df[df["car_brand"] == car_brand]

st.subheader("Customers by City")
country_counts = df["customer_city"].value_counts()
st.write(country_counts)
st.bar_chart(country_counts)

st.subheader("Trips Over time",)
df["Trips Date"] = pd.to_datetime(df["pickup_time"]).dt.date
Trips_counts= df["Trips date"].value_counts()
st.write(Trips_counts)
st.line_chart(Trips_counts)