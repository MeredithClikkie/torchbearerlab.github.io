import streamlit as st
import pandas as pd

# Basic setup to display your map
st.title("Tour History Dashboard")
file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/top_geo.csv'
df= pd.read_csv(file_path)

# Filter by Album
album = st.sidebar.selectbox("Select Album Era", df['Associated Albums'].unique())
filtered_df = df[df['Associated Albums'] == album]

# Display Map
st.map(filtered_df[['latitude', 'longitude']]) # Simple interactive map

# Show raw data for the era
st.write(f"Shows during the {album} era:", filtered_df)