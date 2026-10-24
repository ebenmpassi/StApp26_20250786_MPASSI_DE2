import streamlit as st

# Translations dictionary for all 5 languages
INTRO_TRANSLATIONS = {
    "en": {
        "header": "1. Introduction",
        "hook_title": "### Why Should You Care?",
        "hook_text": """
        Industrial accidents can have a major impact on people's lives, local communities, and the environment. Events such as the **AZF explosion in Toulouse (2001)** and the **Lubrizol fire in Rouen (2019)** remind us that technological risks are still a real challenge in modern society.

        By studying past incidents, we can better understand where risks occur, identify common causes, and highlight areas where safety measures could be improved.
        """,
        "caption_toulouse": "Historic Industrial Disasters Context (AZF Toulouse)",
        "caption_rouen": "More than 240 firefighters were deployed at the Lubrizol factory site near Rouen to contain the fire that broke out on September 26, 2019",
        "context_title": "2. Background and Open Data Context",
        "context_text": """
        The analysis in this project is based on the **ARIA (Analysis, Research and Information on Accidents)** database, maintained by **BARPI**. The dataset contains information on more than **53,000 industrial and technological incidents**, providing valuable insight into accident patterns across France.

        Using this open dataset allows us to explore how industrial risks vary over time, across regions, and between different sectors of activity.
        """,
        "why_open_title": "#### Why Open Data Matters",
        "why_open_points": """
        - Public access to safety-related data promotes transparency and accountability.
        - Open datasets enable researchers, students, and policymakers to better understand industrial risks.
        - Making data available encourages evidence-based decision-making and supports risk prevention efforts.
        """,
        "dashboard_title": "#### What This Dashboard Brings",
        "dashboard_points": """
        - Instead of browsing thousands of records individually, users can explore the data through interactive visualizations.
        - The dashboard highlights key trends, geographical patterns, and sector-specific risks.
        - It transforms raw accident reports into insights that are easier to understand and communicate.
        """,
        "nb_note": "**NB**: An increase in reported incidents does not always mean industrial sites became more dangerous. It may also result from improved reporting requirements and stronger regulatory oversight."
    },
    "fr": {
        "header": "1. Introduction",
        "hook_title": "### Pourquoi s'en soucier ?",
        "hook_text": """
        Les accidents industriels peuvent avoir un impact majeur sur la vie des personnes, les communautés locales et l'environnement. Des événements tels que l'**explosion d'AZF à Toulouse (2001)** et l'**incendie de Lubrizol à Rouen (2019)** nous rappellent que les risques technologiques restent un défi majeur.

        L'étude des incidents passés nous permet de mieux comprendre où surviennent les risques, d'en identifier les causes communes et de souligner les points à améliorer.
        """,
        "caption_toulouse": "Contexte des catastrophes industrielles historiques (AZF Toulouse)",
        "caption_rouen": "Plus de 240 pompiers ont été déployés sur le site de l'usine Lubrizol près de Rouen pour contenir l'incendie du 26 septembre 2019",
        "context_title": "2. Contexte et Données Ouvertes",
        "context_text": """
        L'analyse de ce projet repose sur la base de données **ARIA (Analyse, Recherche et Information sur les Accidents)**, gérée par le **BARPI**. Le jeu de données répertorie plus de **53 000 incidents industriels et technologiques**.

        Ce jeu de données ouvert permet d'explorer la variation des risques industriels dans le temps, entre les régions et selon les secteurs d'activité.
        """,
        "why_open_title": "#### Pourquoi les données ouvertes comptent",
        "why_open_points": """
        - L'accès public favorise la transparence et la responsabilisation.
        - Les données ouvertes permettent aux chercheurs, étudiants et décideurs de mieux comprendre les risques.
        - Elles encouragent la prise de décision basée sur des faits et soutiennent la prévention.
        """,
        "dashboard_title": "#### Ce que ce tableau de bord apporte",
        "dashboard_points": """
        - Explorer les données via des visualisations interactives au lieu de parcourir des milliers de lignes.
        - Mettre en évidence les tendances clés, les modèles géographiques et les risques sectoriels.
        - Transformer des rapports d'accidents bruts en informations faciles à comprendre.
        """,
        "nb_note": "**N.B.** : Une augmentation des incidents signalés ne signifie pas nécessairement que les sites sont devenus plus dangereux ; elle peut résulter d'exigences de déclaration plus strictes."
    },
    "es": {
        "header": "1. Introducción",
        "hook_title": "### ¿Por qué debería importar?",
        "hook_text": """
        Los accidentes industriales pueden tener un gran impacto en la vida de las personas, las comunidades locales y el medio ambiente. Eventos como la **explosión de AZF en Toulouse (2001)** y el **incendio de Lubrizol en Ruán (2019)** nos recuerdan que los riesgos tecnológicos siguen siendo un desafío real.

        Estudiar los incidentes pasados nos permite comprender mejor dónde ocurren los riesgos e identificar las áreas donde se pueden mejorar las medidas de seguridad.
        """,
        "caption_toulouse": "Contexto histórico de desastres industriales (AZF Toulouse)",
        "caption_rouen": "Más de 240 bomberos fueron desplegados en la fábrica de Lubrizol cerca de Ruán para contener el incendio del 26 de septiembre de 2019",
        "context_title": "2. Antecedentes y Contexto de Datos Abiertos",
        "context_text": """
        El análisis se basa en la base de datos **ARIA**, mantenida por el **BARPI**. El conjunto de datos contiene información sobre más de **53,000 incidentes industriales y tecnológicos** en Francia.

        El uso de datos abiertos nos permite explorar cómo varían los riesgos industriales a lo largo del tiempo, entre regiones y sectores de actividad.
        """,
        "why_open_title": "#### Por qué importan los datos abiertos",
        "why_open_points": """
        - El acceso público promueve la transparencia y la rendición de cuentas.
        - Permite a investigadores y legisladores comprender mejor los riesgos industriales.
        - Fomenta la toma de decisiones basada en evidencia y la prevención de riesgos.
        """,
        "dashboard_title": "#### Lo que aporta este panel",
        "dashboard_points": """
        - Explora datos mediante visualizaciones interactivas en lugar de revisar miles de registros.
        - Destaca tendencias clave, patrones geográficos y riesgos sectoriales.
        - Transforma informes brutos de accidentes en información clara y comunicable.
        """,
        "nb_note": "**Nota**: Un aumento en los incidentes reportados no siempre significa que los sitios sean más peligrosos, sino que puede deberse a un monitoreo más estricto."
    },
    "ar": {
        "header": "1. المقدمة",
        "hook_title": "### لماذا يجب أن تهتم؟",
        "hook_text": """
        يمكن أن يكون للحوادث الصناعية تأثير كبير على حياة الناس والمجتمعات المحلية والبيئة. تذكرنا أحداث مثل **انفجار AZF في تولوز (2001)** و**حريق لوبريزول في روان (2019)** بأن المخاطر التكنولوجية لا تزال تشكل تحديًا حقيقيًا.

        من خلال دراسة الحوادث السابقة، يمكننا فهم مكان حدوث المخاطر بشكل أفضل وتحديد المجالات التي يمكن تحسين إجراءات السلامة فيها.
        """,
        "caption_toulouse": "سياق الكوارث الصناعية التاريخية (AZF تولوز)",
        "caption_rouen": "تم نشر أكثر من 240 رجل إطفاء في مصنع لوبريزول بالقرب من روان للسيطرة على الحريق الذي اندلع في 26 سبتمبر 2019",
        "context_title": "2. الخلفية وسياق البيانات المفتوحة",
        "context_text": """
        يعتمد التحليل على قاعدة بيانات **ARIA** التي يديرها **BARPI**. تحتوي قاعدة البيانات على معلومات حول أكثر من **53,000 حادث صناعي وتكنولوجي** في فرنسا.

        تتيح لنا البيانات المفتوحة استكشاف كيفية تغير المخاطر الصناعية عبر الزمن والمناطق والقطاعات.
        """,
        "why_open_title": "#### أهمية البيانات المفتوحة",
        "why_open_points": """
        - تعزز الشفافية والمساءلة العامة.
        - تمكن الباحثين وصناع القرار من فهم المخاطر الصناعية بشكل أفضل.
        - تشجع على اتخاذ القرارات القائمة على الأدلة ودعم جهود الوقاية.
        """,
        "dashboard_title": "#### ما يقدمه لوحة التحكم هذه",
        "dashboard_points": """
        - استكشاف البيانات من خلال الرسوم البيانية التفاعلية بدلاً من تصفح آلاف السجلات.
        - تسليط الضوء على الاتجاهات الرئيسية والأنماط الجغرافية والمخاطر القطاعية.
        - تحويل تقارير الحوادث الخام إلى رؤى أسهل للفهم والتواصل.
        """,
        "nb_note": "**ملاحظة**: لا تعني الزيادة في الحوادث المبلغ عنها دائمًا أن المواقع أصبحت أكثر خطورة، بل قد تنتج عن تحسين التبليغ والرقابة."
    },
    "zh": {
        "header": "1. 简介",
        "hook_title": "### 为什么这很重要？",
        "hook_text": """
        工业事故对人们的生活、当地社区和环境有着重大影响。例如**图卢兹AZF化工厂爆炸 (2001)** 和**鲁昂Lubrizol工厂火灾 (2019)** 等事件提醒我们，技术风险仍是现代社会面临的重大挑战。

        通过研究过去的事故，我们可以更好地了解风险发生的位置，识别共同原因，并找出需要改进安全措施的领域。
        """,
        "caption_toulouse": "历史重大工业灾害背景 (图卢兹 AZF)",
        "caption_rouen": "2019年9月26日，超过240名消防员被派往鲁昂附近的Lubrizol工厂扑灭火灾",
        "context_title": "2. 背景与开放数据",
        "context_text": """
        本项目的分析基于由 **BARPI** 维护的 **ARIA (事故分析、研究与信息)** 数据库。该数据集包含超过 **53,000 起工业和技术事故** 的记录，为深入了解法国的事故模式提供了宝贵的数据支持。

        利用该开放数据集，我们可以探索工业风险如何随时间、区域和不同行业部门发生变化。
        """,
        "why_open_title": "#### 为什么开放数据很重要",
        "why_open_points": """
        - 公众获取安全相关数据促进了透明度与问责制。
        - 开放数据集使研究人员、学生和政策制定者能够更好地理解工业风险。
        - 提供数据有助于推动基于事实的决策并支持风险预防工作。
        """,
        "dashboard_title": "#### 本仪表板带来的价值",
        "dashboard_points": """
        - 用户可以通过交互式可视化探索数据，而无需逐条浏览数万条记录。
        - 仪表板突出了关键趋势、地理分布模式和特定行业的风险。
        - 将原始事故报告转化为更易于理解和传达的洞察。
        """,
        "nb_note": "**注**：报告事故数量的增加并不一定意味着工业场地变得更加危险，这也可能是由于报告要求更加严格和监管力度加强的结果。"
    }
}

def render_image_spot(image_path, caption):
    # Renders a local image.
    st.image(image_path, caption=caption)

def render_intro(df_raw, lang: str = "en"):
    """
    Renders Section 1: Introduction with multi-language support.
    Fallback to English if lang code is not found.
    """
    t = INTRO_TRANSLATIONS.get(lang, INTRO_TRANSLATIONS["en"])

    # 1. The hook
    st.header(t["header"])
    st.markdown(t["hook_title"])
    st.markdown(t["hook_text"])
    
    # Image Spot 1: Story Hook Visual
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        render_image_spot("assets/toulouse.jpg", t["caption_toulouse"])
    with col_img2:
        render_image_spot("assets/rouen.avif", caption=t["caption_rouen"])
        
    st.divider()

    # 2. Context
    st.subheader(t["context_title"])
    st.markdown(t["context_text"])
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(t["why_open_title"])
        st.markdown(t["why_open_points"])
    with c2:
        st.markdown(t["dashboard_title"])
        st.markdown(t["dashboard_points"])
        
    st.markdown(t["nb_note"])