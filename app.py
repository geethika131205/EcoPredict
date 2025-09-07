import streamlit as st
from utils import load_data, plot_city_area_heatmap

st.set_page_config(page_title="City Pollution Heatmap", layout="wide")
st.title("City Pollution Area Heatmap 🌆")

# Load data
df = load_data()

# Show dataset preview
if st.checkbox("Show Dataset Preview"):
    st.dataframe(df.head())

# User input
city_input = st.text_input("Enter City (e.g., Delhi)", "Delhi")
pollutant_input = st.selectbox("Select Pollutant", ['PM2.5','PM10','NO2','CO','O3','AQI'])

# Show heatmap button
if st.button("Show City Heatmap"):
    fig = plot_city_area_heatmap(df, city_input, pollutant_input)
    if fig:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("City data not found! Make sure the city exists in the dataset.")
