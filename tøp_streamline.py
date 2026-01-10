#%%
#%%
import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import squarify # pip install squarify
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px # Requires: pip install plotly
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
df = pd.read_excel(file_path)

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('vader_lexicon')

# 2. Text Preprocessing
stop_words = set(stopwords.words('english'))

def clean_lyrics(text):
    # Lowercase and remove non-alphabetic characters
    words = str(text).lower().split()
    clean_words = [w for w in words if w.isalpha() and w not in stop_words]
    return " ".join(clean_words)

df['Clean_Lyrics'] = df['Lyrics'].apply(clean_lyrics)

# 3. Sentiment Analysis
sia = SentimentIntensityAnalyzer()
df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# 4. Group by Album for Analysis
album_sentiment = df.groupby('album_name')['Sentiment_Score'].mean().sort_values()
print("Average Sentiment by Album:\n", album_sentiment)

# Create a new DataFrame containing only songs from the album "Breach"
df_breach = df[df["album_name"] == "Breach"][["album_name", "track_name", "Lyrics"]]
df_clancy = df[df["album_name"] == "Clancy"][["album_name", "track_name", "Lyrics"]]
df_sai = df[df["album_name"] == "Scaled And Icy"][["album_name", "track_name", "Lyrics"]]
df_trench = df[df["album_name"] == "Trench"][["album_name", "track_name", "Lyrics"]]
df_blurryface = df[df["album_name"] == "Blurryface"][["album_name", "track_name", "Lyrics"]]
df_vessel = df[df["album_name"] == "Vessel"][["album_name", "track_name", "Lyrics"]]
df_self_titled = df[df["album_name"] == "Twenty One Pilots"][["album_name", "track_name", "Lyrics"]]
# To see the first few rows of your filtered data:
print(df_breach.head())

# 1. Define the list of albums you want to analyze
target_albums = [
    "Breach", "Clancy", "Scaled And Icy", "Trench",
    "Blurryface", "Vessel", "Twenty One Pilots"
]

# 2. Filter the main DataFrame for these albums and specific columns
df_combined = df[df["album_name"].isin(target_albums)][["album_name", "track_name", "Lyrics"]]

#%%
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