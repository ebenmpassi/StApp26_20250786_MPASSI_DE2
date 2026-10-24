# ARIA Industrial Accidents Dashboard (France)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit 1.33+](https://img.shields.io/badge/Streamlit-1.33%2B-FF4B4B)](https://streamlit.io/)
[![Plotly 5.18+](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75)](https://plotly.com/python/)
[![Languages](https://img.shields.io/badge/Languages-EN%20%7C%20FR%20%7C%20ES%20%7C%20AR%20%7C%20ZH-orange)](#-multilingual-support)
[![License: Open](https://img.shields.io/badge/License-Open%20Data-green)](https://www.data.gouv.fr/)

An interactive data-storytelling web application built with **Streamlit** and **Plotly** to explore, map, and analyze industrial accidents, root causes, and environmental risks recorded in France.

---

## Project & Academic Metadata

* **Student:** Exauce Eben-Ezer MPASSI
* **Email:** exauce.mpassi@efrei.net
* **Professor:** Mano Joseph Mathew
* **Course:** Data Storytelling & Visualization
* **Academic Year:** 2026–2027
* **GitHub:** [https://github.com/ebenmpassi](https://github.com/ebenmpassi)
* **LinkedIn:** [Exauce MPASSI](https://www.linkedin.com/in/exauce-ebenmpassi/)
* **Link-streamlit:** https://ebenmpassi-stapp26-20250786-mpassi-de2-app-vx3dqe.streamlit.app/

---

## Multilingual Support

The dashboard provides dynamic, full-text internationalization for 5 languages:
* **English (EN)**
* **Français (FR)**
* **Español (ES)**
* **العربية (AR)** *(Includes dynamic Right-to-Left CSS layout adjustments)*
* **中文 (ZH)**[cite: 16]

---

## Storytelling & Narrative Overview

This application investigates industrial safety dynamics across Metropolitan France following a structured 4-stage narrative arc:

1. **Introduction & Context:** Introduces historical industrial disasters (*AZF explosion in Toulouse (2001)* and *Lubrizol fire in Rouen (2019)*) and highlights the role of open data transparency.
2. **Overview & Temporal Trends:** Features key performance metrics (KPIs) and tracks annual incident progression from 1990 onwards alongside regulatory milestones.
3. **Deep Dives & Visual Analytics:**
   * **Interactive Departmental Map:** Choropleth risk heatmap across French departments using GeoJSON boundaries.
   * **Root Causes vs. Consequences Matrix:** Row-normalized co-occurrence heatmap linking organizational defects to human, material, and environmental damage.
   * **Narrative Text Mining:** High-speed regex extraction of operational keywords (*Fire, Leak, Tank, Valve, Piping*) from free-text field logs.
   * **Departmental Ranking:** Top 20 industrial accident hotspots (*Nord, Bouches-du-Rhône, Seine-Maritime, etc.*).
   * **Impacted Economic Sectors:** Bubble scatter plot of top NAF activity branches (*Freight Transport, Agriculture, Gas Distribution*).
   * **Hierarchical Risk Breakdown:** Treemap nesting NAF activity sectors into dominant ARIA incident types.
   * **CLP Chemical Hazards:** Donut breakdown of dangerous chemical classifications (*Flammable gases, Carcinogens*).
4. **Implications & Quality Audit:** Strategic policy recommendations, field completeness audit charts, and a downloadable filtered dataset table.

---

## Dataset Source & Consolidation

The dashboard relies on open data from the official **ARIA** (*Analyse, Recherche et Information sur les Accidents*) database, managed by **BARPI** (*Bureau d’Analyse des Risques et Pollutions Industriels*).

* **Source Portal:** [data.gouv.fr — ARIA Dataset](https://www.data.gouv.fr/datasets/analyse-recherche-et-information-sur-les-accidents)
* **Scope:** 53,000+ public industrial incident reports in France[cite: 11].
* **Consolidation Note:** To bypass the official search portal's 500-record export limit, this project utilizes a fully consolidated UTF-8 dataset stored locally (`data/ARIA.csv`).

---

## Project Architecture

Built following modular Streamlit application architecture guidelines:

StApp26_20000_MPASSI_DE2/
├── app.py                     # Main Streamlit app entry point & language router
├── requirements.txt           # Project environment dependencies
├── README.md                  # Comprehensive project documentation
├── data/
│   └── ARIA.csv               # Processed ARIA database file
├── assets/
│   ├── exauce.jpeg            # Profile image
│   ├── rouen.avif             # Lubrizol incident photo
│   ├── substance.avif         # CLP hazardous substances photo
│   └── toulouse.jpg           # AZF disaster photo
├── sections/
│   ├── intro.py               # Section 1: Hook, context, and open data
│   ├── overview.py            # Section 2: KPIs & temporal line trends
│   ├── deep_dives.py          # Section 3: Maps, heatmaps, text mining, treemaps
│   └── conclusions.py         # Section 4: Policy implications, audit & CSV download
└── utils/
    ├── io.py                  # Cached data loading and date parsing
    ├── prep.py                # Filter logic, KPI computations & quality audits
    └── viz.py                 # Vectorized Plotly visualization engine
