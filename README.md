# AI Brand Visibility Tracker - Mental Health Analytics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Measure → Diagnose → Recommend → Improve**

A comprehensive analytics platform that measures brand visibility across AI platforms in the mental health sector. This tool provides actionable insights for brands to optimize their presence in AI-generated content and recommendations.

## 🚀 Features

### 📊 AI Visibility Scorecard
- **AI Visibility Score (AVS)** - Proprietary scoring algorithm
- Platform-specific brand performance metrics
- Placement score analysis and citation share tracking
- Topic coverage and mention rate analytics

### 🌐 Brand Coverage Analysis
- Cross-platform brand presence mapping
- Mental health topic coverage assessment
- Competitive positioning insights

### 🔗 Authority & Trust Metrics
- Domain citation analysis (owned vs. third-party)
- AI platform trust indicators
- Source credibility tracking

### 💬 AI Conversation Intelligence
- Real user question clustering and analysis
- Topic-based conversation mapping
- Brand presence in specific conversation themes

### ✅ Actionable Content Briefs
- AI-generated content recommendations
- Gap analysis and improvement strategies
- Platform-specific optimization suggestions

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Interactive Dashboard)
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (TF-IDF, K-Means)
- **Visualization**: Matplotlib
- **Data Storage**: CSV, YAML

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akhilesh360/ai-brand-visibility-tracker.git
   cd ai-brand-visibility-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas matplotlib scikit-learn pathlib
   ```

## 🚀 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run app/streamlit_app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Explore the dashboard** through different sections:
   - View visibility scorecards by platform
   - Analyze brand coverage across topics
   - Review citation and trust metrics
   - Generate actionable content briefs

## 📁 Project Structure

```
ai-brand-visibility-tracker/
├── app/
│   └── streamlit_app.py          # Main dashboard application
├── data/
│   ├── brands.yaml               # Brand configuration
│   ├── platforms.yaml            # AI platform definitions
│   ├── topics.yaml               # Mental health topics
│   ├── prompts.csv               # User question dataset
│   └── sample_run/
│       ├── answers.csv           # AI responses data
│       ├── citations.csv         # Citation tracking
│       └── runs.csv              # Execution logs
├── pipeline/
│   ├── __init__.py
│   ├── score.py                  # AVS calculation engine
│   └── actions_briefs.py         # Content brief generator
├── .gitignore
└── README.md
```

## 🎯 Key Metrics & Algorithms

### AI Visibility Score (AVS)
Our proprietary scoring algorithm combines:
- **Placement Score**: Position and prominence in AI responses
- **Citation Share**: Percentage of citations received
- **Mention Rate**: Frequency of brand mentions
- **Topic Coverage**: Breadth across mental health topics

### Conversation Intelligence
- **TF-IDF Vectorization**: For semantic question analysis
- **K-Means Clustering**: Grouping similar user queries
- **Topic Modeling**: Identifying conversation themes

## 📊 Sample Analytics

The platform provides insights across multiple dimensions:

- **Brand Performance**: Track how brands perform across different AI platforms
- **Topic Analysis**: Understand which mental health topics drive visibility
- **Competitive Intelligence**: Compare brand presence against competitors
- **Content Optimization**: Receive AI-generated briefs for improvement

## 🔮 Future Enhancements

- [ ] Real-time data integration with AI platforms
- [ ] Advanced sentiment analysis
- [ ] Automated content generation
- [ ] API integration for external data sources
- [ ] Enhanced machine learning models
- [ ] Custom dashboard themes
- [ ] Export functionality for reports

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sai Akhilesh Veldi**
- GitHub: [@akhilesh360](https://github.com/akhilesh360)
- LinkedIn: [saiakhileshveldi](https://www.linkedin.com/in/saiakhileshveldi/)

## 🙏 Acknowledgments

- Mental health organizations for providing domain expertise
- Open-source community for tools and libraries
- Streamlit team for the amazing framework
- AI platforms for data accessibility

---

**Made with ❤️ for better mental health AI visibility**
