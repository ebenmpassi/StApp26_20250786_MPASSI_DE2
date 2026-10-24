import streamlit as st

from sections.intro import render_image_spot
from utils.viz import (
    interactive_france_map,
    map_departements,
    bar_chart_top_naf,
    treemap_naf_accident_type,
    donut_chart_clp_hazards,
    correlation_causes_consequences_heatmap,
    text_mining_keywords_chart,
)

DEEP_DIVES_TRANSLATIONS = {
    "en": {
        "header": "3. Key Insights & Departmental Visualizations",
        "no_data": "No data available for the selected department or date filters.",
        "v1_title": "1. Interactive Departmental Risk Map of France",
        "v1_text": """
        * **Key Question**: *Where are industrial hazards most concentrated across France?* Major incidents in high-density industrial clusters present elevated risks to local populations and regional ecosystems.
        * **Overview**: This interactive choropleth map illustrates the distribution of reported industrial accidents across French metropolitan departments using official administrative boundaries.
        * **Key Insights**: Key industrial hubs including **Seine-Maritime (76)**, **Bouches-du-Rhône (13)**, **Nord (59)**, and **Rhône (69)** exhibit the highest total volume of recorded events.
        * **Implications**: Emergency responders and regional environmental agencies in these hotspot departments must maintain rapid-response containment infrastructure and conduct frequent site audits.
        """,
        "v2_title": "2. Correlation: Root Causes vs. Real-World Consequences",
        "v2_text": """
        When an industrial incident happens, what actually goes wrong, and where does the damage land?

        This matrix crosses declared **root causes** against observed **consequences** on the ground:

        * **Internal property damage** (*Dommages matériels*) dominates across every category, accounting for **35% to 46%** of all reported consequences.
        * **Human safety takes the biggest hit from operational breakdowns:** Deficiencies in **Work Supervision** (*Organisation du travail*) and **Operating Procedures** (*Procédures et consignes*) lead to the highest rates of worker injuries at **15.7%** and **15.0%** respectively.
        * **Environmental risks stem from inspection gaps:** Lapses in **Inspection Controls** (*Organisation des contrôles*) show higher relative impacts on **Air (11.4%)** and **Water (11.8%)** compared to standard operational errors.

        **Takeaway:** A one-size-fits-all safety policy won't work. Preventing worker injuries requires fixing day-to-day supervision and procedures, while protecting the local environment depends on stricter inspection and control monitoring.
        """,
        "v3_title": "3. Text Mining: Most Frequent Keywords in Incident Narratives",
        "v3_text": """
        What do field reports actually talk about when safety incidents occur?

        By mining the free-text narratives Content, we can extract the specific technical keywords and event types that appear most often:

        * **Fire and leaks dominate the data:** **Incendie** (Fire occurrences) and **Fuite** (Leak occurrences) far outpace every other keyword in field feedback.
        * **Primary physical culprits:** Among hardware components, **Cuve** (Tank) and **Vanne** (Valve) show up most frequently, followed closely by **Explosion** (3.7k).
        * **Auxiliary equipment failures:** Secondary components like **Pompe** (Pump), **Réservoir** (Storage Reservoir), **Tuyauterie** (Piping), and **Joint** (Gasket) account for thousands of additional reported failures.

        **Takeaway:** While catastrophic events like explosions grab headlines, day-to-day site risks are overwhelmingly driven by containment losses (*leaks*) and thermal/fire hazards (*incendie*)—making valve maintenance, tank integrity checks, and leak detection systems prime targets for preventive audits.
        """,
        "v4_title": "4. Department Ranking: Top 20 Hotspots for Industrial Accidents",
        "v4_text": """
        Which regions carry the heaviest industrial accident burden in France?

        This chart ranks the top 20 French departments by total recorded industrial incidents:

        * **The top industrial hotspots:** **Nord (59)** leads all departments with nearly 1,900 recorded incidents, closely followed by **Bouches-du-Rhône (13)**.
        * **The major manufacturing corridors:** **Rhône (69)**, **Isère (38)**, and **Seine-Maritime (76)** round out the top five, driven by heavy chemical corridors, refining sites, and port logistics.
        * **Regional concentration:** The top 5 departments account for a steep drop-off compared to the rest, highlighting that safety risks are heavily concentrated in key industrial hubs rather than evenly distributed across France.

        **Takeaway:** Inspection budgets and DREAL oversight resources should be allocated proportionally to these high-volume departments—particularly Nord (59) and Bouches-du-Rhône (13)—to maximize the impact of regulatory audits.
        """,
        "v5_title": "5. Top 10 Impacted Sectors by Activity Code (NAF)",
        "v5_text": """
        Which economic activities generate the highest volume of reported safety incidents?

        This scatter plot highlights the top 10 industrial sectors based on total reported events across France:

        * **Road freight leads the pack:** **Transports routiers de fret** (Road freight transport) ranks #1 with more than 2,787 reported incidents, reflecting the high operational risks inherent in hazardous material transport and logistics.
        * **High-volume surprises:** **Culture et élevage associés** (Farming & agriculture) comes in at #2, followed closely by **Distribution de combustibles gazeux**.
        * **Chemicals, storage, and waste:** **Basic organic chemicals manufacturing**, **Warehousing & storage**, and **Waste collection & recovery** complete the top high-risk activity branches.

        **Takeaway:** Industrial safety isn't restricted to fixed factory sites. High-incidence sectors like freight transport, gas distribution networks, and agricultural operations require dedicated mobile safety standards and specialized transit protocols.
        """,
        "v6_title": "6. Hierarchical Risk Breakdown: Sectors and Incident Types",
        "v6_text": """
        How do accident types differ depending on the economic activity?

        This treemap breaks down top industrial sectors into their dominant accident classifications (ARIA codes):

        * **Road Freight Transport (*Transports routiers de fret*):** Massively dominated by **TMDROUTE** (Dangerous Goods Transport Accidents).
        * **Gas Distribution Networks (*Distribution de combustibles gazeux*):** Almost exclusively driven by **CANADISTRIGAZ** (Gas Distribution Pipeline incidents).
        * **Agriculture & Farming (*Culture et élevage*):** Concentrated almost entirely under **IC** (*Installations Classées* / Regulated Industrial Facilities).
        * **Private Use & Residential (*Particuliers*):** Dominated by gas utilization hazards like **UTILGAZ** and **UTILGAZ,ASP**.

        **Takeaway:** Risk mitigation strategies must target sector-specific mechanisms—focusing on road transport enforcement for freight companies, pipeline monitoring for gas distributors, and facility compliance (*IC*) for agricultural operations.
        """,
        "v7_title": "7. Chemical & Physical Danger Classes (CLP Regulation)",
        "v7_text": """
        Which chemical and physical hazard classes are most frequently involved in industrial incidents?

        This breakdown categorizes involved hazardous substances according to the European CLP regulation:

        * **Flammable gases under pressure lead by a wide margin:** **Gaz inflammable, Flam. Gas 1, Press. Gas** represents **58.5%** of all recorded CLP hazard events.
        * **Carcinogens and health hazards:** **Cancérogénicité, Carc. 2** (Suspected human carcinogens) represents the second largest share at **26.0%**, with **Carc. 1B** adding another **3.16%**.
        * **Combined share:** Together, flammable pressurized gases and carcinogenic health hazards account for over **87%** of all categorized chemical danger events in the dataset.

        **Takeaway:** Risk management must prioritize pressurized gas handling protocols and long-term containment for carcinogenic substances, ensuring strict compliance with European CLP labeling, storage thresholds, and safety distance buffers.
        """,
        "v7_caption": "CLP Chemical Danger Labels & Hazardous Substances"
    },
    "fr": {
        "header": "3. Analyses Approfondies & Visualisations Départementales",
        "no_data": "Aucune donnée disponible pour le département ou les filtres de dates sélectionnés.",
        "v1_title": "1. Carte Interactive des Risques par Département",
        "v1_text": """
        * **Question clé** : *Où les risques industriels sont-ils les plus concentrés en France ?* Les incidents majeurs dans les clusters industriels denses présentent des risques élevés pour les populations.
        * **Aperçu** : Cette carte choroplèthe interactive illustre la répartition des accidents industriels signalés à travers les départements français.
        * **Enseignements clés** : Les grands hubs comme **Seine-Maritime (76)**, **Bouches-du-Rhône (13)**, **Nord (59)** et **Rhône (69)** enregistrent le volume le plus élevé d'événements.
        * **Implications** : Les services d'urgence et les agences environnementales de ces départements doivent maintenir une infrastructure d'intervention rapide.
        """,
        "v2_title": "2. Corrélation : Causes Profondes vs Conséquences Réelles",
        "v2_text": """
        Lorsqu'un incident industriel survient, qu'est-ce qui échoue réellement et où se situent les dommages ?

        Cette matrice croise les **causes profondes** déclarées aux **conséquences** observées :

        * **Les dommages matériels internes** (*Dommages matériels*) dominent chaque catégorie, représentant **35% à 46%** de toutes les conséquences signalées.
        * **La sécurité humaine est la plus touchée par les défaillances opérationnelles** : Les lacunes dans la **Supervision** (*Organisation du travail*) et les **Procédures** (*Procédures et consignes*) entraînent les taux de blessures les plus élevés (**15,7%** et **15,0%**).
        * **Les risques environnementaux découlent des manques de contrôle** : L'**Organisation des contrôles** montre un impact plus élevé sur l'**Air (11,4%)** et l'**Eau (11,8%)**.

        **À retenir** : Une politique de sécurité unique ne peut pas fonctionner. Prévenir les blessures nécessite de revoir l'encadrement quotidien, tandis que protéger l'environnement exige des contrôles plus stricts.
        """,
        "v3_title": "3. Text Mining : Mots-Clés les plus Fréquents dans les Récits",
        "v3_text": """
        De quoi parlent réellement les rapports de terrain lorsque des incidents surviennent ?

        L'analyse textuelle du contenu permet d'extraire les termes techniques les plus fréquents :

        * **Le feu et les fuites dominent** : **Incendie** et **Fuite** dépassent largement tous les autres mots-clés.
        * **Équipements principaux en cause** : Parmi les composants matériels, **Cuve** et **Vanne** apparaissent le plus souvent, suivis de près par **Explosion** (3,7k).
        * **Défaillances d'équipements auxiliaires** : Les composants comme **Pompe**, **Réservoir**, **Tuyauterie** et **Joint** représentent des milliers de défaillances supplémentaires.

        **À retenir** : Alors que les explosions font les gros titres, les risques quotidiens sont dominés par les pertes de confinement (*fuites*) et les risques thermiques (*incendie*).
        """,
        "v4_title": "4. Classement des Départements : Top 20 des Zones à Risque",
        "v4_text": """
        Quelles régions supportent la plus lourde charge d'accidents industriels en France ?

        Ce graphique classe le Top 20 des départements par nombre d'incidents :

        * **Les zones les plus touchées** : Le **Nord (59)** arrive en tête avec près de 1 900 incidents, suivi de près par les **Bouches-du-Rhône (13)**.
        * **Grands couloirs industriels** : Le **Rhône (69)**, l'**Isère (38)** et la **Seine-Maritime (76)** complètent le Top 5.
        * **Concentration régionale** : Les 5 premiers départements concentrent une grande partie des risques par rapport au reste du territoire.

        **À retenir** : Les budgets d'inspection et les ressources de la DREAL doivent être alloués en priorité à ces départements à fort volume.
        """,
        "v5_title": "5. Top 10 des Secteurs Industriels les plus Impactés (Code NAF)",
        "v5_text": """
        Quelles activités économiques génèrent le plus grand volume d'incidents ?

        Ce graphique met en évidence les 10 principaux secteurs d'activité :

        * **Le transport routier en tête** : **Transports routiers de fret** se classe #1 avec plus de 2 787 incidents signalés.
        * **Secteurs à fort volume** : **Culture et élevage associés** arrive en #2, suivi de près par la **Distribution de combustibles gazeux**.
        * **Chimie, stockage et déchets** : La fabrication de produits chimiques de base, l'entreposage et la collecte des déchets complètent les branches à risque.

        **À retenir** : La sécurité ne se limite pas aux usines fixes ; le transport de fret et la distribution de gaz nécessitent des normes de sécurité mobiles adaptées.
        """,
        "v6_title": "6. Répartition Hiérarchique des Risques : Secteurs et Types d'Accidents",
        "v6_text": """
        Comment les types d'accidents varient-ils selon l'activité économique ?

        Ce treemap décompose les secteurs industriels selon les codes ARIA :

        * **Transport routier de fret** : Largement dominé par **TMDROUTE** (Accidents de transport de marchandises dangereuses).
        * **Distribution de gaz** : Presque exclusivement dominée par **CANADISTRIGAZ** (Incidents sur canalisations de gaz).
        * **Agriculture** : Concentrée sous la catégorie **IC** (*Installations Classées*).
        * **Particuliers** : Dominés par les risques d'utilisation du gaz comme **UTILGAZ**.

        **À retenir** : Les stratégies de prévention doivent cibler les mécanismes spécifiques à chaque secteur.
        """,
        "v7_title": "7. Classes de Danger Chimique et Physique (Réglementation CLP)",
        "v7_text": """
        Quelles classes de danger chimique et physique sont les plus fréquemment impliquées ?

        Cette répartition catégorise les substances selon la réglementation européenne CLP :

        * **Les gaz inflammables sous pression en tête** : **Gaz inflammable, Flam. Gas 1, Press. Gas** représente **58,5%** des événements.
        * **Cancérogènes et risques pour la santé** : **Cancérogénicité, Carc. 2** représente **26,0%**, avec **Carc. 1B** ajoutant **3,16%**.
        * **Part combinée** : Ensemble, les gaz inflammables et les substances cancérogènes représentent plus de **87%** des événements catégorisés.

        **À retenir** : La gestion des risques doit prioriser les protocoles de manipulation des gaz sous pression et le confinement des substances cancérogènes.
        """,
        "v7_caption": "Étiquettes de danger chimique CLP et substances dangereuses"
    },
    "es": {
        "header": "3. Análisis Profundo y Visualizaciones Departamentales",
        "no_data": "No hay datos disponibles para el departamento o rango de fechas seleccionado.",
        "v1_title": "1. Mapa Interactivo de Riesgo por Departamento en Francia",
        "v1_text": """
        * **Pregunta clave**: *¿Dónde se concentran más los peligros industriales en Francia?* Los principales incidentes en zonas industriales de alta densidad representan elevados riesgos.
        * **Visión general**: Este mapa coroplético ilustra la distribución de accidentes industriales entre los departamentos franceses.
        * **Datos clave**: Centros como **Seine-Maritime (76)**, **Bouches-du-Rhône (13)**, **Nord (59)** y **Rhône (69)** presentan el mayor volumen de eventos.
        * **Implicaciones**: Los servicios de emergencia y las agencias ambientales de estos departamentos deben mantener infraestructura de respuesta rápida.
        """,
        "v2_title": "2. Correlación: Causas Raíz vs Consecuencias Reales",
        "v2_text": """
        Cuando ocurre un incidente industrial, ¿qué falla realmente y dónde se producen los daños?

        Esta matriz cruza las **causas raíz** declaradas con las **consecuencias** observadas:

        * **Daños materiales internos** (*Dommages matériels*) dominan todas las categorías, representando del **35% al 46%** de las consecuencias.
        * **La seguridad humana sufre más por fallos operativos**: Las deficiencias en **Supervisión** (*Organisation du travail*) y **Procedimientos** (*Procédures et consignes*) causan las mayores tasas de lesiones.
        * **Riesgos ambientales por falta de inspección**: Lapses en controles muestran mayor impacto relativo en **Aire (11.4%)** y **Agua (11.8%)**.

        **Conclusión**: Una política de seguridad única no funciona; prevenir lesiones requiere mejorar la supervisión diaria, mientras proteger el medio ambiente exige controles más estrictos.
        """,
        "v3_title": "3. Minería de Texto: Palabras Clave Frecuentes en Narrativas",
        "v3_text": """
        ¿De qué hablan realmente los informes de campo cuando ocurren incidentes?

        Al analizar el texto de los informes, extraemos las palabras clave técnicas más frecuentes:

        * **Incendios y fugas dominan**: **Incendie** (Incendio) y **Fuite** (Fuga) superan con creces cualquier otro término.
        * **Principales componentes afectados**: **Cuve** (Tanque) y **Vanne** (Válvula) aparecen con mayor frecuencia, seguidos por **Explosion** (3.7k).
        * **Fallas de equipos auxiliares**: **Pompe** (Bomba), **Réservoir** (Depósito), **Tuyauterie** (Tubería) y **Joint** (Junta) suman miles de fallas adicionales.

        **Conclusión**: Mientras que las explosiones acaparan titulares, los riesgos diarios están dominados por fugas e incendios.
        """,
        "v4_title": "4. Ranking Departamental: Top 20 Puntos Críticos de Accidentes",
        "v4_text": """
        ¿Qué regiones soportan la mayor carga de accidentes industriales en Francia?

        Este gráfico clasifica los 20 principales departamentos por total de incidentes:

        * **Los principales puntos críticos**: **Nord (59)** lidera con casi 1,900 incidentes, seguido de cerca por **Bouches-du-Rhône (13)**.
        * **Corredores industriales principales**: **Rhône (69)**, **Isère (38)** y **Seine-Maritime (76)** completan el Top 5.
        * **Concentración regional**: Los 5 departamentos principales concentran la mayor parte del riesgo en Francia.

        **Conclusión**: Los presupuestos de inspección deben asignarse proporcionalmente a estos departamentos de alto volumen.
        """,
        "v5_title": "5. Top 10 Sectores Industriales más Impactados (Código NAF)",
        "v5_text": """
        ¿Qué actividades económicas generan el mayor volumen de incidentes reportados?

        Este gráfico destaca los 10 sectores industriales principales:

        * **Transporte por carretera a la cabeza**: **Transports routiers de fret** ocupa el puesto #1 con más de 2,787 incidentes reportados.
        * **Sectores de alto volumen**: **Culture et élevage asociados** ocupa el puesto #2, seguido de **Distribution de combustibles gazeux**.
        * **Química, almacenamiento y residuos**: La fabricación de productos químicos, el almacenamiento y la recolección de residuos completan las ramas de mayor riesgo.

        **Conclusión**: La seguridad industrial debe incluir protocolos específicos para el transporte de mercancías y redes de gas.
        """,
        "v6_title": "6. Desglose Jerárquico de Riesgos: Sectores y Tipos de Incidentes",
        "v6_text": """
        ¿Cómo varían los tipos de accidentes según la actividad económica?

        Este mapa de árbol desglosa los sectores industriales según sus códigos ARIA:

        * **Transporte de mercancías por carretera**: Dominado por **TMDROUTE** (Accidentes de transporte de mercancías peligrosas).
        * **Redes de distribución de gas**: Dominado por **CANADISTRIGAZ** (Incidentes en tuberías de gas).
        * **Agricultura**: Concentrada en la categoría **IC** (*Installations Classées*).
        * **Uso residencial/particular**: Dominado por riesgos de uso de gas como **UTILGAZ**.

        **Conclusión**: Las estrategias de mitigación deben adaptarse a los mecanismos específicos de cada sector.
        """,
        "v7_title": "7. Clases de Peligro Químico y Físico (Reglamento CLP)",
        "v7_text": """
        ¿Qué clases de peligro químico y físico están más frecuentemente involucradas?

        Este desglose categoriza las sustancias peligrosas según la normativa europea CLP:

        * **Gases inflamables bajo presión lideran**: **Gaz inflammable, Flam. Gas 1, Press. Gas** representa el **58.5%** de los eventos.
        * **Carcinógenos y riesgos para la salud**: **Cancérogénicité, Carc. 2** representa el **26.0%**, con **Carc. 1B** sumando otro **3.16%**.
        * **Cuota combinada**: Juntos representan más del **87%** de los eventos químicos categorizados.

        **Conclusión**: La gestión de riesgos debe priorizar la manipulación de gases a presión y la contención de sustancias carcinógenas.
        """,
        "v7_caption": "Etiquetas de peligro químico CLP y sustancias peligrosas"
    },
    "ar": {
        "header": "3. التحليلات العميقة والرسوم البيانية للمقاطعات",
        "no_data": "لا تتوفر بيانات للمقاطعة أو نطاق التاريخ المحدد.",
        "v1_title": "1. خريطة المخاطر التفاعلية للمقاطعات الفرنسية",
        "v1_text": """
        * **السؤال الرئيسي**: *أين تتركز المخاطر الصناعية بشكل أكبر في فرنسا؟* تشكل الحوادث الكبرى في التجمعات الصناعية المكتظة مخاطر مرتفعة.
        * **نظرة عامة**: توضح هذه الخريطة التفاعلية توزيع الحوادث الصناعية المبلغ عنها عبر المقاطعات الفرنسية.
        * **الرؤى الرئيسية**: تسجل المراكز الرئيسية مثل **Seine-Maritime (76)** و **Bouches-du-Rhône (13)** و **Nord (59)** و **Rhône (69)** أعلى إجمالي للحوادث.
        * **الآثار المترتبة**: يجب على أجهزة الطوارئ ووكالات البيئة في هذه المقاطعات الحفاظ على البنية التحتية للاستجابة السريعة.
        """,
        "v2_title": "2. الارتباط: الأسباب الجذرية مقابل العواقب الفعلية",
        "v2_text": """
        عند وقوع حادث صناعي، ما الذي يفشل بالفعل، وأين تقع الأضرار؟

        تقاطع هذه مصفوفة بين **الأسباب الجذرية** المصرح بها و**العواقب** المرصودة:

        * **الأضرار المادية الداخلية** (*Dommages matériels*) تهيمن على كل فئة، حيث تشكل **35% إلى 46%** من إجمالي العواقب.
        * **السلامة البشرية تتأثر بشكل أكبر بالأعطال التشغيلية**: تؤدي القصور في **الإشراف** و**إجراءات التشغيل** إلى أعلى معدلات إصابات العمال.
        * **المخاطر البيئية تنجم عن فجوات التفتيش**: تظهر قصور عمليات التفتيش تأثيرات أعلى على **الهواء (11.4%)** و**الماء (11.8%)**.

        **النتيجة**: لا يمكن لسياسة سلامة واحدة أن تنجح؛ تتطلب الوقاية من الإصابات تحسين الإشراف اليومي، بينما تتطلب حماية البيئة رقابة أشد.
        """,
        "v3_title": "3. التنقيب في النصوص: الكلمات المفتاحية الأكثر تكراراً في التقارير",
        "v3_text": """
        عن ماذا تتحدث التقارير الميدانية بالفعل عند وقوع حوادث السلامة؟

        من خلال تحليل النصوص الحرة، يمكننا استخراج الكلمات المفتاحية الفنية الأكثر تكراراً:

        * **الحرائق والتسربات تهيمن على البيانات**: يتفوق **Incendie** (حريق) و **Fuite** (تسرب) بفارق كبير على باقي الكلمات.
        * **المكونات الفيزيائية الرئيسية**: تظهر **Cuve** (خزان) و **Vanne** (صمام) بشكل متكرر، يليها **Explosion** (انفجار).
        * **أعطال المعدات الثانوية**: تسجل **Pompe** (مضخة) و **Tuyauterie** (أنابيب) و **Joint** (وصلة) آلاف الأعطال الإضافية.

        **النتيجة**: بينما تتصدر الانفجارات العناوين، فإن المخاطر اليومية تقودها التسربات الحرارية والحرائق.
        """,
        "v4_title": "4. تصنيف المقاطعات: أعلى 20 منطقة تسجيلًا للحوادث الصناعية",
        "v4_text": """
        ما هي المناطق التي تتحمل العبء الأكبر من الحوادث الصناعية في فرنسا؟

        يصنف هذا الرسم البياني أعلى 20 مقاطعة فرنسية حسب إجمالي الحوادث:

        * **أبرز المناطق الصناعية**: تتصدر **Nord (59)** بـ 1,900 حادث تقريبًا، تليها **Bouches-du-Rhône (13)**.
        * **الممرات الصناعية الرئيسية**: تكتمل المراكز الخمسة الأولى بـ **Rhône (69)** و **Isère (38)** و **Seine-Maritime (76)**.
        * **التركز الإقليمي**: تركز المقاطعات الخمس الأولى معظم المخاطر الصناعية في البلاد.

        **النتيجة**: يجب تخصيص ميزانيات التفتيش والموارد بشكل متناسب مع هذه المقاطعات ذات الحجم المرتفع.
        """,
        "v5_title": "5. أعلى 10 قطاعات صناعية تأثراً (رمز NAF)",
        "v5_text": """
        ما هي الأنشطة الاقتصادية التي تولد أعلى حجم من الحوادث المسجلة؟

        يسلط هذا الرسم البياني الضوء على أعلى 10 قطاعات صناعية:

        * **النقل البري للبضائع يتصدر**: يأت **Transports routiers de fret** في المرتبة الأولى بـ أكثر من 2,787 حادثًا.
        * **قطاعات ذات حجم مرتفع**: يأتي **Culture et élevage associés** (الزراعة) في المرتبة الثانية، يليه **Distribution de combustibles gazeux** (توزيع الغاز).
        * **الكيماويات والتخزين والنفايات**: تكتمل القائمة بتصنيع الكيماويات العضوية والتخزين وجمع النفايات.

        **النتيجة**: السلامة الصناعية لا تقتصر على المصانع؛ تتطلب قطاعات نقل البضائع وشبكات الغاز معايير سلامة خاصة.
        """,
        "v6_title": "6. التفكيك الهيكلي للمخاطر: القطاعات وأنواع الحوادث",
        "v6_text": """
        كيف تختلف أنواع الحوادث باختلاف النشاط الاقتصادي؟

        يطبق هذا الخريطة الشجرية تفكيكًا للقطاعات الصناعية حسب تصنيفات ARIA:

        * **النقل البري للبضائع**: يهيمن عليه **TMDROUTE** (حوادث نقل البضائع الخطرة).
        * **شبكات توزيع الغاز**: يهيمن عليها **CANADISTRIGAZ** (حوادث أنابيب الغاز).
        * **الزراعة**: تتركز تقريبًا تحت **IC** (*المنشآت المصنفة*).
        * **الاستخدام الخاص/السكني**: تهيمن عليه مخاطر استخدام الغاز مثل **UTILGAZ**.

        **النتيجة**: يجب أن تستهدف استراتيجيات الحد من المخاطر الآليات الخاصة بكل قطاع.
        """,
        "v7_title": "7. فئات المخاطر الكيميائية والفيزيائية (لائحة CLP)",
        "v7_text": """
        ما هي فئات المخاطر الكيميائية والفيزيائية الأكثر إشراكًا في الحوادث؟

        يصنف هذا التوزيع المواد الخطرة وفقًا للائحة CLP الأوروبية:

        * **الغازات القابلة للاشتعال تحت الضغط تتصدر بفارق كبير**: تمثل **Gaz inflammable** نسبة **58.5%** من الحوادث.
        * **المواد المسرطنة والمخاطر الصحية**: تمثل **Cancérogénicité, Carc. 2** نسبة **26.0%**، مع إضافة **Carc. 1B** نسبة **3.16%**.
        * **الحصة المشتركة**: تشكل الغازات المضغوطة والمواد المسرطنة أكثر من **87%** من الحوادث المصنفة.

        **النتيجة**: يجب أن تعطي إدارة المخاطر الأولوية لبروتوكولات التعامل مع الغازات المضغوطة واحتواء المواد المسرطنة.
        """,
        "v7_caption": "ملصقات المخاطر الكيميائية CLP والمواد الخطرة"
    },
    "zh": {
        "header": "3. 核心洞察与各省可视化分析",
        "no_data": "所选省份或日期筛选条件下无可用数据。",
        "v1_title": "1. 法国各省风险交互式地图",
        "v1_text": """
        * **核心问题**：*法国的工业危险主要集中在哪里？* 高密度工业集群中的重大事故对当地人口和生态系统构成较高风险。
        * **概述**：该交互式分级统计图使用官方行政边界展示了法国各省报告的工业事故分布。
        * **核心洞察**：包括 **Seine-Maritime (76)**、**Bouches-du-Rhône (13)**、**Nord (59)** 和 **Rhône (69)** 在内的主要工业枢纽记录的事故总量最高。
        * **启示**：这些热点省份的应急响应人员和区域环保机构必须维持快速响应机制并开展频繁的现场审计。
        """,
        "v2_title": "2. 相关性分析：根本原因 vs 实际后果",
        "v2_text": """
        当工业事故发生时，究竟是哪个环节出了问题，损失又发生在何处？

        该矩阵将申报的**根本原因**与地面观察到的**实际后果**进行了交叉分析：

        * **内部财产损失** (*Dommages matériels*) 在各个类别中都占主导地位，占所有报告后果的 **35% 至 46%**。
        * **人员安全受操作失误影响最大**：**工作监督** (*Organisation du travail*) 和 **操作规程** (*Procédures et consignes*) 的缺陷导致工人受伤率最高（分别为 **15.7%** 和 **15.0%**）。
        * **环境风险源于检查缺失**：**检查控制** (*Organisation des contrôles*) 的疏漏对 **空气 (11.4%)** 和 **水质 (11.8%)** 的相对影响高于标准操作失误。

        **核心要点**：一刀切的安全政策行不通。预防工人受伤需要改善日常监督和规程，而保护局部环境则依赖于更严格的检查与监控。
        """,
        "v3_title": "3. 文本挖掘：事故叙述中最频繁的高频词",
        "v3_text": """
        当安全事故发生时，现场报告究竟在讨论什么？

        通过对文本内容进行挖掘，我们可以提取出最频繁出现的具体技术关键词和事件类型：

        * **火灾和泄漏主导数据**：**Incendie**（火灾）和 **Fuite**（泄漏）在现场反馈中远超其他关键词。
        * **主要物理诱因**：在硬件部件中，**Cuve**（罐体）和 **Vanne**（阀门）出现频率最高，紧随其后的是 **Explosion**（爆炸，3.7k）。
        * **辅助设备故障**：像 **Pompe**（泵）、**Réservoir**（储罐）、**Tuyauterie**（管道）和 **Joint**（垫圈）等次要部件也占了数千起故障报告。

        **核心要点**：虽然爆炸等灾难性事件备受关注，但日常场地风险主要由密封失效（*泄漏*）和热/火灾隐患（*火灾*）驱动——这使得阀门维护、罐体完整性检查和泄漏检测系统成为预防性审计的重点。
        """,
        "v4_title": "4. 省份排名：工业事故 Top 20 热点地区",
        "v4_text": """
        法国哪些地区的工业事故负担最重？

        该图表按记录的工业事故总数对前 20 个法国省份进行了排名：

        * **顶级工业热点**：**Nord (59)** 以近 1,900 起记录事故位居榜首，紧随其后的是 **Bouches-du-Rhône (13)**。
        * **主要制造走廊**：**Rhône (69)**、**Isère (38)** 和 **Seine-Maritime (76)** 位列前五，受重化工走廊、炼油厂和港口物流驱动。
        * **区域集中度**：前 5 个省份与其他省份相比存在陡峭的断层，表明安全风险高度集中在关键工业枢纽，而非均匀分布。

        **核心要点**：检查预算和监管资源应按比例分配给这些事故量高的省份（特别是 Nord 和 Bouches-du-Rhône），以最大化监管审计的效果。
        """,
        "v5_title": "5. 按活动代码 (NAF) 划分的前 10 大受影响行业",
        "v5_text": """
        哪些经济活动产生的报告安全事故数量最多？

        该散点图突出了全法范围内基于总报告事件数量的前 10 个工业部门：

        * **公路货运领跑**：**Transports routiers de fret**（公路货运）以超过 2,787 起报告事故排名第一，反映了危险货物运输和物流中固有的高操作风险。
        * **高事故量行业**：**Culture et élevage associés**（农业与畜牧业）位居第二，紧随其后的是 **Distribution de combustibles gazeux**（管道气体燃料输送）。
        * **化工、仓储与废弃物**：基础有机化学品制造、仓储以及废弃物收集与回收构成了其余的高风险行业分支。

        **核心要点**：工业安全并不局限于固定工厂场所。公路货运、天然气输送网络和农业作业等高发行业需要专门的移动安全标准和运输协议。
        """,
        "v6_title": "6. 风险层级拆解：行业与事故类型",
        "v6_text": """
        根据经济活动的不同，事故类型有何差异？

        该树状图将主要工业部门拆解为其主导的事故分类（ARIA 代码）：

        * **公路货运 (*Transports routiers de fret*)**：主要由 **TMDROUTE**（危险货物运输事故）为主导。
        * **天然气输送网络 (*Distribution de combustibles gazeux*)**：几乎完全由 **CANADISTRIGAZ**（输气管道事故）驱动。
        * **农业与种植业 (*Culture et élevage*)**：几乎完全集中在 **IC**（*Installations Classées* / 监管工业设施）下。
        * **民用与住宅 (*Particuliers*)**：由 **UTILGAZ** 等天然气使用风险为主导。

        **核心要点**：风险缓释策略必须针对特定行业的机制——重点关注货运公司的公路运输执法、气体分销商的管道监控以及农业作业的设施合规性。
        """,
        "v7_title": "7. 化学与物理危险等级 (CLP 法规)",
        "v7_text": """
        哪些化学和物理危险等级最常涉及工业事故？

        该拆解根据欧洲 CLP 法规对涉及的危险物质进行了分类：

        * **压力下易燃气体大幅领跑**：**Gaz inflammable, Flam. Gas 1, Press. Gas** 占所有记录的 CLP 危险事件的 **58.5%**。
        * **致癌物与健康危害**：**Cancérogénicité, Carc. 2**（可疑人类致癌物）占第二大份额（**26.0%**），**Carc. 1B** 占 **3.16%**。
        * **合计份额**：压力下易燃气体和致癌健康危害共同占数据集中所有分类化学危险事件的 **87%** 以上。

        **核心要点**：风险管理必须优先考虑加压气体处理协议和致癌物质的长期封存，确保严格遵守欧洲 CLP 标识、储存阈值和安全缓冲距离。
        """,
        "v7_caption": "CLP 化学危险标识与危险物质"
    }
}


def render_deep_dives(df_filtered, lang: str = "en"):
    """
    Renders Section 3: Key Insights & Departmental Visualizations with multi-language support.
    Fallback to English if lang code is not found.
    """
    t = DEEP_DIVES_TRANSLATIONS.get(lang, DEEP_DIVES_TRANSLATIONS["en"])

    st.header(t["header"])
    
    if df_filtered.empty:
        st.error(t["no_data"])
        return

    # Visualization 1: INTERACTIVE GEOGRAPHIC MAP OF FRANCE
    st.subheader(t["v1_title"])
    st.markdown(t["v1_text"])
    st.plotly_chart(interactive_france_map(df_filtered), use_container_width=True)
    st.divider()

    # Visualization 2: Correlation (ROOT CAUSES VS. CONSEQUENCES)
    st.subheader(t["v2_title"])
    st.markdown(t["v2_text"])
    st.plotly_chart(correlation_causes_consequences_heatmap(df_filtered,7), use_container_width=True)
    st.divider()

    # Visualization 3: Original text meaning analysis of accident narratives
    st.subheader(t["v3_title"])
    st.markdown(t["v3_text"])
    st.plotly_chart(text_mining_keywords_chart(df_filtered,12), use_container_width=True)
    st.divider()

    # Visualization 4: Department Impact Ranking
    st.subheader(t["v4_title"])
    st.markdown(t["v4_text"])
    st.plotly_chart(map_departements(df_filtered,20), use_container_width=True)
    st.divider()

    # Visualization 5: Top Impacted Industrial Sectors
    st.subheader(t["v5_title"])
    st.markdown(t["v5_text"])
    st.plotly_chart(bar_chart_top_naf(df_filtered,10), use_container_width=True)
    st.divider()

    # Visualization 6: Hierarchical Risk Breakdown
    st.subheader(t["v6_title"])
    st.markdown(t["v6_text"])
    st.plotly_chart(treemap_naf_accident_type(df_filtered), use_container_width=True)
    st.divider()

    # Visualization 7: CLP Hazard Classes
    st.subheader(t["v7_title"])
    st.markdown(t["v7_text"])
    
    col_img, col_donut = st.columns([1, 1])
    with col_img:
        render_image_spot("assets/substance.avif", t["v7_caption"])
    with col_donut:
        st.plotly_chart(donut_chart_clp_hazards(df_filtered,5), use_container_width=True)