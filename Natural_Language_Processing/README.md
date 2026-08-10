# 📊 CFPB 2025 Consumer Complaint Analysis

## Project Overview
This notebook analyzes the **2025 Consumer Financial Protection Bureau (CFPB) Complaint Database**. It focuses on extracting insights from unstructured consumer narratives to understand the emotional tone (Sentiment) and the urgency (Severity) of financial grievances.

## Key Features
- **Data Cleaning & Normalization**: Standardizes CFPB privacy masks (e.g., `XXXX`), removes web artifacts, and filters out non-meaningful or extremely long narratives.
- **Sentiment Analysis**: Utilizes the **VADER** lexicon to gauge the emotional polarity of complaints.
- **Severity Scoring**: Implements a custom **spaCy-based PhraseMatcher** to categorize complaints into *Critical*, *High*, and *Medium* severity levels based on keywords like 'foreclosure', 'identity theft', and 'billing error'.
- **Geospatial Insights**: Aggregates complaint volume and average severity by State and Territory using Plotly.
- **Linguistic Discovery**: Generates Word Clouds and keyword frequency tables for the top 10 most common complaint issues.

## Data Pipeline
1. **Extraction**: Loads data from CSV (configured for Google Drive).
2. **Preprocessing**: Lowercasing, Lemmatization, and Stopword removal (with custom financial domain exclusions).
3. **Analysis**: sentiment scoring, keyword matching, and correlation analysis between legal risks and financial loss.
4. **Visualization**: Matplotlib heatmaps, Seaborn bar charts, and Plotly interactive maps.

## Dependencies
- `pandas`, `numpy`
- `spacy` (en_core_web_lg)
- `vaderSentiment`
- `wordcloud`
- `plotly`, `seaborn`, `matplotlib`