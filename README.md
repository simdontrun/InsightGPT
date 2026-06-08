# InsightGPT

An AI-powered business intelligence platform that transforms raw sales data into actionable insights using Azure SQL, analytics, and LLM-powered explanations.

## Project Overview

InsightGPT is designed to help business users interact with sales data through intelligent analytics and natural language insights.

The platform performs:

- Data Extraction from CSV datasets
- Data Validation and Quality Checks
- Data Cleaning and Transformation
- Data Loading into Azure SQL Database
- Analytics and KPI Generation
- AI-Powered Business Insights (Upcoming)

---

## ETL Pipeline

### Extract

- Loaded Superstore sales dataset using Pandas

### Transform

- Performed data validation checks
- Cleaned and standardized dataset columns
- Handled data quality issues

### Load

- Connected Python application to Azure SQL Database
- Created database tables automatically
- Loaded processed data into Azure SQL
- Verified successful data ingestion

---

## Current Progress

### Completed

- [x] Project Setup
- [x] ETL Pipeline
- [x] Azure SQL Integration
- [x] Data Validation Layer
- [x] Data Cleaning Layer

### In Progress

- [ ] Analytics Engine
- [ ] KPI Generation
- [ ] AI Insights Layer
- [ ] Interactive Dashboard

---

## Tech Stack

### Data Engineering

- Python
- Pandas
- PyODBC

### Cloud

- Azure SQL Database

### Database

- SQL Server

### Development Tools

- VS Code
- Git
- GitHub

---

## Project Structure

```text
InsightGPT/
│
├── data/
├── database/
├── validators/
├── transformers/
├── reports/
├── test_db.py
├── requirements.txt
└── README.md
```

---

## Next Steps

- Build analytics layer
- Generate business KPIs
- Integrate AI-powered insights
- Develop interactive dashboard