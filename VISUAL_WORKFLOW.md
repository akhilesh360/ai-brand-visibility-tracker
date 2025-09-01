# AI Brand Visibility Tracker - Visual Process Flow

## Main Workflow (Confluence Style)

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    AI Brand Visibility Tracker                                               │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         ┌─────────────┐
│                 │    │                 │    │                 │    │                 │    🤖   │             │
│  User uploads   │───▶│ AI platforms    │───▶│ Brand mentions  │───▶│ AVS Algorithm   │────────▶│ Dashboard   │
│  mental health  │    │ queried with    │    │ extracted and   │    │ calculates      │         │ shows       │
│  research       │    │ 16 prompts      │    │ analyzed for    │    │ visibility      │         │ insights    │
│  questions      │    │ (ChatGPT,Claude)│    │ placement       │    │ scores          │         │             │
│                 │    │                 │    │                 │    │                 │         │             │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘         └─────────────┘
                                                       │                        │                         │
                                                       ▼                        ▼                         ▼
                                              ┌─────────────────┐    ┌─────────────────┐         ┌─────────────┐
                                              │                 │    │                 │   📊    │             │
                                              │ Citation data   │    │ Based on        │────────▶│ Generate    │
                                              │ collected for   │    │ scoring results │         │ content     │
                                              │ domain trust    │    │                 │         │ strategy    │
                                              │ analysis        │    │                 │         │ briefs      │
                                              │                 │    │                 │         │             │
                                              └─────────────────┘    └─────────────────┘         └─────────────┘
                                                       │                                                  │
                                                       ▼                                                  ▼
                                              ┌─────────────────┐                              ┌─────────────┐
                                              │    ML Engine    │                              │     End     │
                                              │                 │                              │             │
                                              │ TF-IDF + K-Means│                              │             │
                                              │ clusters user   │                              │             │
                                              │ questions by    │                              │             │
                                              │ semantic theme  │                              │             │
                                              │                 │                              │             │
                                              └─────────────────┘                              └─────────────┘
```

## Detailed Process Breakdown

### Phase 1: Data Collection
```
┌─────────────────┐
│   Input Gate    │
│                 │
│ ✓ Mental health │
│   topics ready  │
│ ✓ 16 prompts    │
│   validated     │
│ ✓ Platforms     │
│   accessible    │
└─────────────────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    ChatGPT      │    │     Claude      │    │   Perplexity    │
│                 │    │                 │    │                 │
│ Query: "best    │    │ Query: "best    │    │ Query: "best    │
│ therapy app"    │    │ therapy app"    │    │ therapy app"    │
│                 │    │                 │    │                 │
│ Response stored │    │ Response stored │    │ Response stored │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Phase 2: Analysis Engine
```
┌─────────────────┐
│  Brand Detector │
│                 │
│ Scan response   │
│ for mentions:   │
│ • BetterHelp    │
│ • Talkspace     │──────┐
│ • Headspace     │      │
│ • Cerebral      │      │
│ • Others        │      │
└─────────────────┘      │
                         ▼
                ┌─────────────────┐
                │ Placement       │
                │ Classifier      │
                │                 │
                │ Primary: 1.0x   │
                │ Secondary: 0.6x │
                │ Also: 0.3x      │
                └─────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Sentiment       │
                │ Analyzer        │
                │                 │
                │ Positive: +10%  │
                │ Neutral: 0%     │
                │ Negative: -10%  │
                └─────────────────┘
```

### Phase 3: Scoring Algorithm
```
                    ┌─────────────────────────┐
                    │      AVS Engine         │
                    │                         │
                    │ ┌─────────────────────┐ │
                    │ │   Weight Matrix     │ │
                    │ │                     │ │
                    │ │ 45% Placement       │ │
                    │ │ 30% Citations       │ │
                    │ │ 20% Mention Rate    │ │
                    │ │ 5%  Topic Coverage  │ │
                    │ └─────────────────────┘ │
                    │           │             │
                    │           ▼             │
                    │ ┌─────────────────────┐ │
                    │ │  Final AVS Score    │ │
                    │ │  (0.0 - 1.0 scale)  │ │
                    │ └─────────────────────┘ │
                    └─────────────────────────┘
```

### Phase 4: Machine Learning Insights
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Question      │───▶│    TF-IDF       │───▶│   K-Means       │
│   Collection    │    │  Vectorizer     │    │  Clustering     │
│                 │    │                 │    │                 │
│ "anxiety help"  │    │ Convert to      │    │ Group similar   │
│ "best therapy"  │    │ numerical       │    │ questions into  │
│ "insurance"     │    │ vectors         │    │ themes          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Topic Clusters  │
                                              │                 │
                                              │ 🏥 Therapy      │
                                              │ 💰 Insurance    │
                                              │ 🚨 Crisis       │
                                              │ 📊 Comparison   │
                                              └─────────────────┘
```

### Phase 5: Output Generation
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │  Content Brief  │    │   Strategic     │
│   Dashboard     │    │   Generator     │    │   Intelligence  │
│                 │    │                 │    │                 │
│ • AVS scores    │    │ • SEO strategy  │    │ • Competitor    │
│ • Brand compare │    │ • Topic gaps    │    │   analysis      │
│ • Platform view │    │ • H2 outlines   │    │ • Market share  │
│ • Live demo     │    │ • Target words  │    │ • Opportunities │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     System Integration                          │
└─────────────────────────────────────────────────────────────────┘

Frontend (Streamlit)     Backend (Python)        Data Layer
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│ • Dashboard     │────▶│ • score.py      │────▶│ • prompts.csv   │
│ • Visualizations│     │ • clustering    │     │ • answers.csv   │
│ • User controls │     │ • brief_gen     │     │ • citations.csv │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         ▲                       ▲                       ▲
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   GitHub Repo   │
                    │                 │
                    │ Live Demo URL:  │
                    │ streamlit.app   │
                    └─────────────────┘
```

This Confluence-style workflow provides a clean, professional visualization that matches enterprise documentation standards!
