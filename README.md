# breach_lab
Projects and Blog posts

---
layout: home
---

A great data report always starts with an executive summary. This translates the cold numbers—like "0.15 Rhyme Density"—into a story about artistic growth.

You can paste this "Summary of Findings" at the very beginning of your PDF or include it as a text block on the first page.

### Summary of Findings: The Lyrical Evolution of Twenty One Pilots

This analysis of **92 songs** across **10 albums** reveals a band in a state of constant technical and thematic transition. Early eras, specifically the *Self-Titled* and *Vessel* periods, are characterized by high **Lexical Diversity** and overt **Faith & Resilience** themes, suggesting a raw, introspective focus on identity and spiritual struggle. As the discography progresses into the *Trench* and *Clancy* eras, we observe a significant spike in **Rhyme Density**, indicating a shift toward more complex, technical rapping and world-building "Lore."

While later albums like *Scaled And Icy* show a higher **Repetition Score** (suggesting a move toward more structured, formulaic pop compositions), the **Sentiment Analysis** reveals a "U-shaped" emotional journey: starting with heavy introspection, moving into dark narrative conflict, and eventually rebounding toward a resilient, albeit complex, optimism. Ultimately, the data suggests that while the band's structural complexity varies by era, their technical proficiency and thematic depth have consistently deepened over the last 15 years.

---


Instant Insight: You can see "hot spots." For example, if Topic 0 (Faith) has high numbers in 2009 but zeros in 2021, the story of the band's evolution is immediately visible.

Professionalism: Heatmaps are standard in academic and corporate data reporting.

Completeness: It accounts for every single song in the 92-item list without being overwhelming.

Final Project Checklist
PDF Report, your Lore Network, your Rhyme Density Line Chart, and your Cover Heatmap, a fan-data project.

This project achieved:

Calculated technical rapping metrics using phonetics.

Analyzed song structure using Zlib compression logic.

Visualized 15 years of artistic growth chronologically.

Mapped a complex lore-based narrative using network theory.

---


A **Technical Methodology** section is crucial for your project. It proves that your findings aren't just opinions—they are the result of rigorous data science. It explains to your audience exactly how you turned raw lyrics into measurable data.

### Technical Methodology: Lyrical Analysis & Topic Modeling

#### 1. Data Acquisition and Preprocessing

The dataset consists of **92 songs** spanning 10 albums. Raw lyrics were cleaned using **Regex** to remove non-alphanumeric characters and structural metadata. Text was tokenized and filtered against a customized **Stop-Word list** that excluded common English "filler" words as well as music-specific terms (e.g., *Chorus, Verse*).

#### 2. Latent Dirichlet Allocation (LDA)

Thematic clusters were identified using **Gensim’s LDA algorithm**. The model was trained over 15 passes using a Bag-of-Words corpus. This statistical approach identifies groups of words that frequently co-occur, allowing the model to "discover" themes like *Lore*, *Faith*, and *Internal Struggle* without human bias.

#### 3. Phonetic and Structural Metrics

* **Rhyme Density:** Calculated using the **CMU Pronouncing Dictionary** via the `pronouncing` library. The algorithm scans a 10-word "look-ahead" window for phonetic matches, calculating the ratio of rhyming words to total word count.
* **Structural Repetition:** Measured using **Zlib Compression**. By comparing the byte-size of raw lyrics to their compressed version, we established a "Repetition Score." Highly formulaic songs compress more efficiently, while experimental, through-composed songs retain a larger file size.

#### 4. Sentiment and Graph Analysis

* **Sentiment:** Derived using **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, which is specifically tuned for social media and song lyrics.
* **Networking:** The "Lore Connector" graph was built using **NetworkX**, where edges represent shared low-frequency "Lore" keywords between tracks.

---

### Final Project Wrap-Up

This project successfully built a full-stack data analysis pipeline. It handled everything from a `NameError` to complex `NetworkX` graphs.

