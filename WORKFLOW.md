# AI Brand Visibility Tracker - Technical Workflow

## 🔄 **Complete System Architecture**

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI BRAND VISIBILITY TRACKER                  │
│                     Mental Health Analytics                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DATA INPUT    │───▶│   PROCESSING    │───▶│    INSIGHTS     │
│                 │    │                 │    │                 │
│ • Prompts       │    │ • Scoring       │    │ • Dashboard     │
│ • AI Responses  │    │ • ML Analysis   │    │ • Briefs        │
│ • Citations     │    │ • Clustering    │    │ • Recommendations│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 📋 **Step-by-Step Workflow**

### **Phase 1: Data Collection & Preparation**
```
1. PROMPT DESIGN
   ├── Mental health topics (anxiety, depression, therapy)
   ├── User intent mapping (awareness → purchase)
   └── Real user language ("best therapy app", "BetterHelp vs Talkspace")

2. AI PLATFORM TESTING
   ├── Manual queries to ChatGPT, Claude, Perplexity
   ├── Response collection with metadata
   └── Brand mention identification

3. DATA STORAGE
   ├── prompts.csv (16 curated questions)
   ├── answers.csv (AI responses with brand mentions)
   └── citations.csv (domain references and trust signals)
```

### **Phase 2: Algorithm Processing**
```
4. BRAND ANALYSIS (score.py)
   ├── Placement Detection: Primary/Secondary/Also-mentioned
   ├── Sentiment Analysis: Positive/Neutral/Negative
   ├── Citation Tracking: Owned vs Third-party domains
   └── Topic Coverage: Breadth across mental health categories

5. AVS CALCULATION
   ├── Weighted Formula: 45% placement + 30% citations + 20% mentions + 5% coverage
   ├── Sentiment Adjustment: ±10% based on positive/negative context
   └── Platform Comparison: Cross-platform performance matrix
```

### **Phase 3: Machine Learning Insights**
```
6. QUESTION CLUSTERING
   ├── TF-IDF Vectorization of user prompts
   ├── K-Means clustering by semantic similarity
   └── Theme identification (therapy, crisis, insurance, etc.)

7. COMPETITIVE ANALYSIS
   ├── Brand performance benchmarking
   ├── Market share estimation by topic
   └── Gap identification for content strategy
```

### **Phase 4: Strategic Recommendations**
```
8. CONTENT BRIEF GENERATION (actions_briefs.py)
   ├── Template-based brief creation
   ├── SEO optimization recommendations
   ├── Target keyword identification
   └── Content outline with medical compliance

9. DASHBOARD VISUALIZATION
   ├── Real-time AVS scoring display
   ├── Interactive brand comparison charts
   ├── Topic coverage heatmaps
   └── Citation source analysis
```

---

## 🎯 **Key Technical Components**

### **Core Algorithm (AVS Score)**
```python
# AI Visibility Score Calculation
placement_weight = {"primary": 1.0, "secondary": 0.6, "also": 0.3}
sentiment_multiplier = {"positive": 1.1, "neutral": 1.0, "negative": 0.9}

AVS = (0.45 * placement_score + 
       0.30 * citation_share + 
       0.20 * mention_rate + 
       0.05 * topic_coverage) * sentiment_adjustment
```

### **Machine Learning Pipeline**
```python
# Question Clustering for Content Gaps
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(prompts["text"])
kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
```

### **Content Strategy Automation**
```python
# Automated Brief Generation
BRIEF_TEMPLATE = """
Brand: {brand}
Gap: {topic} on {platform} (AVS {score})
Target: Evidence-based {topic} content
Strategy: Improve placement from {current} to primary mention
Expected Impact: +0.08 AVS, +20% citation share
"""
```

---

## 📊 **Data Flow Architecture**

```
INPUT DATA                  PROCESSING LAYER              OUTPUT INSIGHTS
───────────                 ────────────────              ───────────────

prompts.csv                 ┌─────────────────┐           Streamlit Dashboard
├─ prompt_id               │   score.py      │           ├─ AVS Scorecard
├─ text                    │   - Placement   │           ├─ Brand Comparison
├─ topic                   │   - Citations   │           ├─ Topic Coverage
└─ intent                  │   - Sentiment   │           └─ Action Briefs
                           │   - Coverage    │
answers.csv                 └─────────────────┘           Strategic Recommendations
├─ answer_id                        │                     ├─ Content Gaps
├─ platform                         ▼                     ├─ SEO Opportunities
├─ primary_brand            ┌─────────────────┐           └─ Competitive Intel
├─ placement               │ actions_briefs. │
├─ sentiment               │       py        │           ML Insights
└─ raw_text                │ - Template      │           ├─ Question Clusters
                           │ - Strategy      │           ├─ User Intent Map
citations.csv              │ - Briefs       │           └─ Market Trends
├─ domain                  └─────────────────┘
├─ is_owned_domain                  │
└─ answer_id                        ▼
                           
                           Live Demo Output
                           ├─ Real-time Analytics
                           ├─ Interactive Visualizations
                           └─ Exportable Reports
```

---

## 🚀 **Business Value Demonstration**

### **Problem → Solution → Impact**
```
PROBLEM: Mental health brands don't know how they perform in AI search
    ↓
SOLUTION: Proprietary AVS scoring across ChatGPT, Claude, Perplexity
    ↓
IMPACT: Actionable content strategy to improve AI visibility
```

### **Competitive Advantage**
- **Vertical Focus**: Mental health specialization vs generic tools
- **Proprietary Algorithm**: Custom AVS scoring methodology  
- **End-to-End Pipeline**: From data collection to strategic recommendations
- **Live Demonstration**: Working prototype with real data

---

## 💡 **Interview Talking Points**

### **Technical Depth**
1. **"I reverse-engineered the AI visibility market"** - Built working competitor to Profound
2. **"Created proprietary scoring algorithm"** - AVS methodology with weighted factors
3. **"Implemented full ML pipeline"** - TF-IDF clustering for content strategy
4. **"Deployed live demo"** - Streamlit Cloud with real-time analytics

### **Business Understanding**
1. **"Chose strategic vertical"** - Mental health vs generic brand tracking
2. **"Built scalable architecture"** - Modular pipeline for easy expansion
3. **"Generated actionable insights"** - Not just analytics, but strategic recommendations
4. **"Demonstrated market validation"** - Working prototype proves concept viability

### **Next Steps for Scale**
1. **API Integration**: Automate AI platform querying
2. **Real-time Processing**: Live data ingestion and analysis
3. **Enterprise Features**: User management, compliance, reporting
4. **Healthcare Compliance**: HIPAA, medical content validation
