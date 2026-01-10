import streamlit as st
import pandas as pd
from textblob import TextBlob
from streamlit_agraph import agraph, Node, Edge, Config
import lyricsgenius

# --- 1. SETUP ---
# Used the token found in your API Clients screen
GENIUS_TOKEN = "p4dRJPCbMcyzsSAiDRkwWsRkFKpm_znsDXXTavyMUrCBfXPBZoeQCMLzfWbpeJeX"


@st.cache_data
def fetch_album_data(artist_name, album_name):
    """Fetches lyrics and calculates sentiment for an entire album."""
    try:
        genius = lyricsgenius.Genius(GENIUS_TOKEN, verbose=False, remove_section_headers=True)
        # Search for the album
        album = genius.search_album(album_name, artist_name)

        if not album:
            st.error("Album not found.")
            return pd.DataFrame(), None

        song_data = []
        # FIX: Directly access .tracks; each item in .tracks is usually a Song object
        for song in album.tracks:
            # Check if it has lyrics; if it's a tuple, get the first element
            actual_song = song[0] if isinstance(song, tuple) else song

            lyrics = actual_song.lyrics
            score = TextBlob(lyrics).sentiment.polarity

            song_data.append({
                "Title": actual_song.title,
                "Sentiment": score,
                "Preview": lyrics[:150] + "..."
            })

        return pd.DataFrame(song_data), album.cover_art_url
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame(), None


# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="Lore & Lyric Analyzer", layout="wide")
st.title("🎼 Twenty One Pilots: Lore & Sentiment Dashboard")

# User Selection
with st.sidebar:
    st.header("Search Settings")
    target_album = st.selectbox("Select Album", ["Trench", "Vessel", "Blurryface", "Clancy"])
    fetch_btn = st.button("Fetch & Analyze Data")

if fetch_btn:
    with st.spinner("Scraping lyrics and analyzing themes..."):
        df, cover = fetch_album_data("Twenty One Pilots", target_album)
        st.session_state['df'] = df
        st.session_state['cover'] = cover

# --- 3. DATA VISUALIZATION ---
if 'df' in st.session_state and not st.session_state['df'].empty:
    df = st.session_state['df']
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Emotional Arc: {target_album}")
        st.image(st.session_state['cover'], width=250)
        st.line_chart(df.set_index("Title")["Sentiment"])
        st.caption("Gold (Positive) | Red (Anxious/Struggle)")

    with col2:
        st.subheader("Archetypal Lore Map")
        avg_sent = df["Sentiment"].mean()
        # Logic: High sentiment = Hope (Gold), Low = Anxiety (Red)
        node_color = "#FFD700" if avg_sent > 0.05 else "#FF4B4B"

        nodes = [
            Node(id="Album", label=target_album, size=40, color=node_color),
            Node(id="Clancy", label="Clancy (Protagonist)", size=25, color="#C0C0C0"),
            Node(id="Nico", label="Nico (Bishops)", size=25, color="#000000"),
            Node(id="Archetype", label="Biblical Parallel", size=20, color="#4682B4")
        ]
        edges = [
            Edge(source="Album", target="Clancy"),
            Edge(source="Clancy", target="Archetype", label="The Exile"),
            Edge(source="Nico", target="Album", label="Influence")
        ]

        config = Config(width=500, height=450, directed=True, physics=True)
        agraph(nodes=nodes, edges=edges, config=config)

    st.write("### Track-by-Track Sentiment Breakdown")
    st.dataframe(df)