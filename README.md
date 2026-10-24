# ARIA Industrial Accidents Dashboard (France)

An interactive **data storytelling dashboard** built with **Streamlit** and **Plotly** to explore, visualize, and analyze industrial accidents, their root causes, and environmental impacts across France.

This project was developed as part of the **Data Storytelling & Visualization** course at **EFREI Paris**.

---

# Project Information

- **Student:** Exaucé Eben-Ezer MPASSI
- **Email:** exauce.mpassi@efrei.net
- **Professor:** Mano Joseph Mathew
- **Course:** Data Storytelling & Visualization
- **Academic Year:** 2026–2027
- **GitHub:** https://github.com/ebenmpassi
- **LinkedIn:** https://www.linkedin.com/in/exauce-ebenmpassi/
- **Link of the streamlit dashboard:** https://ebenmpassi-stapp26-20250786-mpassi-de2-app-vx3dqe.streamlit.app/

---

# Project Overview

Industrial accidents can have serious consequences for workers, local communities, infrastructure, and the environment. Through the analysis of more than **53,000 industrial incidents**, this dashboard seeks to identify trends, high-risk regions, vulnerable industrial sectors, and recurring accident causes across France.

Rather than presenting raw data alone, the application follows a **data storytelling approach**, transforming complex industrial safety records into understandable insights through interactive visualizations and narrative explanations.

---

# Objectives

The dashboard aims to answer several key questions:

- How have industrial accidents evolved over time in France?
- Which departments are the most affected?
- Which industrial sectors experience the highest number of incidents?
- What are the most common root causes and consequences?
- What hazardous substances are most frequently involved?
- What lessons can be learned to improve industrial safety?

---

# Storytelling Structure

The dashboard follows a four-stage narrative structure.

## 1. Introduction & Context

This section introduces the importance of industrial safety through major French industrial disasters:

- AZF Explosion (Toulouse, 2001)
- Lubrizol Fire (Rouen, 2019)

It also presents the ARIA database and explains the importance of open data for industrial risk management.

---

## 2. Overview & Temporal Trends

This section provides:

- Key Performance Indicators (KPIs)
- Annual evolution of industrial incidents
- Long-term accident trends
- Historical context and regulatory milestones

The objective is to understand how industrial incidents have changed over time.

---

## 3. Deep Dive Analysis

### Geographic Analysis

- Interactive departmental risk map
- Top departments by number of incidents

### Root Cause Analysis

- Correlation heatmap between root causes and observed consequences

### Text Mining Analysis

- Keyword extraction from accident narratives
- Identification of recurring technical failures

### Sector Analysis

- Top industrial sectors based on NAF activity codes
- Bubble chart sector ranking
- Sector-to-accident-type treemap

### Hazard Analysis

- CLP hazard class distribution
- Identification of the most common hazardous substances

---

## 4. Conclusions & Data Quality Assessment

The final section includes:

- Key findings
- Strategic recommendations
- Data completeness analysis
- Data quality indicators
- Downloadable filtered dataset

---

# Dataset Source

This project uses open data from the **ARIA (Analyse, Recherche et Information sur les Accidents)** database maintained by **BARPI (Bureau d'Analyse des Risques et Pollutions Industriels)**.

### Dataset Information

- **Source:** https://www.data.gouv.fr/datasets/analyse-recherche-et-information-sur-les-accidents
- **Coverage:** More than 53,000 industrial and technological incidents in France
- **Provider:** French Ministry for Ecological Transition
- **Format:** CSV

### Data Preparation

To improve usability and performance, accident records were consolidated into a single UTF-8 encoded dataset:

```text
data/ARIA.csv
```

---

# Main Features

Interactive dashboard built with Streamlit

Dynamic filtering by country, department, and year

KPI monitoring

Interactive geographic mapping

Time-series analysis

Sector ranking and comparison

Root cause vs consequence analysis

Text mining of accident reports

CLP hazard classification analysis

Data quality and completeness assessment

Downloadable filtered dataset

---

# Multilingual Support

The dashboard supports multiple languages:

- 🇬🇧 English
- 🇫🇷 French
- 🇪🇸 Spanish
- 🇸🇦 Arabic (RTL support)
- 🇨🇳 Chinese

---

# Project Architecture

The application follows a modular architecture designed to separate data processing, visualization, and presentation layers.

```text
StApp26_20250786_MPASSI_DE2/
│
├── app.py
│   # Main Streamlit application
│
├── requirements.txt
│   # Dependencies
│
├── README.md
│
├── data/
│   └── ARIA.csv
│
├── assets/
│   ├── exauce.jpeg
│   ├── rouen.avif
│   ├── substance.avif
│   └── toulouse.jpg
│
├── sections/
│   ├── intro.py
│   ├── overview.py
│   ├── deep_dives.py
│   └── conclusions.py
│
└── utils/
    ├── io.py
    ├── prep.py
    └── viz.py
```

## Architecture Overview

### Presentation Layer

Located in the `sections/` folder:

- `intro.py` → Project context and industrial disasters
- `overview.py` → KPIs and temporal trends
- `deep_dives.py` → Advanced visual analytics
- `conclusions.py` → Findings and recommendations

### Data Processing Layer

Located in `utils/prep.py`:

- Data cleaning
- Filtering
- KPI calculations
- Data quality assessment

### Visualization Layer

Located in `utils/viz.py`:

- Plotly charts
- Maps
- Heatmaps
- Treemaps
- Text mining visualizations

### Performance Layer

Located in `utils/io.py`:

- Dataset loading
- Date parsing
- Streamlit caching

---

# Technologies Used

### Programming

- Python 3

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

### Web Application

- Streamlit

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/ebenmpassi/StApp26_20250786_MPASSI_DE2.git
```

## Navigate to the Project Folder

```bash
cd StApp26_20250786_MPASSI_DE2
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# Data Quality & Limitations

Several factors should be considered when interpreting the results:

- Reported incidents may increase due to stricter reporting requirements rather than actual increases in risk.
- Some records contain missing values.
- Administrative and regulatory changes may affect long-term comparisons.
- Correlation does not imply causation.
- The analysis relies on publicly available information contained in the ARIA database.

---

# Key Insights

The analysis reveals several notable patterns:

- Industrial incidents are concentrated in a limited number of departments.
- Certain industrial sectors account for a disproportionate share of reported accidents.
- Human and organizational factors frequently contribute to incident occurrence.
- Hazardous substance management remains a recurring challenge across multiple industries.
- Reporting trends often reflect both operational incidents and regulatory evolution.

---

# Learning Outcomes

This project demonstrates skills in:

- Open data integration
- Data cleaning and preparation
- Exploratory Data Analysis (EDA)
- Interactive dashboard design
- Data storytelling
- Geographic visualization
- Text mining
- Risk communication
- Streamlit development
- Plotly visualization

---

# Acknowledgements

Special thanks to:

- **EFREI Paris**
- **Mano Joseph Mathew**
- **BARPI**
- **data.gouv.fr**

for providing the resources and data necessary to complete this project.

---

# Author

**Exaucé Eben-Ezer MPASSI**

Master's Student in Data Engineering & Artificial Intelligence  
EFREI Paris

- GitHub: https://github.com/ebenmpassi
- LinkedIn: https://www.linkedin.com/in/exauce-ebenmpassi/
