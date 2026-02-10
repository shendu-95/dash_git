# Live Global Indicator Dashboard (Python + Power BI)

## Overview
This project demonstrates an end-to-end analytics pipeline that integrates **live API data** with **Power BI** to create an interactive dashboard for analyzing global socio-economic and health indicators.

The data is sourced from the **World Bank public API** and processed using **Python**, eliminating reliance on static CSV files and enabling automated, refreshable data workflows.

---

## Business Problem
Policymakers, analysts, and researchers often rely on fragmented and outdated datasets to understand global trends in health, economy, technology adoption, and poverty reduction.

This project addresses that challenge by providing a unified, data-driven dashboard that enables:
- Cross-country and regional comparisons
- Trend analysis over time
- Exploration of relationships between economic, technological, and health indicators

---

## Key Objectives
- Establish baseline economic and social metrics across countries
- Compare health spending patterns across world regions
- Analyze trends in key indicators such as GDP, unemployment, internet usage, and renewable energy
- Evaluate the impact of internet access on immunization and unemployment
- Identify top- and bottom-performing countries in poverty reduction
- Examine correlations among major health indicators
- Analyze the relationship between health expenditure and life expectancy

---

## Data Pipeline
1. **API Ingestion (Python)**
   - Data fetched from the World Bank API using `requests`
   - Multiple indicator categories (health, economy, trade, labor, environment, technology)
   - Pagination and rate-limiting handled programmatically

2. **Data Processing**
   - API responses normalized into tabular format using `pandas`
   - Country metadata merged for regional and income-level analysis
   - Modular Python functions created for each indicator category

3. **Power BI Integration**
   - Python functions exposed as Power BI data sources
   - Power Query used to apply schema-safe transformations
   - Conditional logic implemented to support both CSV and API-based data sources
   - Interactive visuals built using Power BI

---

## Dashboard Features
- KPI cards for high-level global metrics
- Regional comparison of health expenditure
- Time-series analysis of key socio-economic indicators
- Scatter plots with trend lines for relationship analysis
- Correlation heatmaps across health indicators
- Top and bottom country rankings for poverty reduction
- Region and country-level filters for interactive exploration

---

## Technologies Used
- **Python** (pandas, requests)
- **World Bank API**
- **Power BI**
- **Power Query (M language)**

---

## Notes
- The Power BI report uses Python as a data source.
- The dashboard can be refreshed locally or via Power BI Service with a configured gateway.
- All data used in this project is publicly available.

---

## Preview
![Dashboard Preview](screenshots/dashboard_overview.png)
