import streamlit as st
import pandas as pd
from textblob import TextBlob
from streamlit_agraph import agraph, Node, Edge, Config
import lyricsgenius

# --- 1. SETUP ---
# Integrated from your Genius API settings
GENIUS_TOKEN = "p4dRJPCbMcyzsSAiDRkwWsRkFKpm_znsDXXTavyMUrCBfXPBZoeQCMLzfWbpeJeX"


@st.cache_data
def fetch_album_data(artist_name, album_name):
    """Fetches lyrics and calculates sentiment for an entire album."""
    try:
        genius = lyricsgenius.Genius(GENIUS_TOKEN, verbose=False, remove_section_headers=True)
        album = genius.search_album(album_name, artist_name)

        if not album:
            st.error("Album not found.")
            return pd.DataFrame(), None

        song_data = []
        for track in album.tracks:
            # FIX: Ensure we are accessing the song object correctly
            # Depending on version, this might be track.song or just track
            song = track.song if hasattr(track, 'song') else track

            # Additional check to skip if lyrics aren't found (e.g., instrumentals)
            if hasattr(song, 'lyrics') and song.lyrics:
                lyrics = song.lyrics
                score = TextBlob(lyrics).sentiment.polarity
                song_data.append({
                    "Title": song.title,
                    "Sentiment": score,
                    "Preview": lyrics[:150].replace('\n', ' ') + "..."
                })

        return pd.DataFrame(song_data), album.cover_art_url
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame(), None


# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="Lore & Lyric Analyzer", layout="wide")
st.title("🎼 Twenty One Pilots: Lore & Sentiment Dashboard")

# User Selection in Sidebar
with st.sidebar:
    st.header("Search Settings")
    target_album = st.selectbox("Select Album", ["Trench", "Vessel", "Blurryface", "Clancy", "Scaled and Icy"])
    fetch_btn = st.button("Fetch & Analyze Data")

# Execution Logic
if fetch_btn:
    with st.spinner(f"Accessing Genius API for {target_album}..."):
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
        st.caption("Sentiment Score: Higher is 'Hopeful', Lower is 'Anxious/Struggle'")

    with col2:
        st.subheader("Archetypal Lore Map")
        avg_sent = df["Sentiment"].mean()
        # Visual cue: Map color to sentiment (Gold for Hope, Red for Anxiety)
        node_color = "#FFD700" if avg_sent > 0.05 else "#FF4B4B"

        nodes = [
            Node(id="Album", label=target_album, size=40, color=node_color),
            Node(id="Clancy", label="Clancy (The Exile)", size=25, color="#C0C0C0"),
            Node(id="Nico", label="Nico (The Accuser)", size=25, color="#000000"),
            Node(id="Archetype", label="Biblical Parallel", size=20, color="#4682B4")
        ]
        edges = [
            Edge(source="Album", target="Clancy"),
            Edge(source="Clancy", target="Archetype", label="Spiritual Journey"),
            Edge(source="Nico", target="Album", label="Conflict")
        ]

        config = Config(width=500, height=450, directed=True, physics=True)
        agraph(nodes=nodes, edges=edges, config=config)

    st.divider()
    st.write("### Track Analysis Table")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Click 'Fetch & Analyze Data' to load the dashboard.")