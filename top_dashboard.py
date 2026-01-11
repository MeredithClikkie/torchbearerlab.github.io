import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

# --- 1. SETUP & DATA LOADING ---
st.set_page_config(page_title="TØP Analytics", layout="wide")


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

    # Apply preprocessing
    df['Clean_Lyrics'] = df['Lyrics'].apply(clean_lyrics)
    sia = SentimentIntensityAnalyzer()
    df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    return df, stop_words


df, stop_words = load_data()

# Filter for specific albums
target_albums = ["Twenty One Pilots", "Vessel", "Blurryface", "Trench", "Scaled And Icy", "Clancy"]
df_combined = df[df["album_name"].isin(target_albums)]

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("|-/ Navigation")
page = st.sidebar.radio("Go to:", ["Era Evolution", "Lyric Explorer"])

# --- PAGE 1: ERA EVOLUTION ---
if page == "Era Evolution":
    st.title("Discography Sentiment Evolution")

    # BOX PLOT: Era vs Era
    st.subheader("Sentiment Distribution by Album")
    fig_box = px.box(
        df_combined,
        x="album_name",
        y="Sentiment_Score",
        color="album_name",
        points="all",  # Shows individual song dots over the box
        title="Are the 'Happy' sounding albums actually happy?",
        template="plotly_dark",
        category_orders={"album_name": target_albums}  # Keeps them in chronological order
    )
    st.plotly_chart(fig_box, use_container_width=True)

    st.divider()

    # WORD CLOUD SECTION
    album_choice = st.selectbox("Select an Era for a Deep Dive", target_albums)
    filtered_df = df_combined[df_combined['album_name'] == album_choice]

    col1, col2 = st.columns(2)

    with col1:
        # Scatter Plot for the specific album
        fig_scatter = px.scatter(
            filtered_df, x=filtered_df.index, y='Sentiment_Score',
            hover_name='track_name', template="plotly_dark",
            title=f"{album_choice}: Song by Song Sentiment"
        )
        st.plotly_chart(fig_scatter)

    with col2:
        # Color Map for WordCloud
        era_colors = {"Vessel": "Blues", "Blurryface": "Reds", "Trench": "YlOrBr",
                      "Scaled And Icy": "PuBuGn", "Clancy": "Oranges", "Twenty One Pilots": "Greys"}

        album_text = " ".join(filtered_df['Clean_Lyrics'])
        wc = WordCloud(background_color='black', colormap=era_colors.get(album_choice, 'Reds')).generate(album_text)

        fig_wc, ax = plt.subplots()
        ax.imshow(wc)
        ax.axis('off')
        st.pyplot(fig_wc)

# --- PAGE 2: LYRIC EXPLORER ---
else:
    st.title("🔍 Lyric & Mood Explorer")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Filters")
        search_query = st.text_input("Search for a keyword (e.g., 'Fire', 'Car', 'East')")

        score_range = st.slider(
            "Filter by Sentiment Score",
            min_value=-1.0, max_value=1.0, value=(-1.0, 1.0), step=0.1
        )
        st.caption("Lower = Sadder/Darker | Higher = More Positive")

    # Apply Filters
    search_results = df_combined[
        (df_combined['Lyrics'].str.contains(search_query, case=False, na=False)) &
        (df_combined['Sentiment_Score'] >= score_range[0]) &
        (df_combined['Sentiment_Score'] <= score_range[1])
        ]

    with col2:
        st.subheader(f"Results ({len(search_results)} songs found)")
        if not search_results.empty:
            # Display results in a nice table
            st.dataframe(
                search_results[['track_name', 'album_name', 'Sentiment_Score']],
                use_container_width=True,
                hide_index=True
            )

            # Show the lyrics of the first result or a selected one
            selected_song = st.selectbox("Select a song to read lyrics:", search_results['track_name'].tolist())
            lyrics_to_show = search_results[search_results['track_name'] == selected_song]['Lyrics'].values[0]
            st.text_area("Lyrics:", lyrics_to_show, height=300)
        else:
            st.warning("No songs match those filters. Try broadening your search!")