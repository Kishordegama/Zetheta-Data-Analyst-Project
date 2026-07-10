# 📊 Zetheta Project 1A – Loan Portfolio Risk Analysis

## 📌 Project Overview
This project focuses on analyzing a vehicle loan securitization dataset to identify loan risk categories, loss patterns, recovery trends, and servicer performance. The analysis was performed using Python, Pandas, and Matplotlib to generate meaningful business insights for portfolio monitoring and risk management.

---

## 🎯 Objectives
The primary objectives of this project are:
* Analyze loan portfolio data.
* Perform Loss Analysis and Recovery Analysis.
* Design a basic Star Schema for reporting.
* Build a Risk Scoring Model based on delinquency data.
* Generate business insights for decision-making.
* Prepare the dataset for future Business Intelligence and Machine Learning applications.

---

## 🛠️ Tools & Technologies Used
* **Python** (Core Data Analytics)
* **Pandas** (Data Cleaning & Wrangling)
* **Matplotlib & NumPy** (Visualizations & Logic)
* **VS Code** (Development Environment)
* **CSV Dataset** (Securitization Source Data)

---

## 📂 Dataset Information
The dataset contains loan securitization information including:
* Loan Details & Borrower Information
* Servicer Information & Delinquency (DPD) Data
* Loss Amount & Recovery Amount Data
* Insurance Information

---

## ⚙️ Data Loading & Preparation
The dataset was loaded using Pandas and cleaned before analysis.

### Python Code Snippet
```python
import pandas as pd
df = pd.read_csv("Data/data.csv")

Data Cleaning Steps
Missing values replaced with 0 where required.

Numeric columns converted to proper data types.

Relevant columns selected for analysis.

Data validated before calculations.

📉 Financial Analysis & Insights
1. Loss Analysis
Objective: Identify which servicers have the highest average loan loss amount.

Methodology: Grouped records by ServicerName, calculated average LossAmount, and ranked them.

Key Observation: ICICI Auto Loans recorded the highest average loss amount among all servicers.

2. Recovery AnalysisObjective:

 Evaluate recovery performance across different servicers.Results Matrix:
   Servicer                Average Recovery   
ICICI Auto Loans            2418.23
Bajaj Finance Aut           0.00
HDFC Bank Auto Finance      0.00

Key Observation: ICICI Auto Loans demonstrated the highest recovery amount.

3. Net Loss Analysis

Formula: NetLoss = LossAmount - RecoveryAmount
Results Matrix:
Servicer             Average Net Loss
ICICI Auto Loans          5359.99
Bajaj Finance Auto        0.00
HDFC Bank Auto Finance    0.00

Key Observation: ICICI Auto Loans recorded the highest average net loss among all servicers.

Star Schema Design
A simple Star Schema was created to support analytical reporting and BI integration.
 Fact Table: Contains measurable business metrics (LoanID, LossAmount, RecoveryAmount, NetLoss).
Dimension Table – Servicer: Contains descriptive attributes (ServicerID, ServicerName).


Risk Scoring Model
A rule-based Risk Scoring Model was implemented using DPD (Days Past Due).
Risk Classification Rules
 0 DPD: Low Risk
 1–30 DPD: Medium Risk
 Above 30 DPD: High Risk

Risk Analysis Distribution Results
Servicer                 Low Risk        Medium Risk     High Risk
Bajaj Finance Auto         145              35              0
HDFC Bank Auto Finance     137              19              0
ICICI Auto Loans           133              31              0

Key Findings: Majority of loans belong to the Low Risk category. No High Risk loans were identified, indicating healthy portfolio credit quality.

Future Improvements
Machine Learning Models for Default Probability Prediction.
Power BI/Dashboard Development for Recovery Trend Monitoring.
Real-time Automated Risk Alerts.

Author
Kishor Degama
Aspiring Data Analyst
Skills: Python | SQL | Power BI | Financial Risk Analytics | Data Modeling
