# 🇮🇳 India Socio-Economic Data Pipeline

An end-to-end Data Engineering project that integrates Population Census, Literacy Census, and Employment datasets from India's National Data & Analytics Platform (NDAP) to generate state-level socio-economic insights.

---

## 📌 Project Goal

The objective of this project is to build a scalable data pipeline that consolidates multiple public datasets into a unified analytical model for understanding:

* Population distribution
* Literacy trends
* Employment patterns
* Workforce participation
* Socio-economic indicators across Indian states

---

## 🏗️ Project Architecture

```text
NDAP Datasets
│

├── Population Dataset (2011 Census)
├── Literacy Dataset (2011 Census)
└── Employment Dataset

        │
        ▼

Python Ingestion Layer

        │
        ▼

PostgreSQL Database

        │
        ▼

SQL Transformation Layer

        ├── literacy_analysis
        ├── literacy_state_total
        └── master_state_analysis

        │
        ▼

State-Level Analytics
```

### Architecture Diagram

![Architecture Diagram](docs/architecture.png)

---

## 📂 Datasets

### Population Census Dataset

* Total Population
* Male Population
* Female Population
* Literate Population
* SC/ST Population

### Literacy Dataset

* Literate Population
* Illiterate Population
* Worker Population
* Non-Worker Population
* Rural & Urban Distribution

### Employment Dataset

* Unemployment Rate
* Labour Participation Rate
* Employment Estimates

---

## ⚙️ Technology Stack

| Category                | Tools      |
| ----------------------- | ---------- |
| Programming             | Python     |
| Database                | PostgreSQL |
| Query Language          | SQL        |
| Containerization        | Docker     |
| Version Control         | Git        |
| Repository Hosting      | GitHub     |
| Development Environment | WSL Ubuntu |

---

## 🗄️ Database Objects

### Tables

* population_data
* literacy_data
* employment_data

### Views

#### literacy_analysis

State-level literacy and workforce metrics.

#### literacy_state_total

Filtered state-level totals from literacy data.

#### master_state_analysis

Integrated analytical layer combining:

* Population
* Literacy Rate
* Unemployment Rate
* Worker Population
* Non-Worker Population

---

## 📊 Sample Analysis

The project supports analysis such as:

* Top states by population
* States with highest unemployment
* States with lowest literacy rates
* Worker participation analysis
* Dependency ratio analysis
* Literacy vs unemployment comparison

---

## 📁 Repository Structure

```text
india-data-pipeline/

├── data/
├── docker/
├── ingestion/
├── postgres/
├── sql/
│   ├── tables/
│   ├── views/
│   └── analysis/
├── requirements.txt
└── README.md
```

---

## 🚀 Future Enhancements

* dbt Integration
* Apache Airflow Orchestration
* Power BI Dashboard
* Data Quality Validation Framework
* CI/CD Pipeline
* Cloud Deployment

---

## 📈 Key Learnings

This project demonstrates practical experience in:

* Data Ingestion
* Data Modeling
* SQL Transformations
* PostgreSQL Development
* Docker Fundamentals
* Git & GitHub Workflows
* End-to-End Data Pipeline Design

---

## 👨‍💻 Author

**Maharishi Acharya**

Data Engineering Portfolio Project
