# 🏥 CareLens AI
### AI-Powered Healthcare Analytics & Business Intelligence Platform

### See healthcare data through an intelligent lens.

---

## 📌 Project Overview
CareLens AI is an end-to-end healthcare analytics platform designed to transform complex healthcare data into meaningful business insights.

The project combines cloud data warehousing, SQL analytics, Python, Business Intelligence, and Generative AI into a single analytical ecosystem.

Users can explore healthcare data through interactive Power BI dashboards and interact with the data using Natural Language through an AI-powered Streamlit application.

🔄 The journey

📂 Healthcare Data -> ❄️ Snowflake -> 🧮 SQL / SnowSQL -> 🧹 Data Cleaning & Transformation -> 📊 Power BI Analytics -> 🤖 AI / LLM Layer -> 🎈 Streamlit Application -> 💡 Actionable Healthcare Insights

---

## 🎯 Project Goals

The main objectives of this project are:

* Analyze healthcare encounters, patients, procedures, organizations, and payers.
* Build a centralized analytical environment using **Snowflake**.
* Perform data exploration and transformation using **SQL**.
* Create meaningful healthcare KPIs and business insights.
* Build interactive dashboards using **Power BI**.
* Add an **AI-powered Natural Language interface** for healthcare data.
* Allow users to upload healthcare datasets and ask questions in plain English.
* Develop an interactive **Streamlit web application**.
* Demonstrate an end-to-end modern **Data Analytics + AI workflow**.

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │   Healthcare Data    │
                    │      CSV / Data      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Snowflake       │
                    │   Data Warehouse     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       SnowSQL        │
                    │  SQL Transformation  │
                    │    & Analysis       │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
       ┌─────────────────────┐   ┌─────────────────────┐
       │      Power BI       │   │       Python        │
       │ Interactive         │   │ Data Analysis &     │
       │ Dashboards          │   │ Processing          │
       └──────────┬──────────┘   └──────────┬──────────┘
                  │                         │
                  │                         ▼
                  │                ┌────────────────────┐
                  │                │     OpenRouter     │
                  │                │    AI / LLM Layer  │
                  │                └──────────┬─────────┘
                  │                           │
                  └────────────┬──────────────┘
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │   AI Healthcare App  │
                    └──────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology          | Purpose                                                            |
| ------------------- | ------------------------------------------------------------------ |
| ❄️ **Snowflake**    | Cloud data warehouse for storing and managing healthcare data      |
| 🖥️ **SnowSQL**     | SQL-based interaction and analysis with Snowflake                  |
| 🗄️ **SQL**         | Data exploration, transformation, aggregation and KPI calculations |
| 📊 **Power BI**     | Interactive dashboards and healthcare data visualization           |
| 🐍 **Python**       | Data processing, analysis and application development              |
| 🎈 **Streamlit**    | Interactive web application development                            |
| 🤖 **OpenRouter**   | AI/LLM integration for Natural Language analytics                  |
| 🐼 **Pandas**       | Data manipulation and processing                                   |
| 🔢 **NumPy**        | Numerical analysis                                                 |
| 📈 **Matplotlib**   | Data visualization and exploratory analysis                        |
| 🔧 **Git & GitHub** | Version control and project management                             |

---

# 🗃️ Dataset Structure

The healthcare database contains multiple interconnected tables.

### 1. Patients

Contains information related to patients and their demographics.

Example information:

* Patient ID
* Birth Date
* Death Date
* Gender
* Race
* Ethnicity
* Location information

---

### 2. Encounters

The **central fact table** of the project.

Contains information about healthcare visits and encounters.

Important fields include:

* Encounter ID
* Patient ID
* Organization ID
* Payer ID
* Start Date/Time
* Stop Date/Time
* Encounter Class
* Encounter Code
* Base Encounter Cost
* Total Claim Cost
* Payer Coverage
* Reason Code

---

### 3. Procedures

Contains information about medical procedures performed during encounters.

Important fields include:

* Procedure ID
* Patient ID
* Encounter ID
* Procedure Code
* Procedure Description
* Start Date
* Stop Date
* Base Cost
* Reason

---

### 4. Payers

Contains information about healthcare insurance providers.

Used to analyze:

* Payer coverage
* Insurance contribution
* Number of covered encounters
* Average claim costs
* Payer-level healthcare trends

---

### 5. Organizations

Contains information about healthcare organizations and providers.

Used to analyze healthcare activity across different organizations and locations.

---

# ❓ Key Business Questions

The project answers several healthcare analytics questions, including:

### 👥 Patient Analytics

* How many patients are currently living?
* How many patients are deceased?
* What is the patient distribution across locations?
* How frequently do patients visit healthcare providers?

### 🏥 Encounter Analytics

* How many healthcare encounters occur each year?
* Which encounter types are most common?
* How many emergency visits occur?
* What are the busiest periods?
* What is the average encounter duration?
* How do encounters change over time?

### 💰 Cost Analytics

* What is the total healthcare claim cost?
* How does claim cost change by month?
* Which encounter classes generate the highest costs?
* What are the most expensive procedures?
* How does procedure cost compare with total claim cost?

### 💊 Procedure Analytics

* Which procedures are performed most frequently?
* Which procedures have the highest costs?
* What are the most common procedure reasons?
* How many procedures occur per encounter?

### 🏦 Payer Analytics

* Which payers provide the highest coverage?
* What is the average claim cost by payer?
* How many encounters are associated with each payer?
* How does payer coverage vary across healthcare services?

---

# 📊 Power BI Dashboards

The project includes **4 interactive Power BI dashboards** designed to provide different perspectives of healthcare operations.

### Dashboard 1 — Hospital Performance Overview

Provides a high-level summary of the healthcare system.

Key metrics include:

* Total Patients
* Total Encounters
* Total Procedures
* Total Claim Cost
* Payer Coverage
* Average Encounter Cost

See here -> https://github.com/YASHIKAANEJA/AI-HealthCare-Analytics/blob/main/Hospital%20Performance%20Overview.png

---

### Dashboard 2 — Patient Demographics

Focuses on patient activity and healthcare utilization.

Includes:

* Patient trends
* Encounter trends
* Encounter class distribution
* Emergency vs routine visits
* Encounters by year/month
* Patient activity

See Here -> https://github.com/YASHIKAANEJA/AI-HealthCare-Analytics/blob/main/Patient%20Demographics.png

---

### Dashboard 3 — Clinical and Operational Analytics

Focuses on healthcare expenditure.

Includes:

* Claim cost trends
* Cost by encounter class
* Procedure cost analysis
* Most expensive procedures
* Procedure volume
* Cost comparisons

See here -> https://github.com/YASHIKAANEJA/AI-HealthCare-Analytics/blob/main/Clinical%20and%20Operational%20Analytics.png

---

### Dashboard 4 — Financial & Operational Analytics

Focuses on insurance and healthcare operations.

Includes:

* Payer coverage
* Claims by payer
* Average claim cost
* Insurance contribution
* Operational trends
* Healthcare utilization patterns

See here -> https://github.com/YASHIKAANEJA/AI-HealthCare-Analytics/blob/main/Financial%20%26%20Insurance%20Analytics.png

---

# 🤖 AI Healthcare Analytics

A major part of the project is the integration of an **AI-powered analytics layer**.

Instead of requiring users to write SQL queries, the Streamlit application allows users to interact with healthcare data using **Natural Language**.

For example:

```text
Which encounter type has the highest claim cost?
```

or

```text
What are the most common procedures?
```

or

```text
Which payer provides the highest coverage?
```

The application processes the uploaded healthcare data and uses an LLM through **OpenRouter** to generate understandable analytical responses.

---

# 🧠 AI Features

The AI layer is designed to provide:

### 💬 Natural Language Questions

Users can ask questions about healthcare data without writing SQL.

### 📊 Data Analysis

The application analyzes uploaded datasets and identifies relevant patterns and values.

### 📝 AI-Generated Insights

The LLM converts analytical results into easy-to-understand explanations.

### 📁 Multiple Dataset Support

Users can upload healthcare CSV files and analyze them through the application.

### 📸 Dashboard Screenshot Analysis

The application can also work with **Power BI dashboard screenshots**, allowing AI to interpret dashboard visuals and explain the insights shown.

---

# 🌐 Streamlit Application

The Streamlit application acts as the interactive front-end of the project.

### Main workflow

```text
Upload Healthcare Data
        ↓
Data Processing
        ↓
Ask a Natural Language Question
        ↓
Analyze Relevant Data
        ↓
AI Processing through OpenRouter
        ↓
Generate Explanation / Insight
```

The application brings together:

* Python
* Pandas
* Streamlit
* AI / LLM
* Healthcare analytics

into a single interactive interface.

---

# 🔍 Example Questions

Users can ask questions such as:

```text
What is the total claim cost?

Which encounter class is the most expensive?

Which procedures are performed most frequently?

What is the average encounter duration?

Which payer provides the highest coverage?

What are the busiest months?

How many emergency encounters occurred?

Which procedure has the highest average cost?

What are the major healthcare cost drivers?
```

---

# 🧹 Data Preparation

Before analysis, the healthcare data was prepared and validated through SQL and Python.

Major data preparation tasks included:

* Handling missing values
* Data type validation
* Date/time transformation
* Duplicate checking
* Data consistency checks
* Creating calculated fields
* Aggregating healthcare metrics
* Creating analytical datasets
* Validating relationships between tables

---

# 🧮 SQL Analysis

SQL was extensively used for healthcare analytics.

Examples of analysis performed:

* Aggregations
* GROUP BY analysis
* JOIN operations
* Date-based analysis
* Cost calculations
* Patient-level analysis
* Encounter-level analysis
* Procedure analysis
* Payer analysis
* KPI calculations
* Ranking and filtering

The SQL layer forms the foundation of the analytical workflow before visualization and AI analysis.

---

# 🐍 Python Analysis

Python was used for:

* Data loading
* Data cleaning
* Exploratory Data Analysis
* Data transformation
* Statistical calculations
* Data validation
* AI application development
* Streamlit integration

Main libraries include:

```text
Pandas
NumPy
Matplotlib
Streamlit
```

---

# 📈 Key Analytical Metrics

The project focuses on healthcare KPIs such as:

| KPI                        | Purpose                          |
| -------------------------- | -------------------------------- |
| Total Patients             | Measures patient population      |
| Total Encounters           | Measures healthcare utilization  |
| Total Procedures           | Measures medical activity        |
| Total Claim Cost           | Measures healthcare expenditure  |
| Payer Coverage             | Measures insurance contribution  |
| Average Encounter Cost     | Measures average healthcare cost |
| Average Encounter Duration | Measures visit duration          |
| Procedures per Encounter   | Measures treatment complexity    |
| Emergency Encounter Rate   | Measures emergency utilization   |
| Cost by Procedure          | Identifies expensive procedures  |

---

# 🔗 End-to-End Workflow

The project follows a complete analytics lifecycle:

### Step 1 — Data Collection

Healthcare datasets were collected and organized into relational tables.

### Step 2 — Data Storage

The data was loaded into **Snowflake**.

### Step 3 — Data Exploration

SQL and SnowSQL were used to explore and understand the dataset.

### Step 4 — Data Transformation

Healthcare data was cleaned, transformed and prepared for analysis.

### Step 5 — Analytical Modeling

Relationships between patients, encounters, procedures, payers and organizations were analyzed.

### Step 6 — Business Analysis

Healthcare KPIs and business questions were identified.

### Step 7 — Visualization

Power BI dashboards were developed to communicate insights interactively.

### Step 8 — AI Integration

An AI layer was added using **OpenRouter and LLMs**.

### Step 9 — Application Development

A Streamlit application was developed to provide an interactive Natural Language analytics experience.

---

# 🚀 Future Improvements

Potential future improvements include:

* 🔮 Predictive healthcare analytics
* 🤖 AI-powered healthcare agents
* 🧠 Retrieval-Augmented Generation (RAG)
* 💬 Conversational healthcare analytics
* 📊 Automated dashboard insight generation
* 🚨 Anomaly detection
* 📈 Healthcare cost forecasting
* 🏥 Patient risk analysis
* 🔄 Automated data pipelines
* ☁️ Cloud deployment
* 🔐 Role-based access control
* 📱 Mobile-friendly analytics interface

---

# 💡 What This Project Demonstrates

This project demonstrates practical experience in:

```text
Data Warehousing
        ↓
SQL Analytics
        ↓
Data Transformation
        ↓
Business Intelligence
        ↓
Data Visualization
        ↓
AI Integration
        ↓
Application Development
        ↓
Deployment
```

It combines traditional **Data Analytics and Business Intelligence** with modern **AI-powered analytics**.

---

# 📌 Skills Demonstrated

### Data Analytics

* Data Cleaning
* Exploratory Data Analysis
* Data Transformation
* KPI Development
* Business Analysis
* Insight Generation

### SQL

* Complex Queries
* Joins
* Aggregations
* Date Analysis
* Data Transformation
* Healthcare KPI Analysis

### Business Intelligence

* Power BI
* Interactive Dashboards
* KPI Cards
* Data Modeling
* Visual Analytics
* Dashboard Design

### Cloud & Data Engineering

* Snowflake
* SnowSQL
* Data Warehousing
* Relational Data Modeling

### AI & Application Development

* LLM Integration
* OpenRouter
* Natural Language Analytics
* Prompt Engineering
* Streamlit
* AI-powered Data Applications

### Programming

* Python
* Pandas
* NumPy
* Matplotlib

---

# 🌟 Project Highlights

* ✅ End-to-end healthcare analytics project
* ✅ Snowflake-based data warehouse
* ✅ SQL-driven data analysis
* ✅ 4 interactive Power BI dashboards
* ✅ Python-based data processing
* ✅ AI-powered Natural Language analytics
* ✅ OpenRouter LLM integration
* ✅ Interactive Streamlit application
* ✅ Power BI dashboard screenshot analysis
* ✅ Business-focused healthcare KPIs

---

🎓 Skills Demonstrated
📊 Data Analytics

Data Cleaning • EDA • Data Transformation • KPI Development • Business Analysis • Insight Generation

🧮 SQL

Joins • Aggregations • CTEs • Date Analysis • Data Transformation • Analytical Queries

📊 Business Intelligence

Power BI • Dashboard Development • Data Modeling • KPI Tracking • Interactive Visualization

❄️ Data Warehousing

Snowflake • SnowSQL • Cloud Data Warehousing • Relational Data Modeling

🐍 Programming

Python • Pandas • NumPy • Matplotlib

🤖 AI

LLMs • OpenRouter • Natural Language Analytics • Prompt Engineering • AI-powered Data Analysis

🌐 Application Development

Streamlit • Interactive Web Apps • API Integration

🔧 Development Tools

Git • GitHub • GitHub Codespaces
