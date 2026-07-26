import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("company_financials.csv")

# Title
st.title("Financial Dashboard")

# Latest values
latest = df.iloc[-1]

st.subheader("Latest KPIs")
c1, c2, c3 = st.columns(3)

c1.metric("Sales", latest["Sales"])
c2.metric("Net Profit", latest["Net_Profit"])
c3.metric("OPM %", latest["OPM_Percent"])

# Sales Chart
st.subheader("Sales Trend")
fig, ax = plt.subplots()
ax.plot(df["Period"], df["Sales"], marker="o")
plt.xticks(rotation=45)
st.pyplot(fig)

# Net Profit Chart
st.subheader("Net Profit Trend")
fig, ax = plt.subplots()
ax.plot(df["Period"], df["Net_Profit"], marker="o")
plt.xticks(rotation=45)
st.pyplot(fig)

# OPM Chart
st.subheader("OPM %")
fig, ax = plt.subplots()
ax.bar(df["Period"], df["OPM_Percent"])
plt.xticks(rotation=45)
st.pyplot(fig)

# Data Table
st.subheader("Financial Data")
st.dataframe(df)