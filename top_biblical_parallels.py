import streamlit as st

# 1. Setup Data: Song Lyrics and Biblical Parallels
data = {
    "Trees": {
        "lyrics": """I know where you stand, silent in the trees,
And that's where I am, silent in the trees.
Why won't you speak? Where I happen to be?
Silent in the trees, standing cowardly.""",
        "verse_ref": "Genesis 3:8-9",
        "bible_text": "Then the man and his wife heard the sound of the Lord God as he was walking in the garden in the cool of the day, and they hid from the Lord God among the trees of the garden. But the Lord God called to the man, 'Where are you?'",
        "thematic_link": "A direct echo of the Fall of Man, where humanity hides in shame and God initiates the dialogue."
    },
    "Taxi Cab": {
        "lyrics": """A beautifully plain taxi cab can find it's way,
to take a man from his hideout to a better place...
Then there were three men up front,
and they said 'We had to steal him from his fate.'""",
        "verse_ref": "Proverbs 4:18 / Matthew 28:19",
        "bible_text": "The path of the righteous is like the morning sun, shining ever brighter till the full light of day. (Proverbs 4:18) \n\nGo therefore and make disciples of all nations... in the name of the Father and of the Son and of the Holy Spirit. (Matthew 28:19)",
        "thematic_link": "The 'three men' are often interpreted as the Holy Trinity, intervening to save the narrator from death (the hearse)."
    },
    "Addict with a Pen": {
        "lyrics": """I try desperately to run through the sand,
As I hold the water in the palm of my hand.
'Cause it's all that I have and it's all that I need,
And the waves of the water mean nothing to me.""",
        "verse_ref": "John 4:14",
        "bible_text": "But whoever drinks the water I give them will never thirst. Indeed, the water I give them will become in them a spring of water welling up to eternal life.",
        "thematic_link": "The desert represents a spiritual wasteland, and the water represents the 'Living Water' that provides spiritual sustenance."
    },
    "Holding on to You": {
        "lyrics": """Tie a noose around your mind, loose enough to breathe fine and tie it,
To a tree, tell it, 'You belong to me. This ain't a noose, this is a leash.'""",
        "verse_ref": "2 Corinthians 10:5",
        "bible_text": "We demolish arguments and every pretension that sets itself up against the knowledge of God, and we take captive every thought to make it obedient to Christ.",
        "thematic_link": "A literal visualization of 'taking thoughts captive' and exerting control over the darker parts of the mind."
    },
"Implicit Demand for Proof": {
        "lyrics": "I know you're not a liar... so rain down and destroy me.",
        "verse_ref": "Job 13:3 / 1 Kings 18:38",
        "bible_text": "But I desire to speak to the Almighty and to argue my case with God.",
        "thematic_link": "The 'Doubting Thomas' or Job-like demand for God to manifest His presence."
    },
    "Overcompensate": {
        "lyrics": "So now you pick who you serve, you bow to the masses.",
        "verse_ref": "Joshua 24:15",
        "bible_text": "Choose this day whom you will serve... as for me and my house, we will serve the Lord.",
        "thematic_link": "The choice between following the 'Bishops' (Dema) or a higher truth."
    },
    "Fall Away": {
        "lyrics": "I don't want your way, I want mine.",
        "verse_ref": "Romans 7:15 / Genesis 3",
        "bible_text": "I do not understand what I do. For what I want to do I do not do, but what I hate I do.",
        "thematic_link": "The inherent human struggle between self-will and divine will (original sin)."
    }
}

# 2. App Interface
st.set_page_config(page_title="Gospel of TØP", layout="wide")
st.title("|-/ The Gospel According to TØP")

# Sidebar Search & Filter
search_query = st.sidebar.text_input("Search themes (e.g., 'Water', 'Trinity', 'Sin')")
song_list = list(data.keys())

# Filter logic
if search_query:
    song_list = [s for s in song_list if
                 search_query.lower() in data[s]['thematic_link'].lower() or search_query.lower() in s.lower()]

song_choice = st.sidebar.selectbox("Select a Song", song_list)

if song_choice:
    selected = data[song_choice]

    # 3. Side-by-Side View
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Lyrical Snapshot")
        st.info(f"\"{selected['lyrics']}\"")

    with col2:
        st.subheader(f"Biblical Parallel ({selected['verse_ref']})")
        st.success(selected['bible_text'])

    st.divider()
    st.markdown("### The Theological Connection")
    st.write(selected['thematic_link'])
else:
    st.warning("No songs found matching that theme. Try searching for 'Water' or 'Fate'.")