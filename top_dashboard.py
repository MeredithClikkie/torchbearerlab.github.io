import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

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


# 1. Update the target albums to match your sidebar exactly
target_albums = [
    "Vessel", "Blurryface", "Trench", "Scaled And Icy", "Clancy", "Twenty One Pilots"
]

# 2. Include 'Sentiment_Score' in your combined DataFrame
df_combined = df[df["album_name"].isin(target_albums)][["album_name", "track_name", "Lyrics", "Sentiment_Score"]]

st.title("|-/ The Clique Dashboard")

# 3. Ensure these options match the 'album_name' values in your Excel file
album_choice = st.sidebar.selectbox("Select an Era", target_albums)

# Filter based on the sidebar selection
filtered_df = df_combined[df_combined['album_name'] == album_choice].reset_index()

# Now 'Sentiment_Score' will be available for px.scatter
fig = px.scatter(
    filtered_df,
    x=filtered_df.index,
    y='Sentiment_Score',
    hover_data=['track_name'],
    labels={'x': 'Track Number'}
)
st.plotly_chart(fig)





