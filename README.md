
Ethiopia Financial Inclusion Forecasting System

Project Lead: Hermela Angaw | Firm: Selam Analytics
Objective: Track and forecast Ethiopia's digital financial transformation (2011–2027) using event-augmented time series methods.

🚀 Project Overview

This repository contains a complete forecasting pipeline designed for a consortium of stakeholders (NBE, DFIs, and Mobile Operators). It addresses the "structural plateau" in Ethiopia's financial inclusion by modeling the impacts of infrastructure enablers (electricity, data cost) and market events (Telebirr, M-Pesa).

Key Features

Data Enrichment: Integrated IMF, World Bank, and GSMA data to bridge gaps in the Findex surveys.

Event-Impact Modeling: A custom Association Matrix to quantify how product launches and policies move inclusion metrics.

Scenario Forecasting: 2025–2027 projections across Optimistic, Base, and Pessimistic scenarios.

Interactive Dashboard: A Streamlit-based delivery tool for stakeholder decision-making.

🛠 Environment Setup

To reproduce the analysis and run the dashboard locally:

code
Bash
download
content_copy
expand_less
# 1. Clone the repository
git clone <your-repo-url>
cd ethiopia-fi-forecast

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install required libraries
pip install -r requirements.txt
📂 Project Structure
code
Text
download
content_copy
expand_less
ethiopia-fi-forecast/
├── data/
│   ├── raw/           # Original starter dataset and reference codes
│   └── processed/     # Enriched and cleaned data ready for modeling
├── notebooks/         # Step-by-step EDA, Modeling, and Forecasting
├── src/               # Python modules for data processing
├── dashboard/
│   └── app.py         # Streamlit Dashboard application
├── reports/
│   ├── figures/       # Generated charts and dashboard screenshots
│   └── final_report.md # Comprehensive final analysis (blog-post style)
├── requirements.txt   # List of all project dependencies
└── README.md          # Project documentation
📊 The Unified Data Schema

This project utilizes a Unified Schema where all records share a common column structure to ensure unbiased modeling:

record_type: Defines the row as an observation (metric), event (milestone), target (policy goal), or impact_link (modeled relationship).

pillar: Categorizes data into ACCESS, USAGE, INFRASTRUCTURE, or AFFORDABILITY.

indicator_code: Unique identifiers for metrics (e.g., ACC_OWNERSHIP, ATM_COUNT).

parent_id: Links impact_link records to their specific event for matrix calculation.

🚦 How to Run
1. Data Exploration & Modeling

Open the Jupyter notebooks in the notebooks/ directory in order:

exploration.ipynb: EDA and 2021-2024 slowdown analysis.

impact_modeling.ipynb: Creation of the Event-Indicator Association Matrix.

forecasting.ipynb: Generation of the 2027 scenarios and confidence intervals.

2. Interactive Dashboard

Run the following command to launch the Streamlit app:

code
Bash
download
content_copy
expand_less
streamlit run dashboard/app.py
📈 Methodology

Due to the sparse nature of Global Findex data (5 points over 13 years), we employed an Event-Augmented Trend Model. This approach combines a historical linear trend with quantitative "impact coefficients" derived from comparable country evidence and historical validation (e.g., the Telebirr launch).

🔗 Data Sources

World Bank Global Findex: Primary inclusion indicators.

IMF Financial Access Survey: ATM and physical infrastructure data.

GSMA Intelligence: Mobile connectivity and internet usage.

A4AI: Mobile data affordability benchmarks.

