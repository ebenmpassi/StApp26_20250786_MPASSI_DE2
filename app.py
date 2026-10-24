import streamlit as st
from utils.io import load_data
from utils.prep import filter_data

from sections.intro import render_intro
from sections.overview import render_overview
from sections.deep_dives import render_deep_dives
from sections.conclusions import render_conclusions

# Dictionary containing translations for app.py UI elements
TRANSLATIONS = {
    "English": {
        "page_title": "Data Storytelling — France Industrial Accidents",
        "title": "Data Storytelling: Analysis of Industrial Accidents & Incidents in France",
        "caption": "Source: Bureau d'Analyse des Risques et Pollutions Industriels (BARPI) — data.gouv.fr",
        "project_info": "Project Info",
        "student_info": (
            "**Name:** Exauce Eben-Ezer MPASSI  \n"
            "**Email:** exauce.mpassi@efrei.net  \n"
            "**Professor:** Mano Joseph Mathew  \n"
            "**Academic Year:** 2026-2027\n"
            "**GitHub:** https://github.com/ebenmpassi\n"
            "**LinkedIn:** https://www.linkedin.com/in/exauce-ebenmpassi/"
        ),
        "filters_header": "Filters & Controls (France Focus)",
        "study_period": "Study Period (Years)",
        "dept_filter": "Filter by French Departments",
        "dept_placeholder": "All Departments (Default)"
    },
    "Français": {
        "page_title": "Data Storytelling — Accidents Industriels en France",
        "title": "Data Storytelling : Analyse des Accidents et Incidents Industriels en France",
        "caption": "Source : Bureau d'Analyse des Risques et Pollutions Industriels (BARPI) — data.gouv.fr",
        "project_info": "Informations Projet",
        "student_info": (
            "**Nom :** Exauce Eben-Ezer MPASSI  \n"
            "**Email :** exauce.mpassi@efrei.net  \n"
            "**Professeur :** Mano Joseph Mathew  \n"
            "**Année Académique :** 2026-2027\n"
            "**GitHub :** https://github.com/ebenmpassi\n"
            "**LinkedIn :** https://www.linkedin.com/in/exauce-ebenmpassi/"
        ),
        "filters_header": "Filtres et Contrôles (Focus France)",
        "study_period": "Période d'étude (Années)",
        "dept_filter": "Filtrer par départements français",
        "dept_placeholder": "Tous les départements (Par défaut)"
    },
    "Español": {
        "page_title": "Data Storytelling — Accidentes Industriales en Francia",
        "title": "Data Storytelling: Análisis de Accidentes e Incidentes Industriales en Francia",
        "caption": "Fuente: Bureau d'Analyse des Risques et Pollutions Industriels (BARPI) — data.gouv.fr",
        "project_info": "Información del Proyecto",
        "student_info": (
            "**Nombre:** Exauce Eben-Ezer MPASSI  \n"
            "**Correo:** exauce.mpassi@efrei.net  \n"
            "**Profesor:** Mano Joseph Mathew  \n"
            "**Año Académico:** 2026-2027\n"
            "**GitHub:** https://github.com/ebenmpassi\n"
            "**LinkedIn:** https://www.linkedin.com/in/exauce-ebenmpassi/"
        ),
        "filters_header": "Filtros y Controles (Enfoque Francia)",
        "study_period": "Período de estudio (Años)",
        "dept_filter": "Filtrar por departamentos franceses",
        "dept_placeholder": "Todos los departamentos (Por defecto)"
    },
    "العربية": {
        "page_title": "سرد البيانات — الحوادث الصناعية في فرنسا",
        "title": "سرد البيانات: تحليل الحوادث والحوادث الصناعية في فرنسا",
        "caption": "المصدر: مكتب تحليل المخاطر والتلوث الصناعي (BARPI) — data.gouv.fr",
        "project_info": "معلومات المشروع",
        "student_info": (
            "**الاسم:** Exauce Eben-Ezer MPASSI  \n"
            "**البريد الإلكتروني:** exauce.mpassi@efrei.net  \n"
            "**الأستاذ:** Mano Joseph Mathew  \n"
            "**العام الأكاديمي:** 2026-2027\n"
            "**GitHub:** https://github.com/ebenmpassi\n"
            "**LinkedIn:** https://www.linkedin.com/in/exauce-ebenmpassi/"
        ),
        "filters_header": "الفلاتر وعناصر التحكم (التركيز على فرنسا)",
        "study_period": "فترة الدراسة (بالسنوات)",
        "dept_filter": "التصفية حسب المقاطعات الفرنسية",
        "dept_placeholder": "جميع المقاطعات (افتراضي)"
    },
    "中文": {
        "page_title": "数据叙事 — 法国工业事故分析",
        "title": "数据叙事：法国工业事故与事件分析",
        "caption": "数据来源：法国工业风险与污染分析局 (BARPI) — data.gouv.fr",
        "project_info": "项目信息",
        "student_info": (
            "**姓名:** Exauce Eben-Ezer MPASSI  \n"
            "**邮箱:** exauce.mpassi@efrei.net  \n"
            "**指导教授:** Mano Joseph Mathew  \n"
            "**学年:** 2026-2027\n"
            "**GitHub:** https://github.com/ebenmpassi\n"
            "**LinkedIn:** https://www.linkedin.com/in/exauce-ebenmpassi/"
        ),
        "filters_header": "筛选与控制 (聚焦法国)",
        "study_period": "研究时间段 (年)",
        "dept_filter": "按法国省份筛选",
        "dept_placeholder": "所有省份 (默认)"
    }
}

# Initial configuration
st.set_page_config(page_title="Data Storytelling — France Industrial Accidents", layout="wide")

# Language Selector in Sidebar
language = st.sidebar.selectbox(
    "Language / Langue / Idioma / اللغة / 语言",
    ["English", "Français", "Español", "العربية", "中文"]
)

# Apply Right-To-Left CSS layout adjustments when Arabic is selected
if language == "العربية":
    st.markdown(
        """
        <style>
        body, div, p, h1, h2, h3, h4, h5, h6 {
            direction: RTL;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

t = TRANSLATIONS[language]

# Load dataset with caching
df_raw = load_data()

# Main Title & Subtitle
st.title(t["title"])
st.caption(t["caption"])

# Sidebar informational header & filters 
st.sidebar.title(t["project_info"])
st.sidebar.image(
    "assets/exauce.jpeg",
    width=180
)
st.sidebar.info(t["student_info"])

st.sidebar.divider()

# Sidebar: Interactive Controls
st.sidebar.header(t["filters_header"])

# Filter strictly for France
df_france = df_raw[df_raw['Pays'] == 'FRANCE']

# Date Range Selection
min_year = int(df_france['Annee'].min()) if not df_france['Annee'].isna().all() else 1980
max_year = int(df_france['Annee'].max()) if not df_france['Annee'].isna().all() else 2026

date_range = st.sidebar.slider(
    t["study_period"], 
    min_value=min_year, 
    max_value=max_year, 
    value=(1990, max_year)
)

# French Department Multi-Select Filter
deps_list = sorted([d for d in df_france['Département'].unique() if d not in ['UNKNOWN', 'nan', 'INCONNU']])
selected_deps = st.sidebar.multiselect(
    t["dept_filter"], 
    deps_list, 
    placeholder=t["dept_placeholder"]
)

# Apply Filters (Strictly for France)
df_filtered = filter_data(df_raw, "FRANCE", date_range, selected_deps)

# Map language selection to 2-letter ISO code for section components
lang_code_map = {
    "English": "en",
    "Français": "fr",
    "Español": "es",
    "العربية": "ar",
    "中文": "zh"
}
lang_code = lang_code_map[language]

# Render Data Storytelling Sections (passing lang_code down to sections)
render_intro(df_raw, lang=lang_code)
st.divider()
render_overview(df_filtered, lang=lang_code)
st.divider()
render_deep_dives(df_filtered, lang=lang_code)
st.divider()
render_conclusions(df_filtered, lang=lang_code)