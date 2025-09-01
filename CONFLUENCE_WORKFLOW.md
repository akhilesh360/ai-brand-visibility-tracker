# AI Brand Visibility Tracker - Confluence Workflow

## Visual Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           AI Brand Visibility Tracker Workflow                                        │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Input    │───▶│  AI Response    │───▶│  Brand Analysis │───▶│  ML Processing  │───▶│   Insights &    │
│                 │    │   Collection    │    │   & Scoring     │    │                 │    │ Recommendations │
│ • Mental health │    │                 │    │                 │    │ • TF-IDF        │    │                 │
│   prompts (16)  │    │ • ChatGPT       │    │ • Placement     │    │ • K-Means       │    │ • AVS Dashboard │
│ • User intent   │    │ • Claude        │    │   detection     │    │ • Clustering    │    │ • Content briefs│
│ • Topics mapped │    │ • Perplexity    │    │ • Sentiment     │    │ • Topic groups  │    │ • Strategy gaps │
│                 │    │ • Manual query  │    │ • Citations     │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                       │                       │                       │
                                ▼                       ▼                       ▼                       ▼
                       ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
                       │    Raw Data     │    │  AVS Algorithm  │    │  Question Map   │    │   Business      │
                       │   Storage       │    │                 │    │                 │    │    Actions      │
                       │                 │    │ 45% placement + │    │ Semantic        │    │                 │
                       │ • answers.csv   │    │ 30% citations + │    │ similarity      │    │ • SEO strategy  │
                       │ • citations.csv │    │ 20% mentions +  │    │ analysis for    │    │ • Content gaps  │
                       │ • prompts.csv   │    │ 5% coverage     │    │ content gaps    │    │ • Competitor    │
                       │                 │    │                 │    │                 │    │   benchmarks    │
                       └─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Process Flow Details

### 1. **Data Input Phase**
```
┌─────────────────┐
│ Prompt Design   │
│                 │
│ • Anxiety       │──┐
│ • Depression    │  │
│ • Therapy       │  │──▶ Real user language mapping
│ • Insurance     │  │    ("best therapy app")
│ • Crisis help   │──┘
└─────────────────┘
```

### 2. **AI Response Collection**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    ChatGPT      │    │     Claude      │    │   Perplexity    │
│                 │    │                 │    │                 │
│ Manual queries  │    │ Manual queries  │    │ Manual queries  │
│ Response capture│────│ Response capture│────│ Response capture│
│ Brand mentions  │    │ Brand mentions  │    │ Brand mentions  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │    Structured Data      │
                    │                         │
                    │ • answer_id             │
                    │ • platform              │
                    │ • primary_brand         │
                    │ • placement             │
                    │ • sentiment             │
                    │ • citation_domains      │
                    └─────────────────────────┘
```

### 3. **Brand Analysis & Scoring**
```
                    ┌─────────────────────────┐
                    │     AVS Calculator      │
                    │                         │
                    │ Weighted Algorithm:     │
                    │ ┌─────────────────────┐ │
                    │ │ 45% Placement Score │ │──┐
                    │ │ 30% Citation Share  │ │  │
                    │ │ 20% Mention Rate    │ │  │──▶ Final AVS Score
                    │ │ 5% Topic Coverage   │ │  │
                    │ └─────────────────────┘ │──┘
                    │                         │
                    │ Sentiment Adjustment:   │
                    │ +10% positive / -10% neg│
                    └─────────────────────────┘
```

### 4. **Machine Learning Processing**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   TF-IDF        │───▶│    K-Means      │───▶│  Topic Clusters │
│ Vectorization   │    │   Clustering    │    │                 │
│                 │    │                 │    │ • Therapy types │
│ Convert questions│    │ Group similar   │    │ • Insurance     │
│ to numerical    │    │ questions by    │    │ • Crisis help   │
│ vectors         │    │ semantic theme  │    │ • Provider comp │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 5. **Insights & Recommendations**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  AVS Dashboard  │    │ Content Briefs  │    │ Strategic Gaps  │
│                 │    │                 │    │                 │
│ • Brand scores  │    │ Auto-generated  │    │ • Competitor    │
│ • Platform comp │────│ SEO strategy    │────│   analysis      │
│ • Topic coverage│    │ • Target topics │    │ • Content       │
│ • Trend analysis│    │ • H2 outlines   │    │   opportunities │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## Decision Points & Logic Gates

```
                            ┌─────────────────┐
                            │  Brand Mentioned│
                            │    in Response? │
                            └─────────┬───────┘
                                     │
                            ┌────────▼────────┐
                            │       YES       │
                            └─────────┬───────┘
                                     │
                            ┌────────▼────────┐
                            │  Primary/       │
                            │  Secondary/     │
                            │  Also mentioned?│
                            └─────┬───┬───┬───┘
                                  │   │   │
                         ┌────────▼┐ ┌▼┐ ┌▼──────────┐
                         │Primary  │ │S │ │Also       │
                         │(1.0x)   │ │e │ │(0.3x)     │
                         └─────────┘ │c │ └───────────┘
                                     │o │
                                     │n │
                                     │d │
                                     │a │
                                     │r │
                                     │y │
                                     │  │
                                     │( │
                                     │0 │
                                     │. │
                                     │6 │
                                     │x │
                                     │) │
                                     └─┘
```

---

## Integration Points

```
┌─────────────────┐    API    ┌─────────────────┐    Export   ┌─────────────────┐
│   Streamlit     │◄─────────│  Python Backend │◄───────────│   Data Sources  │
│   Dashboard     │          │                 │            │                 │
│                 │          │ • score.py      │            │ • CSV files     │
│ • Live demo     │          │ • actions_briefs│            │ • ML models     │
│ • Interactive   │          │ • clustering    │            │ • Algorithms    │
│ • Real-time     │          │                 │            │                 │
└─────────────────┘          └─────────────────┘            └─────────────────┘
```

---

## Success Metrics & KPIs

```
┌─────────────────────────────────────────────────────────────────┐
│                         Success Tracking                        │
├─────────────────┬─────────────────┬─────────────────────────────┤
│  Input Metrics  │ Process Metrics │       Output Metrics        │
├─────────────────┼─────────────────┼─────────────────────────────┤
│ • 16 prompts    │ • AVS accuracy  │ • Brand visibility scores   │
│ • 3 platforms   │ • ML clustering │ • Content gap identification│
│ • 5 brands      │ • Response time │ • Strategic recommendations │
│ • 8 topics      │ • Data quality  │ • Competitive intelligence  │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

This Confluence-style workflow gives you a professional visual representation that's perfect for presentations and documentation!
