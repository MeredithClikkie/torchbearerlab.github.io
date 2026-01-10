import streamlit as st
import pandas as pd
from textblob import TextBlob

# Mock Data: In a real app, you would load your scraped lyrics here
data = {
    "Album/Source": ["Self-Titled", "Vessel", "Blurryface", "Trench", "Scales & Icy", "Clancy", "Psalms (Selection)"],
    "Lyrical Hope": [0.05, 0.12, -0.05, 0.15, 0.25, 0.18, 0.30],  # Example Polarity Scores
    "Theme": ["Raw Faith", "Introspection", "Insecurity", "Metaphor", "Optimism", "Resolution", "Praise/Lament"]
}

df = pd.DataFrame(data).set_index("Album/Source")

st.title("🎵 Lyrical Sentiment & Theme Analysis")
st.markdown("""
Compare the emotional arc of **Twenty One Pilots** to the **Psalms**. 
Both often follow a cycle of *doubt, repentance, and hope*.
""")

# Display the Line Chart
st.subheader("Sentiment Tracking: Hope vs. Anxiety")
st.line_chart(df["Lyrical Hope"])

# Theme Analysis Section
st.subheader("Theme Comparison")
selected_album = st.selectbox("Select an album to see its core theme:", df.index)
st.info(f"The primary theme of **{selected_album}** is: **{df.loc[selected_album, 'Theme']}**")

# Functional Sentiment Input
st.divider()
st.write("### Try it yourself")
user_lyrics = st.text_area("Paste a lyric to analyze its 'Hope' score:")
if user_lyrics:
    score = TextBlob(user_lyrics).sentiment.polarity
    st.metric("Sentiment Score", round(score, 2), delta="Positive/Hopeful" if score > 0 else "Negative/Anxious")