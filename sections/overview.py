from altair import Key
import streamlit as st
from utils.prep import compute_kpis
from utils.viz import line_chart_accidents

# Translations dictionary for Section 2 across all 5 languages
OVERVIEW_TRANSLATIONS = {
    "en": {
        "header": "2. Overview & Temporal Trends",
        "kpi_total": "Total Logged Incidents",
        "kpi_dept": "Top Department",
        "kpi_sector": "Primary Industrial Sector",
        "title": "### Annual Progression of Industrial Incidents",
        "overview_label": "**Overview**",
        "overview_text": "Industrial accidents can have severe consequences for workers, local communities, and the environment. Tracking how incident counts evolve over time helps evaluate whether safety practices, regulatory frameworks, and prevention measures are effectively reducing industrial risks across France.",
        "chart_desc_label": "**What does this chart show?**",
        "chart_desc_text": "This chart displays the annual number of reported industrial incidents in France. It highlights long-term trends while providing historical context through major events and regulatory milestones, such as the AZF disaster in 2001 and the Lubrizol fire in 2019.",
        "takeaway_label": "**Key Takeaway**",
        "takeaway_text": "At first glance, an increase in reported incidents may suggest that industrial sites have become more dangerous. However, this is not always the case. Higher numbers can also result from stricter reporting requirements, more frequent inspections, improved monitoring systems, and greater transparency in accident reporting.",
        "importance_label": "**Why is this distinction important?**",
        "importance_text": "When analyzing long-term trends, it is essential to distinguish between actual changes in industrial safety and changes in reporting practices. Without this context, the data may be misinterpreted, leading to incorrect conclusions about the effectiveness of safety regulations and environmental policies.",
        "insight_label": "**Main Insight**",
        "insight_text": "The evolution of reported incidents reflects both operational safety performance and regulatory developments. Therefore, trends should be interpreted carefully, taking into account major policy changes and reporting obligations alongside the raw accident counts."
    },
    "fr": {
        "header": "2. Vue d'ensemble et tendances temporelles",
        "kpi_total": "Total des incidents enregistrés",
        "kpi_dept": "Premier département",
        "kpi_sector": "Secteur industriel principal",
        "title": "### Évolution annuelle des incidents industriels",
        "overview_label": "**Aperçu**",
        "overview_text": "Les accidents industriels peuvent avoir des conséquences graves pour les travailleurs, les communautés locales et l'environnement. Le suivi de l'évolution du nombre d'incidents au fil du temps permet d'évaluer si les pratiques de sécurité, les cadres réglementaires et les mesures de prévention réduisent efficacement les risques.",
        "chart_desc_label": "**Que montre ce graphique ?**",
        "chart_desc_text": "Ce graphique affiche le nombre annuel d'incidents industriels signalés en France. Il met en évidence les tendances à long terme tout en fournissant un contexte historique via des événements majeurs et des jalons réglementaires, tels que la catastrophe d'AZF en 2001 et l'incendie de Lubrizol en 2019.",
        "takeaway_label": "**À retenir**",
        "takeaway_text": "À première vue, une augmentation des incidents signalés peut suggérer que les sites sont devenus plus dangereux. Cependant, des chiffres plus élevés peuvent également résulter d'exigences de déclaration plus strictes, d'inspections plus fréquentes et d'une meilleure transparence.",
        "importance_label": "**Pourquoi cette distinction est-elle importante ?**",
        "importance_text": "Lors de l'analyse des tendances à long terme, il est essentiel de distinguer les évolutions réelles de la sécurité industrielle des changements dans les pratiques de déclaration afin d'éviter toute mauvaise interprétation des données.",
        "insight_label": "**Enseignement principal**",
        "insight_text": "L'évolution des incidents signalés reflète à la fois les performances opérationnelles en matière de sécurité et les évolutions réglementaires. Les tendances doivent donc être interprétées avec précaution."
    },
    "es": {
        "header": "2. Visión general y tendencias temporales",
        "kpi_total": "Total de incidentes registrados",
        "kpi_dept": "Departamento principal",
        "kpi_sector": "Sector industrial principal",
        "title": "### Evolución anual de incidentes industriales",
        "overview_label": "**Visión general**",
        "overview_text": "Los accidentes industriales pueden tener graves consecuencias para los trabajadores, las comunidades locales y el medio ambiente. Realizar un seguimiento de los incidentes a lo largo del tiempo ayuda a evaluar si las medidas de prevención están reduciendo eficazmente los riesgos.",
        "chart_desc_label": "**¿Qué muestra este gráfico?**",
        "chart_desc_text": "Este gráfico muestra el número anual de incidentes industriales reportados en Francia. Destaca tendencias a largo plazo y proporciona contexto histórico mediante hitos como el desastre de AZF en 2001 y el incendio de Lubrizol en 2019.",
        "takeaway_label": "**Conclusión clave**",
        "takeaway_text": "Un aumento en los incidentes reportados no siempre significa que los sitios sean más peligrosos. Unos números más altos también pueden deberse a requisitos de reporte más estrictos e inspecciones más frecuentes.",
        "importance_label": "**¿Por qué es importante esta distinción?**",
        "importance_text": "Al analizar tendencias a largo plazo, es esencial distinguir entre los cambios reales en la seguridad y los cambios en las prácticas de notificación para evitar conclusiones erróneas.",
        "insight_label": "**Perspectiva principal**",
        "insight_text": "La evolución de los incidentes refleja tanto el rendimiento operativo de seguridad como el desarrollo regulatorio. Las tendencias deben interpretarse con cuidado considerando los cambios normativos."
    },
    "ar": {
        "header": "2. نظرة عامة والاتجاهات الزمنية",
        "kpi_total": "إجمالي الحوادث المسجلة",
        "kpi_dept": "المقاطعة الأكثر تضرراً",
        "kpi_sector": "القطاع الصناعي الرئيسي",
        "title": "### التطور السنوي للحوادث الصناعية",
        "overview_label": "**نظرة عامة**",
        "overview_text": "يمكن أن يكون للحوادث الصناعية عواقب وخيمة على العمال والمجتمعات المحلية والبيئة. يساعد تتبع أعداد الحوادث عبر الزمن في تقييم ما إذا كانت ممارسات السلامة واللوائح التنظيمية تقلل بشكل فعال من المخاطر.",
        "chart_desc_label": "**ماذا يوضح هذا الرسم البياني؟**",
        "chart_desc_text": "يعرض هذا الرسم البياني العدد السنوي للحوادث الصناعية المبلغ عنها في فرنسا. ويسلط الضوء على الاتجاهات طويلة الأجل مع توفير سياق تاريخي من خلال الأحداث الكبرى مثل كارثة AZF في عام 2001 وحريق لوبريزول في عام 2019.",
        "takeaway_label": "**النقطة الرئيسية**",
        "takeaway_text": "للوهلة الأولى، قد تشير الزيادة في الحوادث المبلغ عنها إلى أن المواقع الصناعية أصبحت أكثر خطورة. ومع ذلك، قد تنتج الأعداد المرتفعة أيضًا عن متطلبات إبلاغ أكثر صرامة وعمليات تفتيش أكثر تكرارًا.",
        "importance_label": "**لماذا يعتبر هذا التمييز مهماً؟**",
        "importance_text": "عند تحليل الاتجاهات طويلة الأجل، من الضروري التمييز بين التغييرات الفعلية في السلامة والتغييرات في ممارسات الإبلاغ لتجنب التفسيرات الخاطئة للبيانات.",
        "insight_label": "**الرؤية الرئيسية**",
        "insight_text": "يعكس تطور الحوادث المبلغ عنها كلاً من أداء السلامة التشغيلية والتطورات التنظيمية. لذلك، يجب تفسير الاتجاهات بحذر."
    },
    "zh": {
        "header": "2. 概述与时间趋势",
        "kpi_total": "记录的事故总数",
        "kpi_dept": "事故最多省份",
        "kpi_sector": "主要工业部门",
        "title": "### 工业事故年度演变",
        "overview_label": "**概述**",
        "overview_text": "工业事故可能对工人、当地社区和环境造成严重后果。跟踪事故数量随时间的演变有助于评估安全实践、监管框架和预防措施是否有效降低了风险。",
        "chart_desc_label": "**该图表显示了什么？**",
        "chart_desc_text": "该图表显示了法国每年报告的工业事故数量。它突出了长期趋势，同时通过重大事件和监管里程碑（例如2001年的AZF灾难和2019年的Lubrizol火灾）提供了历史背景。",
        "takeaway_label": "**核心要点**",
        "takeaway_text": "乍一看，报告事故数量的增加可能表明工业场所变得更加危险。然而情况并非总是如此。较高的数字也可能是由于更严格的报告要求、更频繁的检查和更好的透明度造成的。",
        "importance_label": "**为什么这种区分很重要？**",
        "importance_text": "在分析长期趋势时，必须区分工业安全的实际变化与报告实践的变化。如果没有这些背景，可能会导致对安全监管和环境政策有效性的错误结论。",
        "insight_label": "**主要洞察**",
        "insight_text": "报告事故的演变既反映了操作安全绩效，也反映了监管的发展。因此，在解释趋势时应谨慎，将政策变化与原始事故数量结合起来考量。"
    }
}


def render_overview(df_filtered, lang: str = "en"):
    """
    Renders Section 2: Overview & Temporal Trends with multi-language support.
    Fallback to English if lang code is not found.
    """
    t = OVERVIEW_TRANSLATIONS.get(lang, OVERVIEW_TRANSLATIONS["en"])

    st.header(t["header"])
    
    kpis = compute_kpis(df_filtered)
    
    # KPI Metrics Header
    c1, c2, c3 = st.columns(3)
    c1.metric(t["kpi_total"], f"{kpis['total']:,}")
    c2.metric(t["kpi_dept"], kpis['top_departement'])
    c3.metric(t["kpi_sector"], str(kpis['top_naf']))
    
    st.divider()

    # Storytelling narrative before line chart
    st.markdown(t["title"])
    st.markdown(f"{t['overview_label']}\n{t['overview_text']}")
    st.markdown(f"{t['chart_desc_label']}\n{t['chart_desc_text']}")

    # Render Line Chart
    fig_time = line_chart_accidents(df_filtered)
    st.plotly_chart(fig_time, use_container_width=True)

    # Narrative insights after line chart
    st.markdown(f"{t['takeaway_label']}\n{t['takeaway_text']}")
    st.markdown(f"{t['importance_label']}\n{t['importance_text']}")
    st.markdown(f"{t['insight_label']}\n{t['insight_text']}")