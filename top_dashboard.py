import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

# --- 1. SETUP & DATA LOADING ---
st.set_page_config(page_title="TØP Era Evolution", layout="wide")


@st.cache_data
def load_data():
    file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
    df = pd.read_excel(file_path)

    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    stop_words = set(stopwords.words('english'))

    def clean_lyrics(text):
        words = str(text).lower().split()
        clean_words = [w for w in words if w.isalpha() and w not in stop_words]
        return " ".join(clean_words)

    df['Clean_Lyrics'] = df['Lyrics'].apply(clean_lyrics)
    sia = SentimentIntensityAnalyzer()
    df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    return df, stop_words


df, stop_words = load_data()

# --- ADDED "Breach" TO THE TARGET LIST ---
target_albums = ["Twenty One Pilots", "Vessel", "Blurryface", "Trench", "Scaled And Icy", "Clancy", "Breach"]
df_combined = df[df["album_name"].isin(target_albums)]

# --- 2. HEADER ---
st.title("|-/ The Clique Analytics Dashboard")

with st.expander("ℹ️ How Sentiment Scoring Works"):
    st.write("""
   We use the **VADER** model to analyze word choice in lyrics. 
    - **Scores near +1.0** indicate themes of hope, joy, or resolution.
    - **Scores near -1.0** indicate themes of struggle, anxiety, or doubt.
    - **Labels on the chart** are automatically chosen based on the most extreme emotional points (the peaks and valleys) of the album.
    """)

# --- 3. DISCOGRAPHY OVERVIEW ---
st.subheader("Discography Sentiment Distribution")
fig_box = px.box(
    df_combined,
    x="album_name",
    y="Sentiment_Score",
    color="album_name",
    points="all",
    template="plotly_dark",
    category_orders={"album_name": target_albums},
    labels={"album_name": "Album Name", "Sentiment_Score": "Sentiment Score"}
)
fig_box.update_layout(showlegend=False)
st.plotly_chart(fig_box, use_container_width=True)

st.divider()

# --- 4. DEEP DIVE: EMOTIONAL JOURNEY ---
album_choice = st.selectbox("Select an Era for a Deep Dive", target_albums)
filtered_df = df_combined[df_combined['album_name'] == album_choice].copy().reset_index(drop=True)

# LABELING LOGIC
max_val = filtered_df['Sentiment_Score'].max()
min_val = filtered_df['Sentiment_Score'].min()
avg_val = filtered_df['Sentiment_Score'].mean()


def get_label(row):
    if row['Sentiment_Score'] == max_val or row['Sentiment_Score'] == min_val:
        return row['track_name']
    if abs(row['Sentiment_Score'] - avg_val) > 0.6:
        return row['track_name']
    return ""


filtered_df['Display_Label'] = filtered_df.apply(get_label, axis=1)

col_chart, col_cloud = st.columns([2, 1])

with col_chart:
    track_nums = list(range(1, len(filtered_df) + 1))

    fig_journey = px.scatter(
        filtered_df,
        x=track_nums,
        y='Sentiment_Score',
        text='Display_Label',
        hover_name='track_name',
        template="plotly_dark",
        title=f"The Emotional Journey of {album_choice}"
    )

    fig_journey.update_traces(
        mode='lines+markers+text',
        textposition='top center',
        marker=dict(size=12, line=dict(width=1, color='white')),
        line=dict(width=2, color='gray')
    )

    fig_journey.update_layout(
        hovermode="x unified",
        xaxis_title="Track Number",
        yaxis_title="Sentiment Score",
        yaxis=dict(range=[min_val - 0.2, max_val + 0.2])
    )

    st.plotly_chart(fig_journey, use_container_width=True)

with col_cloud:
    st.subheader("Era Themes")

    # --- ADDED "Breach" COLOR THEME HERE ---
    era_colors = {
        "Vessel": "Blues",
        "Blurryface": "Reds",
        "Trench": "YlOrBr",
        "Breach": "GnBu",  # Green-Blue theme for Breach
        "Scaled And Icy": "PuBuGn",
        "Clancy": "Oranges",
        "Twenty One Pilots": "Greys"
    }

    album_text = " ".join(filtered_df['Clean_Lyrics'])
    if album_text:
        wc = WordCloud(
            width=400, height=400,
            background_color='black',
            colormap=era_colors.get(album_choice, "Reds")
        ).generate(album_text)

        fig_wc, ax = plt.subplots()
        ax.imshow(wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_wc)
    else:
        st.info("Not enough data for word cloud.")

# --- 5. SONG SPOTLIGHT (Individual Song View) ---
st.divider()
st.subheader(f"🔍 Song Spotlight: {album_choice}")

# Selection for individual songs
song_list = filtered_df['track_name'].tolist()
selected_song = st.selectbox("Pick a song to see details:", song_list)

# Get data for the selected song
song_data = filtered_df[filtered_df['track_name'] == selected_song].iloc[0]

sm1, sm2, sm3 = st.columns([1, 1, 2])

with sm1:
    st.metric("Sentiment Score", f"{song_data['Sentiment_Score']:.3f}")

with sm2:
    status = "Positive" if song_data['Sentiment_Score'] > 0.05 else "Negative" if song_data[
                                                                                      'Sentiment_Score'] < -0.05 else "Neutral"
    st.write(f"**Tone:** {status}")
    st.write(f"**Track #:** {song_list.index(selected_song) + 1}")

with sm3:
    # Display the lyrics in a scrollable box
    st.text_area(f"Lyrics for {selected_song}", song_data['Lyrics'], height=250)

# --- 5. SUMMARY METRICS ---
st.divider()
st.subheader(f"Snapshot: {album_choice}")
m1, m2, m3 = st.columns(3)

if not filtered_df.empty:
    happiest_song = filtered_df.loc[filtered_df['Sentiment_Score'].idxmax(), 'track_name']
    saddest_song = filtered_df.loc[filtered_df['Sentiment_Score'].idxmin(), 'track_name']

    m1.metric("Era Average Sentiment", f"{avg_val:.2f}")
    m2.metric("Happiest Track", happiest_song)
    m3.metric("Saddest Track", saddest_song)

    # --- 6. LYRIC COMPARISON ---
    st.subheader("Contrast: Happiest vs. Saddest Lyrics")
    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"**☀️ {happiest_song}**")
        happy_lyrics = filtered_df[filtered_df['track_name'] == happiest_song]['Lyrics'].values[0]
        st.text_area("Top Sentiment Lyrics", happy_lyrics, height=200, key="happy")

    with c2:
        st.markdown(f"**🌙 {saddest_song}**")
        sad_lyrics = filtered_df[filtered_df['track_name'] == saddest_song]['Lyrics'].values[0]
        st.text_area("Bottom Sentiment Lyrics", sad_lyrics, height=200, key="sad")