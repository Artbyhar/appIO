import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def fetch_data():
    #Ambil dari ThingSpeak
    url = "https://api.thingspeak.com/channels/2987739/feeds.json?api_key=O5GQEGC1N5FIEO1T&results=100"
    response = requests.get(url)
    data = response.json()
    feeds = data['feeds']
    df = pd.DataFrame(feeds)
    return df

df = fetch_data()

# Tampilkan data mentah
st.title("Data Monitoring IoT dari ThingSpeak")
st.write(df.head())

# Plot Field 1
st.subheader("Field 1 Chart")
st.line_chart(df["field1"].astype(float))

# Plot Field 2
st.subheader("Field 2 Chart")
st.line_chart(df["field2"].astype(float))
