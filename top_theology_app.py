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

# --- 1. SETUP & DATA PROCESSING ---
st.set_page_config(page_title="TØP Theology & Tech", layout="wide")


@st.cache_data
def load_and_process():
    file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
    df = pd.read_excel(file_path)

    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    stop_words = set(stopwords.words('english'))
    # Custom stop words based on your specific TØP list
    stop_words.update(['yeah', 'oh', 'ooh', 'verse', 'chorus', 'im', 'dont', 'lada', 'hoohoohoo'])

    # Calculating Advanced Metrics
    def get_diversity(text):
        words = str(text).lower().split()
        return len(set(words)) / len(words) if words else 0

    def get_repetition(text):
        if not text or len(str(text)) < 10: return 0
        encoded = str(text).lower().encode('utf-8')
        return 1 - (len(zlib.compress(encoded)) / len(encoded))

    df['Clean_Lyrics'] = df['Lyrics'].apply(
        lambda x: " ".join([w for w in str(x).lower().split() if w.isalpha() and w not in stop_words]))
    df['Lexical_Diversity'] = df['Lyrics'].apply(get_diversity)
    df['Repetition_Score'] = df['Lyrics'].apply(get_repetition)

    sia = SentimentIntensityAnalyzer()
    df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

    return df, stop_words


df, stop_words = load_and_process()
target_albums = ["Twenty One Pilots", "Vessel", "Blurryface", "Trench", "Breach", "Scaled And Icy", "Clancy"]
df_combined = df[df["album_name"].isin(target_albums)].copy()

# --- 2. THEOLOGY MAPPING DATA ---
theology_map = {
    "Taxi Cab": {"Theme": "The Trinity", "Verse": "Matt 28:19",
                 "Lesson": "Divine rescue from death and the washing away of blood/sin."},
    "Trees": {"Theme": "Divine Silence", "Verse": "Genesis 3:8",
              "Lesson": "The soul's desperate cry to a Creator who seems to hide."},
    "Paladin Strait": {"Theme": "Spiritual Warfare", "Verse": "Ephesians 6:13",
                       "Lesson": "The final stand against spiritual strongholds (Bishops)."},
    "Oldies Station": {"Theme": "Sanctification", "Verse": "Galatians 6:9",
                       "Lesson": "Pushing through the mundane struggle of the 'Oldies Station' of life."},
    "Tally": {"Theme": "Grace vs. Law", "Verse": "Matthew 12:36",
              "Lesson": "The realization of our 'tally' of mistakes and the need for mercy."},
    "Addict with a Pen": {"Theme": "Repentance", "Verse": "Psalm 42",
                          "Lesson": "Seeking 'Living Water' in a desert of spiritual dryness."}
}

# --- 3. DEFINING THE TABS ---
# This is where we define the variables correctly to avoid NameErrors
tab_theo, tab_tech, tab_export = st.tabs(["🙏 Theology Map", "📊 Technical Metrics", "📄 Export Report"])

# --- TAB 1: THEOLOGY MAP ---
with tab_theo:
    st.header("|-/ Scriptural Commentary")

    # 1. Selection
    sel_song = st.selectbox("Select a song to see its theological root:", list(theology_map.keys()))
    t_info = theology_map[sel_song]

    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.success(f"**Theme:** {t_info['Theme']}")
        st.info(f"**Scripture:** {t_info['Verse']}")
    with col_b:
        st.write(f"**Theological Lesson:** {t_info['Lesson']}")

    st.divider()

    # 2. Faith Density Chart
    faith_lexicon = ['god', 'faith', 'believe', 'pray', 'soul', 'spirit', 'halo', 'jesus', 'cross', 'trees']
    df_combined['Faith_Count'] = df_combined['Lyrics'].apply(
        lambda x: sum(1 for w in str(x).lower().split() if w in faith_lexicon))

    st.subheader("Theological Density (Faith Keywords)")
    fig_theo = px.scatter(df_combined, x='Sentiment_Score', y='Faith_Count', color='album_name',
                          hover_name='track_name', template='plotly_dark')
    st.plotly_chart(fig_theo, use_container_width=True)

# --- TAB 2: TECHNICAL METRICS ---
with tab_tech:
    st.header("Technical Complexity: Diversity & Structure")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Lexical Diversity")
        div_data = df_combined.groupby('album_name')['Lexical_Diversity'].mean().reindex(target_albums).reset_index()
        fig_div = px.bar(div_data, x='Lexical_Diversity', y='album_name', orientation='h', color='Lexical_Diversity',
                         template='plotly_dark')
        st.plotly_chart(fig_div)
        st.caption("Vocabulary Richness: Higher = More unique words.")

    with c2:
        st.subheader("Repetition (Formulaic Patterns)")
        rep_data = df_combined.groupby('album_name')['Repetition_Score'].mean().reindex(target_albums).reset_index()
        fig_rep = px.line(rep_data, x='album_name', y='Repetition_Score', markers=True, template='plotly_dark')
        st.plotly_chart(fig_rep)
        st.caption("Repetition: Spikes indicate more formulaic/repeating hooks.")

# --- TAB 3: EXPORT REPORT ---
with tab_export:
    st.header("Download Findings")
    if st.button("Generate Full PDF Analysis"):
        report_name = "TOP_Theological_Report.pdf"
        with PdfPages(report_name) as pdf:
            # Table Page
            plt.figure(figsize=(11, 8.5))
            plt.axis('off')
            plt.text(0.5, 0.9, "|-/ Discography Summary Report", ha='center', fontsize=16, weight='bold')
            metrics = df_combined.groupby('album_name')[
                ['Sentiment_Score', 'Lexical_Diversity', 'Faith_Count']].mean().reindex(target_albums)
            plt.table(cellText=metrics.values.round(3), colLabels=metrics.columns, rowLabels=metrics.index,
                      loc='center')
            pdf.savefig()
            plt.close()

            # Plot Page
            plt.figure(figsize=(10, 6))
            df_combined.groupby('album_name')['Faith_Count'].mean().reindex(target_albums).plot(kind='bar',
                                                                                                color='gold')
            plt.title("Theological Keyword Density by Era")
            pdf.savefig()
            plt.close()

        st.success(f"Report saved to your desktop as {report_name}")