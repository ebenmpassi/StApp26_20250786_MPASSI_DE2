import streamlit as st
from utils.prep import get_data_quality_report
from utils.viz import completeness_bar_chart

CONCLUSIONS_TRANSLATIONS = {
    "en": {
        "header": "4. Implications, Recommendations & Data Health Check",
        "tab_audit": "Implications & Quality Audit",
        "tab_data": "Filtered Dataset & CSV Export",
        "implications_title": "### Key Strategic Implications",
        "imp_1_title": "1. **Focus resources where the risks are highest**",
        "imp_1_desc": "Departments and industrial sectors with a large number of reported incidents should receive increased inspections and closer regulatory monitoring.",
        "imp_2_title": "2. **Strengthen emergency preparedness in industrial areas**",
        "imp_2_desc": "Regions with high concentrations of industrial facilities need well-coordinated emergency response plans to reduce the impact of potential accidents on nearby communities and the environment.",
        "imp_3_title": "3. **Promote a proactive safety culture**",
        "imp_3_desc": "Beyond regulatory compliance, companies should invest in employee training, preventive maintenance, and risk awareness to reduce the likelihood of future incidents.",
        "imp_4_title": "4. **Use data to support decision-making**",
        "imp_4_desc": "Insights from the ARIA database can help public authorities and industry stakeholders identify trends, anticipate risks, and prioritize prevention efforts more effectively.",
        "data_subtitle": "Filtered ARIA Dataset Overview",
        "download_label": "Download Filtered ARIA CSV Data"
    },
    "fr": {
        "header": "4. Implications, Recommandations et Audit Qualité",
        "tab_audit": "Implications et Audit Qualité",
        "tab_data": "Données Filtrées et Export CSV",
        "implications_title": "### Principales Implications Stratégiques",
        "imp_1_title": "1. **Cibler les ressources là où les risques sont les plus élevés**",
        "imp_1_desc": "Les départements et secteurs industriels enregistrant un grand nombre d'incidents doivent faire l'objet d'inspections accrues et d'un suivi réglementaire plus étroit.",
        "imp_2_title": "2. **Renforcer la préparation aux urgences dans les zones industrielles**",
        "imp_2_desc": "Les régions à forte concentration industrielle ont besoin de plans d'intervention d'urgence bien coordonnés pour limiter l'impact des accidents sur les populations et l'environnement.",
        "imp_3_title": "3. **Promouvoir une culture de sécurité proactive**",
        "imp_3_desc": "Au-delà de la conformité réglementaire, les entreprises doivent investir dans la formation, la maintenance préventive et la sensibilisation aux risques.",
        "imp_4_title": "4. **Utiliser les données pour soutenir la prise de décision**",
        "imp_4_desc": "Les enseignements de la base ARIA aident les autorités publiques et les acteurs industriels à identifier les tendances et à anticiper les risques plus efficacement.",
        "data_subtitle": "Aperçu du jeu de données ARIA filtré",
        "download_label": "Télécharger les données ARIA filtrées en CSV"
    },
    "es": {
        "header": "4. Implicaciones, Recomendaciones y Control de Calidad",
        "tab_audit": "Implicaciones y Auditoría de Calidad",
        "tab_data": "Datos Filtrados y Exportación CSV",
        "implications_title": "### Principales Implicaciones Estratégicas",
        "imp_1_title": "1. **Enfocar recursos donde los riesgos sean mayores**",
        "imp_1_desc": "Los departamentos y sectores industriales con mayor número de incidentes reportados deben recibir inspecciones más frecuentes y un monitoreo regulatorio más riguroso.",
        "imp_2_title": "2. **Fortalecer la preparación ante emergencias en zonas industriales**",
        "imp_2_desc": "Las regiones con alta concentración industrial necesitan planes de respuesta a emergencias coordinados para reducir el impacto de posibles accidentes en las comunidades locales.",
        "imp_3_title": "3. **Promover una cultura de seguridad proactiva**",
        "imp_3_desc": "Más allá del cumplimiento normativo, las empresas deben invertir en capacitación del personal, mantenimiento preventivo y concienciación sobre los riesgos.",
        "imp_4_title": "4. **Utilizar datos para respaldar la toma de decisiones**",
        "imp_4_desc": "Los análisis de la base de datos ARIA ayudan a las autoridades y actores industriales a identificar tendencias, anticipar riesgos y priorizar medidas de prevención.",
        "data_subtitle": "Visión general del conjunto de datos ARIA filtrado",
        "download_label": "Descargar datos filtrados de ARIA en CSV"
    },
    "ar": {
        "header": "4. الآثار المترتبة والتوصيات وفحص جودة البيانات",
        "tab_audit": "الآثار التدقيقية وجودة البيانات",
        "tab_data": "مجموعة البيانات المصفاة وتصدير CSV",
        "implications_title": "### الآثار الاستراتيجية الرئيسية",
        "imp_1_title": "1. **تركيز الموارد حيث تكون المخاطر أعلى**",
        "imp_1_desc": "يجب أن تتلقى المقاطعات والقطاعات الصناعية ذات الأعداد الكبيرة من الحوادث عمليات تفتيش مكثفة ومراقبة تنظيمية دقيقة.",
        "imp_2_title": "2. **تعزيز الجاهزية للطوارئ في المناطق الصناعية**",
        "imp_2_desc": "تحتاج المناطق ذات التركيز العالي للمنشآت الصناعية إلى خطط استجابة للطوارئ منسقة جيدًا لتقليل تأثير الحوادث على المجتمعات والبيئة.",
        "imp_3_title": "3. **تعزيز ثقافة السلامة الاستباقية**",
        "imp_3_desc": "بعيدًا عن الامتثال التنظيمي، يجب على الشركات الاستثمار في تدريب الموظفين والصيانة الوقائية والتوعية بالمخاطر.",
        "imp_4_title": "4. **استخدام البيانات لدعم اتخاذ القرار**",
        "imp_4_desc": "تساعد الرؤى من قاعدة بيانات ARIA السلطات العامة وأصحاب المصلحة في تحديد الاتجاهات وتوقع المخاطر بشكل أكثر فعالية.",
        "data_subtitle": "نظرة عامة على مجموعة بيانات ARIA المصفاة",
        "download_label": "تحميل بيانات ARIA المصفاة بصيغة CSV"
    },
    "zh": {
        "header": "4. 启示、建议与数据质量检查",
        "tab_audit": "启示与质量审计",
        "tab_data": "已筛选数据集与 CSV 导出",
        "implications_title": "### 核心战略启示",
        "imp_1_title": "1. **将资源集中在风险最高的领域**",
        "imp_1_desc": "报告事故数量较多的省份和工业部门应接受更多的现场检查和更严格的监管监控。",
        "imp_2_title": "2. **加强工业区应急准备**",
        "imp_2_desc": "工业设施高度集中的地区需要高度协调的应急响应计划，以减轻潜在事故对周边社区和环境的影响。",
        "imp_3_title": "3. **促进积极主动的安全文化**",
        "imp_3_desc": "除法规合规外，企业还应投资于员工培训、预防性维护和风险意识，以降低未来事故发生的可能性。",
        "imp_4_title": "4. **利用数据支持决策**",
        "imp_4_desc": "ARIA 数据库的洞察可以帮助公共机构和行业相关者识别趋势、预判风险并更有效地规划预防工作。",
        "data_subtitle": "已筛选 ARIA 数据集概述",
        "download_label": "下载筛选后的 ARIA CSV 数据"
    }
}


def render_conclusions(df_filtered, lang: str = "en"):
    """
    Renders Section 4: Implications, Recommendations & Data Health Check with multi-language support.
    Fallback to English if lang code is not found.
    """
    t = CONCLUSIONS_TRANSLATIONS.get(lang, CONCLUSIONS_TRANSLATIONS["en"])

    st.header(t["header"])
    
    # 1. Create Tabs
    tab_audit, tab_data = st.tabs([
        t["tab_audit"], 
        t["tab_data"]
    ])
    
    # Tab 1: Implications & Data Audit
    with tab_audit:
        st.markdown(f"""
        {t['implications_title']}

        {t['imp_1_title']}  
        {t['imp_1_desc']}

        {t['imp_2_title']}  
        {t['imp_2_desc']}

        {t['imp_3_title']}  
        {t['imp_3_desc']}

        {t['imp_4_title']}  
        {t['imp_4_desc']}
        """)

        report = get_data_quality_report(df_filtered)
        st.plotly_chart(completeness_bar_chart(report), use_container_width=True)

    # Tab 2: Filtered Data Overview & Download
    with tab_data:
        st.subheader(t["data_subtitle"])

        display_cols = [
            "Numéro ARIA",
            "Date",
            "Titre",
            "Département",
            "Commune",
            "Code NAF",
            "Type d'accident",
            "Classe de danger CLP",
            "Echelle",
            "Equipements",
            "Causes profondes"
        ]

        display_cols = [c for c in display_cols if c in df_filtered.columns]

        # Determine sort column safely without invalid parameters
        sort_col = "Date_parsed" if "Date_parsed" in df_filtered.columns else ("Numéro ARIA" if "Numéro ARIA" in df_filtered.columns else None)
        
        if sort_col:
            df_sorted = df_filtered.sort_values(by=sort_col, ascending=False)[display_cols]
        else:
            df_sorted = df_filtered[display_cols]

        st.dataframe(
            df_sorted,
            use_container_width=True,
            hide_index=True
        )

        csv_data = df_filtered[display_cols].to_csv(index=False).encode("utf-8")

        st.download_button(
            label=t["download_label"],
            data=csv_data,
            file_name="aria_accidents_france_filtered.csv",
            mime="text/csv",
        )