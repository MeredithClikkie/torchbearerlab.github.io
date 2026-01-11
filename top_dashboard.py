import streamlit as st
import plotly.express as px

st.title("|-/ The Clique Dashboard")

# Sidebar for filters
album = st.sidebar.selectbox("Select an Era", ["Vessel", "Blurryface", "Trench", "SAI", "Clancy"])

# Load your data

st.header(f"Insights for the {album} Era")

# Example: Sentiment Chart
fig = px.scatter(df_combined[df_combined['album_name'] == album], x='', y='sentiment_score', text='track_name')
st.plotly_chart(fig)
st.plotly_chart(fig)

st.write("Would you like me to help you write the code to perform sentiment analysis on your lyrics specifically?")


