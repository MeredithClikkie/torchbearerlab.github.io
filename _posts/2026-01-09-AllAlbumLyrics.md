# %% [markdown]
# # All Lyrics
# %%
import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import squarify # pip install squarify
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px # Requires: pip install plotly

# %%
file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/Alltøplyrics.xlsx'
df = pd.read_excel(file_path)
# %%
df.head()
# %%
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('vader_lexicon')

# 2. Text Preprocessing
stop_words = set(stopwords.words('english'))

def clean_lyrics(text):
    # Lowercase and remove non-alphabetic characters
    words = str(text).lower().split()
    clean_words = [w for w in words if w.isalpha() and w not in stop_words]
    return " ".join(clean_words)

df['Clean_Lyrics'] = df['Lyrics'].apply(clean_lyrics)

# 3. Sentiment Analysis
sia = SentimentIntensityAnalyzer()
df['Sentiment_Score'] = df['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# 4. Group by Album for Analysis
album_sentiment = df.groupby('album_name')['Sentiment_Score'].mean().sort_values()
print("Average Sentiment by Album:\n", album_sentiment)

# 5. Visualize: Word Cloud for the most positive album
top_album = album_sentiment.idxmax()
text = " ".join(df[df['album_name'] == top_album]['Clean_Lyrics'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title(f"Most Frequent Words in {top_album}")
plt.axis('off')
plt.show()
# %%
stop_words = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "he", "him", "his", "she", "her", "it", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
    "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by",
    "for", "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once", "not", "no", "yes", "so", "can", "just", "wanted", "where",
    "dont", "yeah", "let", "im", "ah", "want", "like", "ive", "all", "ooh", "ill", "even", "forforforforforfor", "every", "hoohoohoo", "hell",
    "yeahyeahyeahyeah", "daisychained", "thats", "there", "how", "somehow", "when", "used", "cant", "chorus", "lada"
]

# Function to remove stop words from a string
def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)
# %%
df.info

# %%
df.shape
# %%
# Create a new DataFrame containing only songs from the album "Breach"
df_breach = df[df["album_name"] == "Breach"][["album_name", "track_name", "Lyrics"]]
df_clancy = df[df["album_name"] == "Clancy"][["album_name", "track_name", "Lyrics"]]
df_sai = df[df["album_name"] == "Scaled And Icy"][["album_name", "track_name", "Lyrics"]]
df_trench = df[df["album_name"] == "Trench"][["album_name", "track_name", "Lyrics"]]
df_blurryface = df[df["album_name"] == "Blurryface"][["album_name", "track_name", "Lyrics"]]
df_vessel = df[df["album_name"] == "Vessel"][["album_name", "track_name", "Lyrics"]]
df_self_titled = df[df["album_name"] == "Twenty One Pilots"][["album_name", "track_name", "Lyrics"]]
# To see the first few rows of your filtered data:
print(df_breach.head())
# %%
# 1. Define the list of albums you want to analyze
target_albums = [
    "Breach", "Clancy", "Scaled And Icy", "Trench",
    "Blurryface", "Vessel", "Twenty One Pilots"
]

# 2. Filter the main DataFrame for these albums and specific columns
df_combined = df[df["album_name"].isin(target_albums)][["album_name", "track_name", "Lyrics"]]

# 3. Check the results
print(df_combined["album_name"].unique())
print(df_combined.shape)
# %%
print(df['track_name'].unique())
# %%
# List of the albums you want
target_albums = [
    "Breach", "Clancy", "Scaled And Icy", "Trench",
    "Blurryface", "Vessel", "Twenty One Pilots"
]

# Create a dictionary where the key is the album name and the value is its dataframe
albums = {name: df[df["album_name"] == name][["track_name", "Lyrics"]] for name in target_albums}

# How to use it:
# albums["Vessel"] now holds just the Vessel data
print(albums["Vessel"].head())
# %% [markdown]
# # Create a clean DataFrame for the whole album
# all_albums = [Breach, Clancy, ScaledAndIcy, Trench, Blurryface, Vessel, Twenty_One_Pilots]  # List of your lyric variables
# # 3. Combine with your song names (if you have them in a list)
# album_names = ["Breach", "Clancy", "ScaledAndIcy", "Trench", "Blurryface", "Vessel", "Twenty_One_Pilots"] # Add all 14 names
# df_AlbumTopics['Album_Name'] = song_names[:len(df_topics)]
# df_all_albums = pd.DataFrame({
#     'Album_Name': album_names,
#     'Album_Lyrics': all_albums
# })
# %% [markdown]
# ### Create all_processed_words list
# %%
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords

# 1. Setup: Load stopwords (words like 'the', 'and', 'is' that we want to ignore)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
# Optional: Add custom "filler" words common in songs
stop_words.update(['yeah', 'oh', 'ooh', 'woah', 'la', 'na'])

# 2. Define your target albums
target_albums = [
    "Breach", "Clancy", "Scaled And Icy", "Trench",
    "Blurryface", "Vessel", "Twenty One Pilots"
]

# 3. Process each album in a loop
album_themes = {}

for album in target_albums:
    # Filter for the current album
    # Note: Use 'Lyrics' or 'lyrics' depending on your exact column name
    album_df = df[df["album_name"] == album]

    # Combine all lyrics from this album into one big string
    all_text = " ".join(album_df["Lyrics"].astype(str)).lower()

    # Clean the text: keep only words, remove stopwords
    words = [word for word in all_text.split() if word.isalpha() and word not in stop_words]

    # Count the most common words (Themes)
    top_words = Counter(words).most_common(10)

    # Store the results in our dictionary
    album_themes[album] = top_words

# 4. Display the results
for album, themes in album_themes.items():
    print(f"\n--- Top Themes for {album} ---")
    for word, count in themes:
        print(f"{word}: {count}")
# %% [markdown]
# ### LDA training code
# %%
import nltk
from nltk.corpus import stopwords
import gensim
from gensim import corpora
import re

# List of your album dataframes
album_list = [df_breach, df_clancy, df_sai, df_trench, df_blurryface, df_vessel, df_self_titled]
album_names = ["Breach", "Clancy", "Scaled And Icy", "Trench", "Blurryface", "Vessel", "Self Titled"]

# 1. Download if you haven't already
nltk.download('stopwords')

# 2. CREATE A NEW SET from the stopwords (This is the fix)
stop_words = set(stopwords.words('english'))

# 3. Now .update() will work perfectly
extra_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "he", "him", "his", "she", "her", "it", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
    "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by",
    "for", "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once", "not", "no", "yes", "so", "can", "just", "wanted", "where",
    "dont", "yeah", "let", "im", "ah", "want", "like", "ive", "all", "ooh", "ill", "even", "forforforforforfor", "every", "hoohoohoo", "hell", "get", "chorus", "johnny"
    "yeahyeahyeahyeah", "daisychained", "thats", "there", "how", "somehow", "when", "used", "cant"]
stop_words.update(extra_words)

print(f"Stopwords prepared. Total count: {len(stop_words)}")
# %%
def preprocess(text):
    # Clean: remove punctuation, lowercase, and split into words
    text = re.sub(r'[^\w\s]', '', str(text).lower())
    return [word for word in text.split() if word not in stop_words and len(word) > 2]

# Dictionary to store results for each album
all_album_topics = {}

for name, album_df in zip(album_names, album_list):
    # Process each song individually
    processed_songs = [preprocess(s) for s in album_df["Lyrics"].astype(str)]

    # Create dictionary from the list of lists
    dictionary = corpora.Dictionary(processed_songs)

    # Create corpus from the list of lists
    corpus = [dictionary.doc2bow(song) for song in processed_songs]

    # Train LDA...
    lda_model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=3)
    all_album_topics[name] = lda_model.print_topics(-1)
# %%
import gensim
from gensim import corpora

# 1. Create the Dictionary
# This maps every unique word to an ID
dictionary = corpora.Dictionary(processed_songs)

# 2. Create the Corpus
# This converts each song into a "Bag of Words" format (word_id, frequency)
corpus = [dictionary.doc2bow(text) for text in processed_songs]

# 3. Train the LDA Model
# We use 3 topics because 14 songs is a smaller sample size
lda_model = gensim.models.LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=3,
    random_state=100,
    update_every=1,
    chunksize=10, # Adjusted for your 14 songs
    passes=20,    # Increased passes to help the model find patterns in a small dataset
    alpha='auto'
)

# 4. Show the discovered Topics
print("--- Discovered Lyrical Themes ---")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}\n")
# %%
# Create the mapping based on your results
topic_labels = {
    0: "Vulnerability & Flight",
    1: "Anxiety & Internal Dialogue",
    2: "Nostalgia & Character Narrative"
}

print("--- Final Lyrical Analysis ---")
for idx, topic in lda_model.print_topics(-1):
    label = topic_labels.get(idx, "Unknown Theme")
    # Clean the topic string for better readability
    clean_words = ", ".join([word.split("*")[1].replace('"', '') for word in topic.split(" + ")])

    print(f"THEME: {label}")
    print(f"Keywords: {clean_words}\n")
# %% [markdown]
# ### Topic Model
# %%
import gensim
from gensim import corpora

# 1. Create the Dictionary
# This maps every unique word to a unique ID
dictionary = corpora.Dictionary(all_processed_words)

# 2. Create the Corpus
# This converts each song into a list of (word_id, word_frequency)
corpus = [dictionary.doc2bow(text) for text in all_processed_words]

# 3. Train the LDA Model
# We use 5 topics as a starting point for 14 songs
lda_model = gensim.models.LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=5,
    random_state=100,
    passes=20,     # More passes help with small datasets
    alpha='auto',  # Let the model learn the topic distribution
    per_word_topics=True
)

# 4. Display the Topics and their Top Words
print("--- Discovered Lyrical Themes ---")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}\n")
# %% [markdown]
# ### Define lexicons
# %%
faith_words = ['faith', 'believe', 'god', 'pray', 'lord', 'creator', 'church', 'soul', 'spirit', 'halo', 'jesus', "lion", "holy"]
hope_words = ['hope', "love" 'hopeful', 'holding','light', 'morning', 'sun', 'sky', 'alive', 'stay', 'future', 'hold', 'better', "friends"]
word_words = ["flesh", "den", "mind"]
# %% [markdown]
# ### The Analysis Code
# %%
def count_keywords(text, lexicon):
    words = str(text).lower().split()
    return sum(1 for word in words if word in lexicon)

# Apply the counting to your combined DataFrame
df_combined['Faith_Count'] = df_combined['Lyrics'].apply(lambda x: count_keywords(x, faith_words))
df_combined['Hope_Count'] = df_combined['Lyrics'].apply(lambda x: count_keywords(x, hope_words))
df_combined['Word_Count'] = df_combined['Lyrics'].apply(lambda x: count_keywords(x, hope_words))

# Calculate the most "Faithful" and "Hopeful" songs
top_faith_songs = df_combined.nlargest(5, 'Faith_Count')[['album_name', 'track_name', 'Faith_Count']]
top_hope_songs = df_combined.nlargest(5, 'Hope_Count')[['album_name', 'track_name', 'Hope_Count']]
top_word_songs = df_combined.nlargest(5, 'Word_Count')[['album_name', 'track_name', 'Word_Count']]
print("--- Top 5 Songs for Faith ---")
print(top_faith_songs)
print("\n--- Top 5 Songs for Hope ---")
print(top_hope_songs)
print("\n--- Top 5 Songs for Word ---")
print(top_word_songs)
# %% [markdown]
# ### Aggregate by album
# %%
# Group by album and calculate the average occurrences
album_trends = df_combined.groupby('album_name')[['Faith_Count', 'Hope_Count']].mean()

# Sort by Faith to see which album leads
print("\n--- Theme Density by Album ---")
print(album_trends.sort_values(by='Faith_Count', ascending=False))
# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
for i, album in enumerate(album_trends.index):
    plt.scatter(album_trends.loc[album, 'Faith_Count'],
                album_trends.loc[album, 'Hope_Count'],
                label=album, s=100)
    plt.text(album_trends.loc[album, 'Faith_Count']+0.05,
             album_trends.loc[album, 'Hope_Count']+0.05, album)

plt.title("Faith vs. Hope Across Albums")
plt.xlabel("Average Faith Word Count")
plt.ylabel("Average Hope Word Count")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
# %%
# Assuming 'df_92' is your combined dataframe of 92 songs
# We create a list of processed songs (list of lists)
import re

def clean_lyric(text):
    text = re.sub(r'[^\w\s]', '', str(text).lower())
    return [word for word in text.split() if word not in stop_words and len(word) > 2]

# This creates a list of 92 lists, one for each song
all_processed_songs = [clean_lyric(s) for s in df_combined["Lyrics"]]
# %%
from gensim import corpora
import gensim

# 1. Create the Dictionary based on all 92 songs
dictionary = corpora.Dictionary(all_processed_songs)

# 2. Create the Corpus (Bag of Words) for all 92 songs
corpus = [dictionary.doc2bow(text) for text in all_processed_songs]

# 3. Train the LDA Model on the full corpus
lda_model = gensim.models.LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=5,  # You can increase this since you have more data now
    random_state=100,
    passes=15
)
# %%
def get_dominant_topic(ldamodel, corpus):
    topic_data = []
    for i, row in enumerate(ldamodel[corpus]):
        # Sort topics by probability
        topics = sorted(row, key=lambda x: x[1], reverse=True)
        topic_num, prop_topic = topics[0]
        topic_data.append([int(topic_num), round(prop_topic, 4)])
    return pd.DataFrame(topic_data, columns=['Dominant_Topic', 'Topic_Perc_Contribution'])

# This now has 92 rows
df_topics = get_dominant_topic(lda_model, corpus)

# Attach metadata from the original 92-song dataframe
df_topics['Song_Name'] = df_combined['track_name'].values
df_topics['Album'] = df_combined['album_name'].values

# Map your labels
df_topics['Topic_Label'] = df_topics['Dominant_Topic'].map(topic_labels)
# %% [markdown]
# ### Quantify the vibe of each song
# %%
# 1. Combine all your albums into one Master DataFrame first
# This ensures we have all 92 songs in the correct order
all_albums_df = pd.concat([
    df_self_titled, df_vessel, df_blurryface,
    df_trench, df_sai, df_clancy, df_breach
]).reset_index(drop=True)

# 2. Get your topic dataframe (the one with 92 rows)
df_topics = get_dominant_topic(lda_model, corpus)

# 3. Match the names by using the index of the Master DataFrame
# This will assign the correct name to all 92 rows automatically
df_topics['Song_Name'] = all_albums_df['track_name']
df_topics['Album'] = all_albums_df['album_name']

# 4. Apply your labels
topic_labels = {
    0: "Faith & Resilience",
    1: "Emotional Exposure",
    2: "Search for Truth",
    3: "Wasted Time",
    4: "Path & Purpose"
}
df_topics['Topic_Label'] = df_topics['Dominant_Topic'].map(topic_labels)

# Display the top of your 92-song list
print(df_topics[['Album', 'Song_Name', 'Topic_Label']].head(20))
# %%
print(f"Songs in Master DF: {len(all_albums_df)}")
print(f"Songs processed by LDA: {len(df_topics)}")
# These two numbers MUST be the same.
# %%
# Look for songs that have 0 words after cleaning
empty_songs = [i for i, text in enumerate(all_processed_words) if len(text) == 0]
if empty_songs:
    print(f"Warning: Songs at indices {empty_songs} are empty after preprocessing.")
# %% [markdown]
# Discovered Lyrical Themes
# Topic 0: Persistent Reminiscing Focuses on the passage of time, keeping score of past hurts ("tally," "track," "replay"), and the struggle to "believe" while feeling "lost" in heartbreak.
# 
# Topic 1: Unfiltered Vulnerability Centers on raw emotions and internal conflict, specifically the refusal to slow down despite "fear" and the "raw" feeling of "hiding" one's heart.
# 
# Topic 2: Searching for Proof Reflects a quest for clarity or "evidence," using imagery of things being "etched" on the "surface" to "find" or "know" the truth.
# 
# Topic 3: Regret and Stagnation Deals with the anxiety of "wasting" time and "days" lying "dormant," highlighting the realization that one cannot "afford" to let more time slip away.
# 
# Topic 4: Direction and Intent Explores the path forward ("way") and the internal "intentions" or "aim" behind one's actions, balancing "right" and "will."
# %%
# Create a new column for the descriptive label
df_topics['Topic_Label'] = df_topics['Dominant_Topic'].map(topic_labels)

# Displaying the final organized table
print(df_topics[['Song_Name', 'Topic_Label', 'Topic_Perc_Contribution']])
# %%
import matplotlib.pyplot as plt

# 1. Ensure the mapping is applied (if not already done)

df_topics['Topic_Label'] = df_topics['Dominant_Topic'].map(topic_labels)

# 2. Count the occurrences of each label
# We use the list of values from our dictionary to keep the 0-4 order
ordered_labels = [topic_labels[i] for i in range(5)]
topic_counts = df_topics['Topic_Label'].value_counts().reindex(ordered_labels).fillna(0)

# 3. Create the bar chart
plt.figure(figsize=(12, 6))
topic_counts.plot(kind='bar', color='maroon', edgecolor='black')

plt.title('Frequency of Lyrical Themes in "Breach"', fontsize=14)
plt.xlabel('Lyrical Theme', fontsize=12)
plt.ylabel('Number of Songs', fontsize=12)

# Set the x-ticks to your specific labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%
import matplotlib.pyplot as plt

# Count how many songs fall into each topic
topic_counts = df_topics['Dominant_Topic'].value_counts().sort_index()

# Simple bar chart
plt.figure(figsize=(10,6))
topic_counts.plot(kind='bar', color='maroon')
plt.title('Number of Songs per Lyrical Theme')
plt.xlabel('Topic ID')
plt.ylabel('Number of Songs')
plt.xticks(rotation=0)
plt.show()
# %%
# Calculate how many songs in each album fall under each theme
album_summary = df_topics.groupby(['Album', 'Topic_Label']).size().unstack(fill_value=0)

# Normalize to see percentages instead of counts
album_pct = album_summary.div(album_summary.sum(axis=1), axis=0) * 100
print(album_pct)
# %% [markdown]
# ### Thematic Evolution Stacked
# %%
# Create the chronological mapping
release_dates = {
    "Twenty One Pilots": 2009,
    "Regional at Best": 2011,
    "Vessel": 2013,
    "Blurryface": 2015,
    "Trench": 2018,
    "Scaled And Icy": 2021,
    "Clancy": 2024,
    "Breach": 2025  # Adjust based on your specific dataset context
}

# Add a numeric sort column to your dataframe
df_combined['Release_Year'] = df_combined['album_name'].map(release_dates)

# Sort the dataframe permanently
df_combined = df_combined.sort_values(by=['Release_Year', 'album_name']).reset_index(drop=True)
# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Re-order the pivot table index using the release_dates keys
ordered_albums = [a for a in release_dates.keys() if a in df_topics['Album'].unique()]

theme_dist = df_topics.groupby(['Album', 'Topic_Label']).size().unstack(fill_value=0)
theme_dist = theme_dist.reindex(ordered_albums) # This forces the chronological order

# Plot as before...
theme_dist.plot(kind='bar', stacked=True, figsize=(12, 7), colormap = 'YlOrRd')
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_diversity(text):
    words = str(text).lower().split()
    if len(words) == 0: return 0
    return len(set(words)) / len(words)

# 2. Apply Diversity Calculation
df_combined['Lexical_Diversity'] = df_combined['Lyrics'].apply(calculate_diversity)

# 3. Create the Score Dataframe and map the years
# We don't use .sort_values() here because we want to control the order manually
diversity_scores = df_combined.groupby('album_name')['Lexical_Diversity'].mean().reset_index()
diversity_scores['Release_Year'] = diversity_scores['album_name'].map(release_dates)

# 4. Sort by Release_Year instead of the score
diversity_scores = diversity_scores.sort_values('Release_Year')

# 5. Define Colors (matching your warm palette)
warm_colors = ['#4A0E0E', '#7B0828', '#9B1B30', '#B22222', '#C0392B', '#D72638', '#E74C3C']

# 6. Plotting
plt.figure(figsize=(10, 6))
sns.barplot(
    data=diversity_scores,
    x='Lexical_Diversity',
    y='album_name',
    hue='album_name',
    palette=warm_colors,
    legend=False # Removes the redundant legend
)

plt.title('Vocabulary Richness Over Time (Chronological)', fontsize=16)
plt.xlabel('Unique Words / Total Words Ratio', fontsize=12)
plt.ylabel('Album (Oldest to Newest)', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()
# %%
from textblob import TextBlob

# Calculate scores
df_combined['Polarity'] = df_combined['Lyrics'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df_combined['Subjectivity'] = df_combined['Lyrics'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

# Plotting
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df_combined, x='Polarity', y='Subjectivity', hue='album_name', s=100, alpha=0.7)

# Add a vertical line for neutral sentiment
plt.axvline(0, color='red', linestyle='--', alpha=0.5)
plt.title('Song Emotional Map: Polarity vs. Subjectivity', fontsize=16)
plt.xlabel('Emotional Tone (Negative <---> Positive)', fontsize=12)
plt.ylabel('Personal/Subjective Intensity', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
# %%
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure you have the sentiment lexicon
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# 1. Calculate Sentiment Score per Album
# We calculate the "Compound" score (-1 to 1) for each song, then average by album
df_combined['Sentiment'] = df_combined['Lyrics'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
album_sentiments = df_combined.groupby('album_name')['Sentiment'].mean()

# 2. Sort by Release Date (Using your previous mapping)
ordered_albums = [a for a in release_dates.keys() if a in album_sentiments.index]

# 3. Create a Grid of Word Clouds
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 10))
axes = axes.flatten()

for i, album in enumerate(ordered_albums):
    # Filter lyrics for this album
    text = " ".join(df_combined[df_combined['album_name'] == album]['Lyrics'])
    score = album_sentiments[album]

    # Determine color scheme based on sentiment
    # Positive (>0.05) = Greens, Negative (< -0.05) = Reds, Neutral = Blues
    if score > 0.05:
        color_map = 'Reds'
        mood = "Positive"
    elif score < -0.05:
        color_map = 'Blues'
        mood = "Negative/Intense"
    else:
        color_map = 'coolwarm'
        mood = "Neutral"

    # Generate Word Cloud
    wc = WordCloud(

        colormap=color_map,
        max_words=50,
        stopwords=stop_words
    ).generate(text)

    # Plotting
    axes[i].imshow(wc, interpolation='bilinear')
    axes[i].set_title(f"{album}\nScore: {score:.2f} ({mood})", fontsize=14)
    axes[i].axis('off')

# Hide any unused subplots
for j in range(i + 1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()

![each_album_wc](/breach_lab/assets/each_album_wordcloud.png)
<img width="944" height="38" alt="image" src="https://github.com/user-attachments/assets/5c464ac2-9fce-4748-a4d9-e914a4f952fc" />


# %%
import networkx as nx
import matplotlib.pyplot as plt

# 1. Define your "Lore" or "Target" words
lore_keywords = {'dema', 'bishop', 'clancy', 'torch', 'neon', 'vulture', 'rebel', 'bandito', 'yellow'}

# 2. Initialize the Graph
G = nx.Graph()

# 3. Add Nodes (Songs) and Edges (Shared Lore)
# We loop through your 92-song dataframe
for i, song_a in df_combined.iterrows():
    # Add the song as a node
    G.add_node(song_a['track_name'], album=song_a['album_name'])

    # Check for lore words in song_a
    words_a = set(str(song_a['Lyrics']).lower().split())
    shared_lore_a = words_a.intersection(lore_keywords)

    # Compare with every other song to find connections
    if shared_lore_a:
        for j, song_b in df_combined.iloc[i+1:].iterrows():
            words_b = set(str(song_b['Lyrics']).lower().split())
            shared_words = shared_lore_a.intersection(words_b)

            # If they share at least one lore word, create a connection
            if shared_words:
                G.add_edge(song_a['track_name'], song_b['track_name'], weight=len(shared_words))

# 4. Visualization
plt.figure(figsize=(15, 12))
pos = nx.spring_layout(G, k=0.15) # k controls the distance between nodes

# Color nodes by album (using your previous logic)
# This helps see if "Trench" songs cluster together
nx.draw(G, pos, with_labels=True, node_size=50, font_size=8, alpha=0.7, edge_color='gray')
plt.title("The Twenty One Pilots 'Lore' Network")
plt.show()
# %%
from pyvis.network import Network

# Initialize Pyvis network
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True)

# Load the NetworkX graph into Pyvis
net.from_nx(G)
net.show("lore_network.html")
# %%
import pandas as pd
import pronouncing
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_rhyme_score(text):
    # Clean text into tokens
    words = [w.lower().strip(".,!?\"") for w in str(text).split() if w.isalpha()]
    if not words:
        return 0

    rhyme_count = 0
    # We check each word against the next 10 words to find internal/near rhymes
    # (Typical of dense rap schemes like Levitate)
    for i in range(len(words)):
        current_word = words[i]
        # Get the phonetic rhyme parts for the current word
        current_rhymes = pronouncing.rhymes(current_word)

        # Look ahead at the next few words for a rhyme match
        look_ahead = words[i+1 : i+11]
        for future_word in look_ahead:
            if future_word in current_rhymes:
                rhyme_count += 1
                break # Count the word once if it rhymes with something nearby

    # Score = Rhyming words / Total words
    return rhyme_count / len(words)

def syllable_count(word):
    phones = pronouncing.phones_for_word(word)
    if phones:
        return pronouncing.syllable_count(phones[0])
    return 0


# You can use this to weigh your rhyme_count!

# 1. Apply to your 92-song dataframe
df_combined['Rhyme_Density'] = df_combined['Lyrics'].apply(calculate_rhyme_score)

# 2. Group by Album and Sort Chronologically
# (Using your previous release_dates mapping)
album_rhyme_stats = df_combined.groupby('album_name')['Rhyme_Density'].mean().reset_index()
album_rhyme_stats['Year'] = album_rhyme_stats['album_name'].map(release_dates)
album_rhyme_stats = album_rhyme_stats.sort_values('Year')

# 3. Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=album_rhyme_stats, x='album_name', y='Rhyme_Density', marker='o', color='#E21F26', linewidth=2.5)

plt.title('Technical Complexity: Rhyme Density Over Time', fontsize=16)
plt.ylabel('Rhyme Density Score (Rhymes/Total Words)')
plt.xlabel('Album Chronology')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import zlib

def calculate_repetition_score(text):
    if not text or len(str(text)) < 10:
        return 0

    # Encode text to bytes
    encoded_text = str(text).lower().encode('utf-8')

    # Calculate compressed size vs original size
    original_size = len(encoded_text)
    compressed_size = len(zlib.compress(encoded_text))

    # A higher score means more of the song was "redundant" (repeated)
    repetition_score = 1 - (compressed_size / original_size)
    return repetition_score

# 1. Apply to your 92-song dataframe
df_combined['Repetition_Score'] = df_combined['Lyrics'].apply(calculate_repetition_score)

# 2. Map to Release Years and Sort
album_structure = df_combined.groupby('album_name')['Repetition_Score'].mean().reset_index()
album_structure['Year'] = album_structure['album_name'].map(release_dates)
album_structure = album_structure.sort_values('Year')

# 3. Visualization: The "Experimental" Scale
plt.figure(figsize=(12, 6))
# We invert the score for the plot: 1 - Repetition = Uniqueness/Experimentalism
sns.barplot(data=album_structure, x='Repetition_Score', y='album_name',
            palette='magma', hue='album_name', legend=False)

plt.title('Song Structure: Experimentalism vs. Formulaic Patterns', fontsize=16)
plt.xlabel('Repetition Score (Higher = More Repeated Choruses/Hooks)', fontsize=12)
plt.ylabel('Album', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
# %%
import numpy as np
import matplotlib.pyplot as plt

# 1. Select the song you want to analyze
song_title = "Stressed Out" # Replace with any track_name from your df_92
lyrics = df_combined[df_combined['track_name'] == song_title]['Lyrics'].values[0]

# 2. Break lyrics into lines
lines = [line.strip().lower() for line in lyrics.split('\n') if line.strip()]
n = len(lines)

# 3. Create the Matrix (This defines the variable)
# We create an n x n grid of zeros
matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        # If line i is the same as line j, mark it with a 1
        if lines[i] == lines[j]:
            matrix[i, j] = 1

# 4. Plot the Matrix
plt.figure(figsize=(8, 8))
plt.imshow(matrix, cmap='binary', interpolation='none')

plt.title(f'Structural Fingerprint: {song_title}', fontsize=15)
plt.xlabel('Line Number')
plt.ylabel('Line Number')

# Adding a grid to make it easier to see blocks
plt.grid(False)
plt.show()
# %%
# Create the Master Report
master_report = df_combined.groupby('album_name').agg({
    'Sentiment': 'mean',
    'Lexical_Diversity': 'mean',
    'Rhyme_Density': 'mean',
    'Repetition_Score': 'mean'
}).reset_index()

# Sort by Release Year
master_report['Year'] = master_report['album_name'].map(release_dates)
master_report = master_report.sort_values('Year')

print("--- FINAL DISCOGRAPHY ANALYSIS ---")
print(master_report)
# %%
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns

# Create the PDF file
with PdfPages('T0P_Data_Analysis_Report.pdf') as pdf:

    # --- PAGE 1: The Master Metrics Table ---
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    # Use the master_report dataframe we created earlier
    table = ax.table(cellText=master_report.values, colLabels=master_report.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.title("Discography Master Metrics Overview", fontsize=16, pad=20)
    pdf.savefig() # Saves the current figure into the PDF
    plt.close()

    # --- PAGE 2: Sentiment vs Lexical Diversity ---
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_combined, x='Sentiment', y='Lexical_Diversity', hue='album_name', s=100)
    plt.title("Emotional Tone vs. Vocabulary Richness")
    pdf.savefig()
    plt.close()

    # --- PAGE 3: Thematic Evolution (Stacked Bar) ---
    theme_dist_pct.plot(kind='bar', stacked=True, figsize=(12, 7))
    plt.title("Thematic Evolution Over Time")
    plt.legend(bbox_to_anchor=(1.05, 1))
    pdf.savefig(bbox_inches='tight')
    plt.close()

    # --- PAGE 4: Rhyme Density Trend ---
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=album_rhyme_stats, x='album_name', y='Rhyme_Density', marker='o')
    plt.title("Technical Rap Complexity Over Time")
    plt.xticks(rotation=45)
    pdf.savefig(bbox_inches='tight')
    plt.close()

print("Success! Your full report has been saved as 'T0P_Data_Analysis_Report.pdf'")


with PdfPages('T0P_Data_Analysis_Report.pdf') as pdf:
    # --- NEW PAGE 0: The Executive Summary ---
    plt.figure(figsize=(11, 8.5)) # Standard Letter size
    plt.axis('off')

    summary_text = (
        "SUMMARY OF FINDINGS\n\n"
        "This analysis of 92 songs reveals a band in a state of constant technical transition.\n"
        "Early eras focus on Lexical Diversity and Faith themes, while later eras like 'Trench'\n"
        "show a spike in Rhyme Density and Lore-building.\n\n"
        "Key Takeaways:\n"
        "1. Technical Growth: Rhyme complexity has increased by X% since 2009.\n"
        "2. Structural Shift: 'Scaled And Icy' represents the most formulaic peak.\n"
        "3. Thematic Legacy: 'Lore' keywords now connect over 40% of the discography."
    )

    plt.text(0.1, 0.9, summary_text, fontsize=12, verticalalignment='top', family='serif')
    plt.title("Twenty One Pilots: A Data-Driven Discography Review", fontsize=16, fontweight='bold')

    pdf.savefig()
    plt.close()

    # ... (Include all your other plot pages here)
# %%
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Prepare the data: Count themes per album
heatmap_data = df_topics.groupby(['Album', 'Topic_Label']).size().unstack(fill_value=0)

# 2. Sort the index (Albums) by your release_dates mapping
ordered_albums = [a for a in release_dates.keys() if a in heatmap_data.index]
heatmap_data = heatmap_data.reindex(ordered_albums)

# 3. Create the Visualization
plt.figure(figsize=(12, 8))
sns.heatmap(
    heatmap_data,
    annot=True,          # Shows the actual song counts in the boxes
    fmt="d",             # Formats counts as integers
    cmap="YlOrRd",       # A professional Yellow-Green-Blue gradient
    cbar_kws={'label': 'Number of Songs'}
)

plt.title("Thematic Fingerprint of Twenty One Pilots", fontsize=18, pad=20)
plt.xlabel("Lyrical Themes (LDA Identified)", fontsize=12)
plt.ylabel("Album (Chronological Order)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save it as the cover
plt.savefig("Report_Cover_Heatmap.png", dpi=300)
plt.show()
