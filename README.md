# InsightGPT — AI-Powered Business Intelligence Platform

An end-to-end AI analytics and decision intelligence platform that transforms raw sales data into actionable business insights.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Launch_App-2ea44f)](https://insightgpt-hgu3rbo8wpmnabsuabfntn.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75)

## Overview

InsightGPT bridges the gap between traditional business intelligence and generative AI by enabling businesses to analyze performance, identify financial risks, forecast sales and explore business documents through a unified analytics platform.

## Key Business Metrics

| Metric | Value |
|---|---:|
| Records Analyzed | 9,994 |
| Total Revenue | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin | 12.47% |
| Forecasting Horizon | 30 Days |

## Key Features

### 1. Business Intelligence Dashboard
- Interactive KPI dashboard
- Regional and category-wise revenue analysis
- Product-level profitability analysis
- Interactive Plotly visualizations

### 2. Natural Language to SQL
- Converts business questions into SQL queries using Gemini AI
- Executes queries against a SQLite database
- Generates human-readable business interpretations

### 3. AI Root Cause Analysis
- Identifies loss-making product groups
- Analyzes revenue, profit, discounts and sales quantity
- Generates executive-level business insights

### 4. AI Recommendation Engine
- Generates actionable business recommendations
- Identifies pricing and discount optimization opportunities
- Prioritizes potential business interventions

### 5. Predictive Sales Analytics
- Time-series forecasting using Prophet
- 30-day sales predictions
- Interactive forecast charts with uncertainty intervals

### 6. Document Intelligence (RAG)
- PDF document processing
- Semantic information retrieval using FAISS
- AI-powered document question answering
- Retrieval-Augmented Generation

### 7. Executive Report Generation
- Automated business performance summaries
- AI-generated analysis and recommendations
- Downloadable PDF reports

## Technology Stack

| Layer | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite, SQL |
| Visualization | Plotly |
| Application Framework | Streamlit |
| Generative AI | Google Gemini |
| Forecasting | Prophet |
| Document Intelligence | LangChain, FAISS, Hugging Face |
| PDF Processing | PyPDF |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## System Architecture

```text
Raw Sales Dataset
        |
        v
Data Ingestion & ETL (Pandas)
        |
        v
    SQLite Database
        |
        +-- Business Intelligence Dashboard
        |
        +-- Natural Language to SQL
        |
        +-- AI Root Cause Analysis
        |
        +-- AI Business Recommendations
        |
        +-- Revenue Forecasting (Prophet)

PDF Documents
        |
        v
Document Processing (PyPDF)
        |
        v
RAG Pipeline (LangChain + FAISS)
        |
        v
AI Document Intelligence

=========================================
       Streamlit Application
       Google Gemini AI Integration
       Executive PDF Reporting
=========================================
```

## Business Insights

- The West region generates the highest total revenue of approximately $725K.
- Technology is the highest revenue-generating category.
- Tables, Bookcases and Supplies account for approximately $22.4K in combined losses.
- Tables have an average discount rate of 26.13%, suggesting an opportunity to investigate discount and pricing strategies.

## Project Structure

```text
InsightGPT/
├── analytics/
├── dashboard/
├── data/
├── database/
├── forecasting/
├── ingestion/
├── nl_sql/
├── rag/
├── recommendations/
├── reports/
├── root_cause/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Live Application

Explore the deployed application:

[Launch InsightGPT](https://insightgpt-hgu3rbo8wpmnabsuabfntn.streamlit.app/)

## Limitations and Future Improvements

- Improve AI-generated SQL accuracy and validation.
- Strengthen evidence-grounded AI responses.
- Evaluate forecasting performance using MAE and RMSE.
- Improve executive PDF report formatting.
- Expand support for additional business datasets.
- Improve reproducibility of local installation.

## Skills Demonstrated

- Exploratory Data Analysis
- Data Engineering and ETL
- SQL and Database Management
- Business Intelligence
- Data Visualization
- Predictive Analytics
- Generative AI Integration
- Retrieval-Augmented Generation
- Application Deployment

## Author

**Simran Rai**

B.Tech — Computer Science and Engineering

VIT Bhopal University

[GitHub Profile](https://github.com/simdontrun)
| Frontend | Streamlit, Plotly, Tabler Icons |
| AI / LLM | Google Gemini 2.5 Flash Lite |
| Forecasting | Prophet (Meta) |
| RAG | FAISS, HuggingFace Embeddings (all-MiniLM-L6-v2), LangChain |
| Database | SQLite (local, auto-seeded) |
| Data | Pandas, NumPy |
| Language | Python 3.10+ |

---

## Features

### Dashboard
Live KPI cards (Revenue, Profit, Margin) with regional, category, and product breakdown charts. Light/dark theme toggle.

### AI Analytics
Ask any business question in plain English. Gemini generates SQL, the app executes it against the local database, and returns a table plus an AI-written business interpretation.

### Root Cause Analysis
Automatically identifies loss-making product sub-categories, shows supporting evidence (revenue, profit, discount, quantity), and generates an executive-style AI analysis.

### AI Recommendations
Analyses the same loss-making products and produces up to 5 prioritised, actionable recommendations from a senior consultant persona.

### Forecast Center
Fits a Prophet model on historical sales data and plots a 30-day forward forecast with confidence intervals. Includes a downloadable CSV of the forecast.

### Document Intelligence
Upload any business PDF. The app chunks it, builds a FAISS vector index, retrieves relevant passages, and uses Gemini to answer your questions — grounded strictly in the document.

---

## Dataset

**Sample Superstore** — 9,994 orders across US regions, product categories, and customer segments.

Source: Tableau Sample Superstore (widely used public business intelligence dataset).

---

## Project Structure

```
InsightGPT/
├── app.py                  # Main Streamlit entry point
├── analytics/              # KPI, region, category, product services
├── database/               # SQLite loader (auto-seeds on first run)
├── forecasting/            # Prophet forecast engine
├── ingestion/              # Data validation and cleaning pipeline
├── nl_sql/                 # NL→SQL generation, validation, execution
├── rag/                    # PDF loader, FAISS vector store, RAG engine
├── recommendations/        # Risk analyser + Gemini recommendation engine
├── root_cause/             # Loss product queries + AI evidence explainer
├── data/
│   ├── raw/                # SampleSuperstore.csv (source of truth)
│   ├── cleaned/            # Cleaned sales CSV, forecast CSV
│   └── documents/          # Sample quarterly report PDF
└── dashboard/              # Legacy dashboard (superseded by app.py)
```

---

## Dataset Verification

- Source CSV rows: 9,994
- SQLite rows after seed: 9,994
