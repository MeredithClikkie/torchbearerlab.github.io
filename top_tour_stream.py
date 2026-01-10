import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# 1. Load and Prepare Data
file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/top_geo.csv'
df= pd.read_csv(file_path)
df['ShowDate'] = pd.to_datetime(df['ShowDate'])
df = df.sort_values('ShowDate') # Essential for chronological distance

# 2. Sidebar Filter
st.sidebar.header("Tour Filters")
album = st.sidebar.selectbox("Select Album Era", df['Associated Albums'].unique())
filtered_df = df[df['Associated Albums'] == album].copy()

# 3. Calculate Distance for the Selected Era
def calculate_total_distance(data):
    total_miles = 0
    # We need at least two shows to calculate a distance
    if len(data) > 1:
        points = data[['latitude', 'longitude']].values
        for i in range(len(points) - 1):
            # Calculate distance between show i and show i+1
            start = points[i]
            end = points[i+1]
            total_miles += geodesic(start, end).miles
    return total_miles

total_dist = calculate_total_distance(filtered_df)

# 4. Display Metrics and Map
st.title(f"Tour Analysis: {album}")

# Show the distance as a highlight metric
st.metric(label="Total Era Travel Distance", value=f"{total_dist:,.2f} Miles")

st.subheader("Show Locations")
st.map(filtered_df[['latitude', 'longitude']])

st.subheader("Era Show Logs")
st.write(filtered_df)