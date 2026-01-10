import streamlit as st
import pandas as pd
from textblob import TextBlob
from streamlit_agraph import agraph, Node, Edge, Config
import lyricsgenius

# --- 1. CONFIGURATION ---
# Using your Client Access Token from the Genius API page
GENIUS_TOKEN = "p4dRJPCbMcyzsSAiDRkwWsRkFKpm_znsDXXTavyMUrCBfXPBZoeQCMLzfWbpeJeX"

# Initialize Session State variables if they don't exist
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'cover' not in st.session_state:
    st.session_state['cover'] = None


@st.cache_data(show_spinner=False)
def fetch_album_data(artist_name, album_name):
    """Fetches lyrics and calculates sentiment for an entire album."""
    try:
        genius = lyricsgenius.Genius(GENIUS_TOKEN, verbose=False, remove_section_headers=True)
        # Timeout and retries to prevent connection hangs
        genius.timeout = 15
        genius.retries = 3

        album = genius.search_album(album_name, artist_name)

        if not album:
            return None, None

        song_data = []
        for track in album.tracks:
            # Handle potential variation in object structure
            song = track.song if hasattr(track, 'song') else track

            # Ensure it's a song object with lyrics
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
        st.error(f"Genius API Error: {e}")
        return None, None


# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="Lore & Lyric Analyzer", layout="wide")
st.title("🎼 Twenty One Pilots: Lore & Sentiment Dashboard")

with st.sidebar:
    st.header("Search Settings")
    target_album = st.selectbox("Select Album", ["Trench", "Vessel", "Blurryface", "Clancy", "Scaled and Icy"])

    # Logic: When button is pressed, update session state immediately
    if st.button("Fetch & Analyze Data"):
        with st.spinner(f"Connecting to Genius for {target_album}..."):
            df_result, cover_result = fetch_album_data("Twenty One Pilots", target_album)
            if df_result is not None:
                st.session_state['df'] = df_result
                st.session_state['cover'] = cover_result
            else:
                st.error("Failed to retrieve data. Check your API token or internet connection.")

# --- 3. DATA VISUALIZATION ---
# Check if session state actually contains data
if st.session_state['df'] is not None:
    df = st.session_state['df']
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Emotional Arc")
        if st.session_state['cover']:
            st.image(st.session_state['cover'], width=250)
        st.line_chart(df.set_index("Title")["Sentiment"])
        st.caption("Sentiment: 1.0 (Hope) | -1.0 (Anxiety)")

    with col2:
        st.subheader("Archetypal Lore Map")
        avg_sent = df["Sentiment"].mean()
        node_color = "#FFD700" if avg_sent > 0.05 else "#FF4B4B"

        nodes = [
            Node(id="Album", label=target_album, size=40, color=node_color),
            Node(id="Clancy", label="Clancy", size=25, color="#C0C0C0"),
            Node(id="Archetype", label="Biblical Parallel", size=20, color="#4682B4")
        ]
        edges = [
            Edge(source="Album", target="Clancy"),
            Edge(source="Clancy", target="Archetype", label="Journey")
        ]

        config = Config(width=500, height=450, directed=True, physics=True)
        agraph(nodes=nodes, edges=edges, config=config)

    st.divider()
    st.write("### Track Breakdown")
    st.dataframe(df, use_container_width=True)
else:
    # This shows ONLY if no data has been successfully fetched yet
    st.warning("No data loaded. Please select an album and click the 'Fetch' button in the sidebar.")