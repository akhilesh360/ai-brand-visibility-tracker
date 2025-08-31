import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Import scoring + brief generator
from pipeline.score import compute_scores
from pipeline.actions_briefs import generate_brief

# ---------- Page chrome ----------
st.set_page_config(
    page_title="AI Visibility – Mental Health",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.title("🧠 AI Visibility & Market Insights – Mental Health")
st.caption("Prototype demo: Measure → Diagnose → Recommend → Improve")

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
    merged = answers.merge(
        prompts[["prompt_id", "topic", "text"]],
        on="prompt_id", how="left"
    )
    return answers, citations, prompts, scores, merged

answers, citations, prompts, scores, merged = load_data()

# Fixed brand colors for a polished look
BRAND_COLORS = {
    "BetterHelp": "#2ecc71",   # green
    "Talkspace":  "#1abc9c",   # teal
    "Headspace":  "#e67e22",   # orange
    "Cerebral":   "#9b59b6",   # purple
}

# =====================================================
# 📊 Visibility Scorecard
# =====================================================
st.header("📊 Visibility Scorecard")
st.caption("Overall brand visibility across AI platforms (AVS scoring).")

platform = st.selectbox("AI Platform", sorted(scores["platform"].unique().tolist()))
splt = scores[scores["platform"] == platform]

fig, ax = plt.subplots()
ax.bar(
    splt["brand"],
    splt["AVS"],
    color=[BRAND_COLORS.get(b, "#3498db") for b in splt["brand"]]
)
ax.set_ylabel("AI Visibility Score (AVS)")
ax.set_title(f"AVS by Brand on {platform}")
st.pyplot(fig)

st.dataframe(
    splt[["brand", "placement_score", "citation_share",
          "mention_rate", "topic_coverage", "AVS"]]
    .round(3)
    .reset_index(drop=True)
)

st.divider()

# =====================================================
# 🌐 Where Brands Show Up
# =====================================================
st.header("🌐 Where Brands Show Up")
st.caption("Coverage of each brand across key mental health topics.")

topic_cov = (
    merged.groupby(["topic", "primary_brand"]).size()
    .unstack(fill_value=0)
)
st.dataframe(topic_cov)

st.divider()

# =====================================================
# 🔗 Who AI Trusts
# =====================================================
st.header("🔗 Who AI Trusts")
st.caption("Top domains cited in AI answers — owned vs third-party.")

cit_brand = citations.merge(
    merged[["answer_id", "primary_brand"]],
    on="answer_id", how="left"
)
own = (
    cit_brand.groupby(["primary_brand", "domain"])["domain"].size()
    .rename("count").reset_index()
)
st.dataframe(own.sort_values("count", ascending=False))

st.divider()

# =====================================================
# 💬 AI Conversations Map
# =====================================================
st.header("💬 AI Conversations Map")
st.caption("Clusters of real user questions answered by AI, grouped by theme.")

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(prompts["text"])
k = st.slider("Number of clusters", min_value=3, max_value=8, value=4, step=1)
kmeans = KMeans(n_clusters=k, n_init="auto", random_state=42).fit(X)
prompts["cluster"] = kmeans.labels_

col1, col2 = st.columns([1, 2])
with col1:
    cluster_id = st.selectbox(
        "Cluster",
        sorted(prompts["cluster"].unique().tolist())
    )
with col2:
    st.write("Sample questions in this cluster:")
    st.write(
        prompts[prompts["cluster"] == cluster_id]["text"]
        .head(5).tolist()
    )

cluster_prompts = prompts[prompts["cluster"] == cluster_id]["prompt_id"].tolist()
cluster_answers = merged[merged["prompt_id"].isin(cluster_prompts)]
cluster_scores = (
    cluster_answers.groupby("primary_brand").size()
    / max(1, len(cluster_answers))
).rename("presence").reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(
    cluster_scores["primary_brand"],
    cluster_scores["presence"],
    color=[BRAND_COLORS.get(b, "#3498db") for b in cluster_scores["primary_brand"]]
)
ax2.set_title("Brand presence in selected cluster")
st.pyplot(fig2)

st.divider()

# =====================================================
# ✅ What to Do Next (Content Briefs)
# =====================================================
st.header("✅ What to Do Next (Content Briefs)")
st.caption("Actionable briefs to help brands close AI visibility gaps.")

topic = st.selectbox("Select topic", sorted(merged["topic"].unique().tolist()))
topic_scores = (
    merged[merged["topic"] == topic]
    .merge(
        scores[["platform", "brand", "AVS"]],
        left_on=["platform", "primary_brand"],
        right_on=["platform", "brand"],
        how="left"
    )
)
topic_scores = (
    topic_scores.groupby(["platform", "brand"])["AVS"]
    .mean().reset_index().dropna()
)

if not topic_scores.empty:
    by_platform = topic_scores.groupby("platform")
    for plat, sub in by_platform:
        weakest = sub.sort_values("AVS").iloc[0]
        brief = generate_brief({
            "brand": weakest["brand"],
            "platform": plat,
            "AVS": weakest["AVS"],
            "topic": topic
        })
        with st.expander(f"Suggested brief for {weakest['brand']} on {plat}"):
            st.text(brief)
else:
    st.info("No topic scores available.")
