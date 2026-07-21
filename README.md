# InsightGPT

AI-Powered Decision Intelligence Platform

## Overview

InsightGPT is a full-stack AI analytics platform that lets business users explore sales data using natural language, automated root-cause analysis, AI-generated recommendations, time-series forecasting, and document Q&A — all from a single Streamlit dashboard.

The platform combines:

- Data Engineering & ETL
- Business Intelligence Dashboard
- Natural Language → SQL (Gemini AI)
- AI Root Cause Analysis
- AI Recommendation Engine
- 30-Day Sales Forecasting (Prophet)
- Document Intelligence / RAG (FAISS + HuggingFace + Gemini)

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/InsightGPT.git
cd InsightGPT
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Gemini API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a free key at [https://aistudio.google.com](https://aistudio.google.com)

### 4. Run the app

```bash
streamlit run app.py
```

The database is created automatically on first launch — no setup required.
The app seeds a local SQLite database from `data/raw/SampleSuperstore.csv` (9,994 rows).

---

## Tech Stack

| Layer | Technology |
|---|---|
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
