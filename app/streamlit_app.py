import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.score import compute_scores
from pipeline.actions_briefs import generate_brief

st.set_page_config(
    page_title="AI Brand Visibility Tracker",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("AI Brand Visibility Tracker - Mental Health Analytics")
st.caption("Measure → Diagnose → Recommend → Improve")

# Data paths
DATA_DIR = Path("data")
ANS = DATA_DIR / "sample_run" / "answers.csv"
CIT = DATA_DIR / "sample_run" / "citations.csv"  
PRM = DATA_DIR / "prompts.csv"

@st.cache_data
def load_data():
    answers = pd.read_csv(ANS)
    citations = pd.read_csv(CIT)
    prompts = pd.read_csv(PRM)
    scores = compute_scores(str(ANS), str(CIT), str(PRM))
    merged = answers.merge(prompts[["prompt_id", "topic", "text"]], on="prompt_id", how="left")
    return answers, citations, prompts, scores, merged

answers, citations, prompts, scores, merged = load_data()

# Brand color scheme
BRAND_COLORS = {
    "BetterHelp": "#2ecc71",
    "Talkspace": "#1abc9c", 
    "Headspace": "#e67e22",
    "Cerebral": "#9b59b6",
}

# AVS Scorecard
st.header("AVS Scorecard")
st.caption("Brand performance across AI platforms using our proprietary scoring algorithm")

platform = st.selectbox("Select Platform", sorted(scores["platform"].unique()))
platform_data = scores[scores["platform"] == platform]

fig, ax = plt.subplots(figsize=(4, 4))
bars = ax.bar(platform_data["brand"], platform_data["AVS"], 
              color=[BRAND_COLORS.get(b, "#3498db") for b in platform_data["brand"]])
ax.set_ylabel("AI Visibility Score")
ax.set_title(f"Brand Performance on {platform}")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Show detailed scores
st.dataframe(platform_data[["brand", "placement_score", "citation_share", 
                           "mention_rate", "topic_coverage", "AVS"]].round(3))

st.divider()

# Topic Coverage Analysis
st.header("Topic Coverage Map")
st.caption("Which brands dominate specific mental health topics")

topic_coverage = merged.groupby(["topic", "primary_brand"]).size().unstack(fill_value=0)
st.dataframe(topic_coverage)

st.divider()

# Citation Analysis  
st.header("Citation Analysis")
st.caption("Domains that AI platforms trust and cite most frequently")

citation_data = citations.merge(merged[["answer_id", "primary_brand"]], on="answer_id", how="left")
domain_counts = citation_data.groupby(["primary_brand", "domain"]).size().reset_index(name="citations")
st.dataframe(domain_counts.sort_values("citations", ascending=False))

st.divider()

# Question Clustering
st.header("Question Analysis")
st.caption("ML clustering of user questions to identify content themes")

# TF-IDF clustering
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(prompts["text"])

num_clusters = st.slider("Number of clusters", min_value=3, max_value=8, value=4)
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(tfidf_matrix)
prompts["cluster"] = cluster_labels

col1, col2 = st.columns([1, 2])
with col1:
    selected_cluster = st.selectbox("Select Cluster", sorted(prompts["cluster"].unique()))

with col2:
    st.write("**Sample questions in this cluster:**")
    cluster_questions = prompts[prompts["cluster"] == selected_cluster]["text"].head(5)
    for q in cluster_questions:
        st.write(f"- {q}")

# Brand performance in selected cluster
cluster_prompt_ids = prompts[prompts["cluster"] == selected_cluster]["prompt_id"]
cluster_data = merged[merged["prompt_id"].isin(cluster_prompt_ids)]

if len(cluster_data) > 0:
    brand_presence = cluster_data.groupby("primary_brand").size() / len(cluster_data)
    
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.bar(brand_presence.index, brand_presence.values,
            color=[BRAND_COLORS.get(b, "#3498db") for b in brand_presence.index])
    ax2.set_title(f"Brand Presence in Cluster {selected_cluster}")
    ax2.set_ylabel("Presence Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)

st.divider()

# Content Strategy Recommendations
st.header("Content Strategy Briefs")
st.caption("AI-powered recommendations to improve brand visibility")

selected_topic = st.selectbox("Select Topic", sorted(merged["topic"].unique()))

# Get scores for selected topic
topic_data = merged[merged["topic"] == selected_topic]
topic_scores = topic_data.merge(
    scores[["platform", "brand", "AVS"]], 
    left_on=["platform", "primary_brand"], 
    right_on=["platform", "brand"], 
    how="left"
).dropna()

if len(topic_scores) > 0:
    avg_scores = topic_scores.groupby(["platform", "brand"])["AVS"].mean().reset_index()
    
    for platform in avg_scores["platform"].unique():
        platform_scores = avg_scores[avg_scores["platform"] == platform]
        if len(platform_scores) > 0:
            lowest_performer = platform_scores.loc[platform_scores["AVS"].idxmin()]
            
            brief_params = {
                "brand": lowest_performer["brand"],
                "platform": platform,
                "AVS": lowest_performer["AVS"],
                "topic": selected_topic
            }
            
            brief = generate_brief(brief_params)
            
            with st.expander(f"Strategy Brief: {lowest_performer['brand']} on {platform}"):
                st.text(brief)
else:
    st.info("No data available for this topic.")
