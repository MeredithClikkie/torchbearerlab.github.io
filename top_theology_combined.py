import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
import zlib
from matplotlib.backends.backend_pdf import PdfPages

# --- 1. SETUP (Must be the very first command) ---
st.set_page_config(page_title="TØP Ultimate Analytics", layout="wide")


@st.cache_data
def load_and_process_data():
    # Update this path to your local file
    file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
    df = pd.read_excel(file_path)

    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    stop_words = set(stopwords.words('english'))
    stop_words.update(['yeah', 'oh', 'ooh', 'woah', 'la', 'na', 'chorus', 'im', 'dont', 'lada', 'hoohoohoo'])

    # --- ADVANCED METRIC FUNCTIONS ---
    def calculate_diversity(text):
        words = str(text).lower().split()
        return len(set(words)) / len(words) if words else 0

    def calculate_repetition(text):
        if not text or len(str(text)) < 10: return 0
        encoded = str(text).lower().encode('utf-8')
        return 1 - (len(zlib.compress(encoded)) / len(encoded))

    # --- APPLY ALL METRICS TO THE MAIN DATAFRAME ---
    # We do this BEFORE filtering to ensure all columns exist
    df['Clean_Lyrics'] = df['Lyrics'].apply(
        lambda x: " ".join([w for w in str(x).lower().split() if w.isalpha() and w not in stop_words]))
    df['Lexical_Diversity'] = df['Lyrics'].apply(calculate_diversity)
    df['Repetition_Score'] = df['Lyrics'].apply(calculate_repetition)

    sia = SentimentIntensityAnalyzer()
    df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

    return df, stop_words


# Load Data
df, stop_words = load_and_process_data()

# --- 2. CHRONOLOGY & FILTERING ---
release_dates = {
    "Twenty One Pilots": 2009, "Vessel": 2013, "Blurryface": 2015,
    "Trench": 2018, "Scaled And Icy": 2021, "Clancy": 2024, "Breach": 2025,
}
# Only include albums that actually exist in your Excel file
target_albums = [a for a in release_dates.keys() if a in df['album_name'].unique()]
df_combined = df[df["album_name"].isin(target_albums)].copy()
df_combined['release_year'] = df_combined['album_name'].map(release_dates)

# --- 3. THEOLOGY DATA MAP ---
theology_map = {
    "Taxi Cab": {"Theme": "The Trinity", "Verse": "Matthew 28:19",
                 "Lesson": "Divine rescue from death and the washing away of sin."},
    "Trees": {"Theme": "The Call of the Creator", "Verse": "Genesis 3:8-9",
              "Lesson": "The soul's journey from hiding in silence to bold recognition of God."},
    "Paladin Strait": {"Theme": "Spiritual Warfare", "Verse": "Ephesians 6:13",
                       "Lesson": "The final stand against spiritual strongholds (Bishops)."},
    "Oldies Station": {"Theme": "Sanctification", "Verse": "Galatians 6:9",
                       "Lesson": "Maintaining faith during the mundane, repetitive trials of life."},
    "Addict with a Pen": {"Theme": "Repentance", "Verse": "Psalm 42",
                          "Lesson": "Recognizing spiritual dryness and needing 'Living Water'."},
    "Tally": {"Theme": "Grace vs. Law", "Verse": "Matthew 12:36",
              "Lesson": "Acknowledging our account (tally) but relying on mercy."}
}

# --- 4. TABS DEFINITION (UNPACKED CORRECTLY) ---
st.title("|-/ Ultimate Discography Dashboard")
tab_journey, tab_theology, tab_tech, tab_export = st.tabs([
    "🚶 Emotional Journey", "🙏 Theology Map", "📊 Technical Metrics", "📄 Export Report"
])

# --- TAB 1: EMOTIONAL JOURNEY ---
with tab_journey:
    st.subheader("Discography Sentiment Distribution")
    fig_box = px.box(df_combined, x="album_name", y="Sentiment_Score", color="album_name",
                     points="all", template="plotly_dark", category_orders={"album_name": target_albums})
    st.plotly_chart(fig_box, use_container_width=True)

    st.divider()
    album_choice = st.selectbox("Select an Era for a Deep Dive", target_albums)
    filtered_df = df_combined[df_combined['album_name'] == album_choice].copy().reset_index(drop=True)

    col_chart, col_cloud = st.columns([2, 1])
    with col_chart:
        # Create unique track numbers 1, 2, 3...
        track_numbers = list(range(1, len(filtered_df) + 1))
        fig_journey = px.scatter(filtered_df, x=track_numbers, y='Sentiment_Score',
                                 hover_name='track_name', template="plotly_dark", title=f"Journey: {album_choice}")
        fig_journey.update_traces(mode='lines+markers', marker=dict(size=12, line=dict(width=1, color='white')))
        fig_journey.update_layout(xaxis_title="Track Number", yaxis_title="Sentiment Score")
        st.plotly_chart(fig_journey, use_container_width=True)

    with col_cloud:
        st.subheader("Era Themes")
        era_colors = {"Vessel": "Blues", "Blurryface": "Reds", "Trench": "YlOrBr", "Breach": "GnBu",
                      "Scaled And Icy": "PuBuGn", "Clancy": "Oranges"}
        wc_text = " ".join(filtered_df['Clean_Lyrics'])
        if wc_text:
            wc = WordCloud(background_color='black', colormap=era_colors.get(album_choice, "Reds")).generate(wc_text)
            fig_wc, ax = plt.subplots();
            ax.imshow(wc, interpolation='bilinear');
            ax.axis('off')
            st.pyplot(fig_wc)

# --- TAB 2: THEOLOGY MAP ---
with tab_theology:
    st.header("|-/ Theological Deep Dive")
    # Lexical Theology Calculation
    faith_words = ['god', 'faith', 'believe', 'pray', 'soul', 'spirit', 'cross', 'save', 'hello', 'trees']
    df_combined['Faith_Density'] = df_combined['Lyrics'].apply(
        lambda x: sum(1 for w in str(x).lower().split() if w in faith_words))

    col_a, col_b = st.columns(2)
    with col_a:
        faith_avg = df_combined.groupby('album_name')['Faith_Density'].mean().reindex(target_albums).reset_index()
        fig_faith = px.line(faith_avg, x='album_name', y='Faith_Density', markers=True, template='plotly_dark',
                            title="Faith Keywords by Era")
        st.plotly_chart(fig_faith)
    with col_b:
        fig_theo_scatter = px.scatter(df_combined, x='Lexical_Diversity', y='Faith_Density', color='album_name',
                                      hover_name='track_name', template='plotly_dark',
                                      title="Vocabulary Complexity vs. Spiritual Theme")
        st.plotly_chart(fig_theo_scatter)

    st.divider()
    sel_theo_song = st.selectbox("Select a Song for Scriptural Commentary:", list(theology_map.keys()))
    t_data = theology_map[sel_theo_song]
    st.info(f"**Theme:** {t_data['Theme']} | **Verse:** {t_data['Verse']}")
    st.write(f"**Lesson:** {t_data['Lesson']}")

# --- TAB 3: TECHNICAL METRICS ---
with tab_tech:
    st.header("Lyrical Richness & Structure")
    c1, c2 = st.columns(2)
    with c1:
        div_avg = df_combined.groupby('album_name')['Lexical_Diversity'].mean().reindex(target_albums).reset_index()
        st.plotly_chart(px.bar(div_avg, x='Lexical_Diversity', y='album_name', orientation='h',
                               color='Lexical_Diversity', template='plotly_dark', title="Lexical Diversity"))
    with c2:
        rep_avg = df_combined.groupby('album_name')['Repetition_Score'].mean().reindex(target_albums).reset_index()
        st.plotly_chart(px.line(rep_avg, x='album_name', y='Repetition_Score', markers=True, template='plotly_dark',
                                title="Repetition Over Time"))

# --- TAB 4: EXPORT REPORT ---
with tab_export:
    st.header("Generate Findings PDF")
    if st.button("Generate TØP Theological Analysis"):
        report_path = 'TOP_Analysis_Report.pdf'
        with PdfPages(report_path) as pdf:
            # Table Page
            plt.figure(figsize=(11, 8.5));
            plt.axis('off')
            plt.text(0.5, 0.9, "Twenty One Pilots: Analysis Summary", ha='center', fontsize=16, weight='bold')
            metrics = df_combined.groupby('album_name')[
                ['Sentiment_Score', 'Lexical_Diversity', 'Faith_Density']].mean().reindex(target_albums)
            plt.table(cellText=metrics.values.round(3), colLabels=metrics.columns, rowLabels=metrics.index,
                      loc='center')
            pdf.savefig();
            plt.close()
        st.success(f"Report Generated: {report_path}")