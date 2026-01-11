import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
import zlib  # For repetition scoring

# --- 1. SETUP & DATA LOADING ---
st.set_page_config(page_title="TØP Advanced Analytics", layout="wide")


@st.cache_data
def load_data():
    file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
    df = pd.read_excel(file_path)

    # Preprocessing Helpers
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    stop_words = set(stopwords.words('english'))
    stop_words.update(['yeah', 'oh', 'ooh', 'woah', 'la', 'na', 'chorus', 'im', 'dont'])

    def clean_lyrics(text):
        words = str(text).lower().split()
        return " ".join([w for w in words if w.isalpha() and w not in stop_words])

    def calculate_diversity(text):
        words = str(text).lower().split()
        return len(set(words)) / len(words) if words else 0

    def calculate_repetition(text):
        if not text or len(str(text)) < 10: return 0
        encoded = str(text).lower().encode('utf-8')
        return 1 - (len(zlib.compress(encoded)) / len(encoded))



    # 2. Apply it to the main dataframe BEFORE you filter for 'df_combined'
    df['Lexical_Diversity'] = df['Lyrics'].apply(calculate_diversity)


    # Apply all metrics
    df['Clean_Lyrics'] = df['Lyrics'].apply(clean_lyrics)
    df['Repetition_Score'] = df['Lyrics'].apply(calculate_repetition)

    sia = SentimentIntensityAnalyzer()
    df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

    return df, stop_words


df, stop_words = load_data()

# Chronology Mapping
# 3. Define Chronology
release_dates = {
    "Twenty One Pilots": 2009,
    "Vessel": 2013,
    "Blurryface": 2015,
    "Trench": 2018,
    "Breach": 2020,
    "Scaled And Icy": 2021,
    "Clancy": 2024
}

# 4. Filter and Create df_combined
# This now contains the new metric columns automatically
target_albums = [a for a in release_dates.keys() if a in df['album_name'].unique()]
df_combined = df[df["album_name"].isin(target_albums)].copy()

# 5. Add the release year for sorting/plotting
df_combined['release_year'] = df_combined['album_name'].map(release_dates)

# --- 2. THE TABS ---
st.title("|-/ The Advanced Clique Dashboard")
tab1, tab2, tab3 = st.tabs(["Era Evolution", "Technical Metrics", "Lyric Explorer"])

# --- TAB 1: ERA EVOLUTION (Thematic & Sentiment) ---
with tab1:
    st.subheader("Sentiment & Thematic Distribution")
    fig_box = px.box(df_combined, x="album_name", y="Sentiment_Score", color="album_name",
                     points="all", template="plotly_dark", category_orders={"album_name": target_albums})
    st.plotly_chart(fig_box, use_container_width=True)

# --- TAB 2: TECHNICAL METRICS (The New Parts) ---
with tab2:
    st.header("Technical Complexity Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Lexical Diversity (Vocabulary Richness)")
        div_avg = df_combined.groupby('album_name')['Lexical_Diversity'].mean().reindex(target_albums).reset_index()
        fig_div = px.bar(div_avg, x='Lexical_Diversity', y='album_name', orientation='h',
                         color='Lexical_Diversity', color_continuous_scale='Reds', template='plotly_dark')
        st.plotly_chart(fig_div, use_container_width=True)
        st.info("Higher score = More unique words (Less repetitive lyrics).")

    with col2:
        st.subheader("Repetition vs. Formulaic Patterns")
        rep_avg = df_combined.groupby('album_name')['Repetition_Score'].mean().reindex(target_albums).reset_index()
        fig_rep = px.line(rep_avg, x='album_name', y='Repetition_Score', markers=True, template='plotly_dark')
        st.plotly_chart(fig_rep, use_container_width=True)
        st.info("Measures how 'compressible' the lyrics are. High scores = repetitive hooks/choruses.")

# --- TAB 3: LYRIC EXPLORER (The Search & Detailed View) ---
with tab3:
    # (Insert your previous Spotlight & Lyric Comparison code here)
    st.subheader("Search & Spotlight")
    # ... previous code ...


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

# --- 5. Advanced Lexical Theology Section ---
# 2. Advanced Lexical Theology Section
# In this section, we use your Lexical Diversity and Word Counts to track "Theological Density."
# A. The "Lament" Correlation
# Theology often distinguishes between Praise (Positive Sentiment) and Lament (Negative Sentiment).
# The Logic: In the Book of Psalms, 70% of the chapters are Laments.
# The Code Integration:
# Categorize songs by Lament vs. Praise
df_combined['Theological_Category'] = df_combined.apply(
    lambda x: 'Lament' if x['Sentiment_Score'] < -0.3 else ('Praise/Hope' if x['Sentiment_Score'] > 0.3 else 'Reflective'),
    axis=1
)

# Categorize songs by Word vs. Spirit
# B. The "Word" vs. "Spirit" Balance
# We can track specific lexicons to see which era is more "Physical" (the struggle of the flesh) versus "Metaphysical" (the battle of the mind/spirit).
# Define Lexicons
flesh_lexicon = ['skin', 'bones', 'blood', 'body', 'flesh', 'hands', 'feet']
spirit_lexicon = ['soul', 'mind', 'ghost', 'spirit', 'dream', 'think', 'believe']

def count_themes(text, lexicon):
    return sum(1 for word in str(text).lower().split() if word in lexicon)

df_combined['Flesh_Count'] = df_combined['Lyrics'].apply(lambda x: count_themes(x, flesh_lexicon))
df_combined['Spirit_Count'] = df_combined['Lyrics'].apply(lambda x: count_themes(x, spirit_lexicon))

# 3. Integrated Streamlit Code: The "Theology Tab"
# Add this as a new tab to your existing dashboard.
# It combines the Lexical Diversity from your notebook with the Theology Map.

# Define the tab variables here
# --- 2. THE TABS ---
st.title("|-/ The Ultimate Discography Report")

# Define the tab variables here
tab_theology, tab_tech, tab_export = st.tabs(["Theological Map", "Technical Metrics", "Export Report"])

# Now use the EXACT same names in the 'with' blocks
with tab_theology:
    st.header("Scriptural Connections")
    # ... (rest of the theology code)

with tab_tech:
    st.header("Advanced Technical Metrics")
    # ... (rest of the technical metrics code)

with tab_export:
    st.header("Generate PDF Findings")
    # ... (rest of the export code)

with tab_theology:
    st.header("|-/ Theological Deep Dive")

    # 1. Metric: Lexical Theology (Density of Faith Words)
    faith_words = ['god', 'faith', 'believe', 'pray', 'soul', 'spirit', 'cross', 'save', 'hello', 'trees']
    df_combined['Faith_Density'] = df_combined['Lyrics'].apply(lambda x: count_themes(x, faith_words))

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Theological Density by Era")
        faith_avg = df_combined.groupby('album_name')['Faith_Density'].mean().reindex(target_albums).reset_index()
        fig_faith = px.line(faith_avg, x='album_name', y='Faith_Density', markers=True,
                            template='plotly_dark', title="Average Faith-Based Keywords")
        st.plotly_chart(fig_faith)

    with col_b:
        st.subheader("Lexical Diversity & Spiritual Complexity")
        # Comparing Vocabulary Richness to Faith Keywords
        fig_theo_scatter = px.scatter(df_combined, x='Lexical_Diversity', y='Faith_Density',
                                      color='album_name', hover_name='track_name', template='plotly_dark')
        st.plotly_chart(fig_theo_scatter)

    # 2. The Interactive Map
    st.divider()
    st.subheader("Scriptural Commentary")

    # Selection from the expanded map
    selected_theo_song = st.selectbox("Select a Song to see its Theological Root:", list(theology_map.keys()))

    t_data = theology_map[selected_theo_song]
    c1, c2 = st.columns([1, 2])
    with c1:
        st.info(f"**Theme:** {t_data['Theme']}")
        st.success(f"**Scripture:** {t_data['Verse']}")
    with c2:
        st.write(f"**Theological Lesson:** {t_data['Lesson']}")
        # Show lyrics snippet
        snippet = df_combined[df_combined['track_name'] == selected_theo_song]['Lyrics'].values[0][:500]
        st.caption(f"Lyrics Preview: {snippet}...")


# --- 6. SUMMARY METRICS ---
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