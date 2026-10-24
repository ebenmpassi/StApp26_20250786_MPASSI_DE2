import re
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# URL source for GeoJSON boundary polygons representing French departments
GEOJSON_FRANCE = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"

# Standard branding color used across dashboard line elements
COLOR_PRIMARY = "#008080"  # Teal


def correlation_causes_consequences_heatmap(df, top_n: int = 7):
    # Generates a row-normalized co-occurrence heatmap matrix between Root Causes and Real Consequences.
    col_causes = 'Causes profondes' if 'Causes profondes' in df.columns else 'Root Causes'
    col_cons = 'Conséquences' if 'Conséquences' in df.columns else 'Consequences'

    # Guard clause: Verify input DataFrame is populated and required columns exist
    if df.empty or col_causes not in df.columns or col_cons not in df.columns:
        return px.imshow([[0]], title="Insufficient data for correlation matrix", template="plotly_white")

    # Drop null values across target columns
    df_sub = df.dropna(subset=[col_causes, col_cons])
    if df_sub.empty:
        return px.imshow([[0]], title="No valid records available", template="plotly_white")

    invalid_items = {'NON SPÉCIFIÉ', 'AUTRE', 'NOT SPECIFIED', 'OTHER', 'UNKNOWN', 'INCONNU', ''}

    # Vectorized extraction of top 'N' root cause categories
    causes_series = df_sub[col_causes].astype(str).str.split(',').explode().str.strip()
    causes_series = causes_series[~causes_series.str.upper().isin(invalid_items)]
    top_causes = causes_series.value_counts().head(top_n).index.tolist()

    # Vectorized extraction of top 'N' consequence categories
    cons_series = df_sub[col_cons].astype(str).str.split(',').explode().str.strip()
    cons_series = cons_series[~cons_series.str.upper().isin(invalid_items)]
    top_cons = cons_series.value_counts().head(top_n).index.tolist()

    if not top_causes or not top_cons:
        return px.imshow([[0]], title="Not enough matching pairs", template="plotly_white")

    # Prepare temporary DataFrame and explode both target columns
    temp_df = df_sub[[col_causes, col_cons]].copy()
    temp_df['Cause'] = temp_df[col_causes].astype(str).str.split(',')
    temp_df['Consequence'] = temp_df[col_cons].astype(str).str.split(',')

    # Explode both columns to create unpivoted pair rows
    df_pairs = temp_df.explode('Cause').explode('Consequence')
    df_pairs['Cause'] = df_pairs['Cause'].str.strip()
    df_pairs['Consequence'] = df_pairs['Consequence'].str.strip()

    # Filter matrix pairs to include only top N categories
    df_pairs = df_pairs[df_pairs['Cause'].isin(top_causes) & df_pairs['Consequence'].isin(top_cons)]

    if df_pairs.empty:
        return px.imshow([[0]], title="No co-occurrence pairs found", template="plotly_white")

    # FIX: Reset the index on the filtered Series before passing into pd.crosstab()
    # to eliminate duplicate index labels inherited from explode()
    cause_clean = df_pairs['Cause'].reset_index(drop=True)
    cons_clean = df_pairs['Consequence'].reset_index(drop=True)

    # Construct co-occurrence matrix safely with unique indices
    matrix = pd.crosstab(cause_clean, cons_clean).reindex(index=top_causes, columns=top_cons, fill_value=0)

    # Perform row-wise normalization
    matrix_pct = matrix.div(matrix.sum(axis=1).replace(0, 1), axis=0) * 100

    fig = px.imshow(
        matrix_pct,
        labels=dict(x="Observed Consequences", y="Declared Root Causes", color="% of Incidents"),
        x=matrix_pct.columns,
        y=matrix_pct.index,
        color_continuous_scale="YlOrRd",
        text_auto=".1f",
        title="Correlation & Co-occurrence: Root Causes vs Consequences (%)",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Observed Consequences",
        yaxis_title="Declared Root Causes",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig


def text_mining_keywords_chart(df, top_n: int=12):
    # Extracts operational and technical keyword occurrences from free-text incident narratives.
    col_text = 'Contenu' if 'Contenu' in df.columns else 'Content'

    # Guard clause: Check if textual column exists
    if df.empty or col_text not in df.columns:
        return px.bar(title="No textual content available", template="plotly_white")

    # Define target technical keywords to mine from incident narratives
    keywords = [
        "fuite", "explosion", "incendie", "vanne", "tuyauterie", 
        "surpression", "joint", "corrosion", "cuve", "purge", 
        "pompe", "réservoir", "nuage", "chaleur", "étincelle"
    ]

    # Convert narrative column to lower-case string series
    series_text = df[col_text].dropna().astype(str).str.lower()
    
    # Construct a single regex OR pattern matching word boundaries
    pattern = r'\b(' + '|'.join(keywords) + r')\b'
    
    # Perform vectorized regex match across the whole series and aggregate counts
    matches = series_text.str.findall(pattern).explode()
    counts_series = matches.value_counts().reindex(keywords, fill_value=0)

    # Format result DataFrame for Plotly Express horizontal bar rendering
    df_kw = pd.DataFrame({
        'Operational Term': [k.capitalize() for k in counts_series.index],
        'Frequency': counts_series.values
    }).sort_values('Frequency', ascending=True).tail(top_n)

    # Generate horizontal bar chart
    fig = px.bar(
        df_kw,
        x='Frequency',
        y='Operational Term',
        orientation='h',
        title="Text Mining: Most Frequent Keywords in Incident Narratives",
        color='Frequency',
        color_continuous_scale="Viridis",
        template="plotly_white"
    )
    
    # Customize hover tooltips and axis labels
    fig.update_traces(hovertemplate="<b>Term:</b> %{y}<br><b>Narrative Occurrences:</b> %{x:,}<extra></extra>")
    fig.update_layout(
        xaxis_title="Number of Textual Occurrences",
        yaxis_title="Technical Keyword",
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig


def line_chart_accidents(df):
    # Plots the annual trend of reported industrial incidents in France with milestone event markers.
    col_year = 'Annee' if 'Annee' in df.columns else 'Year'

    # Guard clause: Validate input data
    if df is None or df.empty or col_year not in df.columns:
        return px.line(title="No data available for this selection", template="plotly_white")
        
    # Group by year and calculate total count per year
    counts = df.groupby(col_year, as_index=False).size().rename(columns={col_year: 'Year', 'size': 'Number of Incidents'})
    
    # Calculate Year-over-Year percentage change
    counts['YoY_Change'] = counts['Number of Incidents'].pct_change() * 100
    counts['YoY_Text'] = counts['YoY_Change'].apply(
        lambda x: f"{x:+.1f}%" if pd.notnull(x) else "N/A"
    )
    
    # Construct line chart with markers
    fig = px.line(
        counts, 
        x='Year', 
        y='Number of Incidents', 
        title="Annual Trend of Reported Industrial Incidents in France",
        markers=True,
        color_discrete_sequence=[COLOR_PRIMARY],
        template="plotly_white",
        custom_data=['YoY_Text']
    )
    
    # Update trace styling and custom unified hover text
    fig.update_traces(
        hovertemplate="<b>Incidents:</b> %{y}<br><b>YoY Change:</b> %{customdata[0]}<extra></extra>",
        marker=dict(size=7, symbol="diamond")
    )
    
    # Add vertical reference lines for historic industrial disasters
    milestones = [
        {"year": 2001, "label": "AZF Disaster (2001)"},
        {"year": 2019, "label": "Lubrizol Fire (2019)"}
    ]
    
    max_val = counts['Number of Incidents'].max() if not counts.empty else 0
    for m in milestones:
        if m["year"] in counts['Year'].values:
            # Draw vertical dashed reference line
            fig.add_vline(
                x=m["year"], 
                line_dash="dash", 
                line_color="gray", 
                opacity=0.7
            )
            # Add text annotation at the top of the chart
            fig.add_annotation(
                x=m["year"],
                y=max_val,
                text=m["label"],
                showarrow=False,
                yshift=10,
                font=dict(size=10, color="gray")
            )

    # Format layout parameters
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Number of Incidents",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig


def bar_chart_top_naf(df, top_n: int=10):
    # Renders an interactive Scatter/Bubble plot displaying top NAF industrial activity sectors.
    col_naf = 'Code NAF' if 'Code NAF' in df.columns else 'NAF Code'

    # Guard clause: Ensure sufficient data points are present
    if df.empty or len(df) < 5 or col_naf not in df.columns:
        fig = go.Figure()
        fig.add_annotation(
            text="Sample too small (<5 incidents) to establish sector ranking",
            showarrow=False, 
            font=dict(size=14, color="gray")
        )
        fig.update_layout(template="plotly_white", xaxis_visible=False, yaxis_visible=False)
        return fig
        
    # Aggregate top NAF sectors by incident count
    top_df = df[col_naf].value_counts().head(top_n).reset_index()
    top_df.columns = ['NAF_Code', 'Count']
    top_df = top_df.sort_values('Count', ascending=True)

    counts = top_df['Count'].values
    min_count, max_count = counts.min(), counts.max()
    
    # Scale incident counts to dynamic marker pixel sizes
    sizes = np.interp(counts, (min_count, max_count), (20, 50)) if min_count != max_count else np.full_like(counts, 30)

    fig = go.Figure()

    # Add interactive scatter bubble trace
    fig.add_trace(go.Scatter(
        x=counts,
        y=top_df['NAF_Code'],
        mode='markers+text',
        text=counts,
        textposition='middle right',
        textfont=dict(size=11, color='#1E293B', family='Arial Black'),
        marker=dict(
            size=sizes,
            color=counts,
            colorscale='Sunsetdark',
            cmin=min_count,
            cmax=max_count,
            showscale=True,
            colorbar=dict(title="Incidents", len=0.8),
            line=dict(width=1.5, color='#0F172A')
        ),
        hovertemplate="<b>Industry Sector (NAF):</b> %{y}<br><b>Total Incidents:</b> %{x:,}<extra></extra>"
    ))

    # Add 15% margin padding on x-axis to prevent text labels from getting clipped
    max_x = max_count * 1.15 if max_count > 0 else 100

    fig.update_layout(
        title=dict(
            text=f"Scatter Plot: Top {top_n} Impacted Industrial Sectors in France",
            font=dict(size=16)
        ),
        xaxis_title="Number of Reported Events",
        yaxis_title="NAF Code / Industrial Activity",
        xaxis=dict(range=[0, max_x], showgrid=True, gridcolor="#E2E8F0"),
        yaxis=dict(showgrid=True, gridcolor="#F1F5F9"),
        template="plotly_white",
        margin=dict(l=20, r=20, t=50, b=20),
        height=450
    )

    return fig


def treemap_naf_accident_type(df: pd.DataFrame, top_n: int = 8):
    # Renders a hierarchical Treemap breaking down sectors into specific accident classifications.
    col_naf = 'Code NAF' if 'Code NAF' in df.columns else 'NAF Code'
    col_type = 'Type d\'accident' if 'Type d\'accident' in df.columns else 'Accident Type'

    # Guard clause: Check required columns and minimum size
    if df.empty or len(df) < 5 or col_naf not in df.columns or col_type not in df.columns:
        fig = go.Figure()
        fig.add_annotation(text="Insufficient data for hierarchical view", showarrow=False)
        fig.update_layout(template="plotly_white")
        return fig
        
    # Get top NAF sector codes
    top_nafs = df[col_naf].value_counts().head(top_n).index
    df_sub = df[df[col_naf].isin(top_nafs)]
    
    # Aggregate counts by sector and accident type
    grouped = df_sub.groupby([col_naf, col_type], as_index=False).size().rename(columns={'size': 'Count'})
    
    # Create hierarchical treemap figure
    fig = px.treemap(
        grouped,
        path=[col_naf, col_type],
        values='Count',
        title="Hierarchical Breakdown: Sector → Accident Type",
        color='Count',
        color_continuous_scale='Spectral',
        template='plotly_white'
    )
    
    fig.update_traces(hovertemplate="<b>%{label}</b><br>Incidents: %{value}<extra></extra>")
    fig.update_layout(margin=dict(l=10, r=10, t=50, b=10))
    return fig


def interactive_france_map(df: pd.DataFrame):
    # Renders an interactive Choropleth Map of France using department GeoJSON boundaries.
    col_dept = 'Département' if 'Département' in df.columns else 'Department'
    col_country = 'Pays' if 'Pays' in df.columns else 'Country'

    # Filter dataset for records originating in France
    df_fr = df[df[col_country] == 'FRANCE'] if col_country in df.columns else df
    
    if df_fr.empty or col_dept not in df_fr.columns:
        fig = go.Figure()
        fig.add_annotation(text="No geographic data available for France", showarrow=False)
        fig.update_layout(template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        return fig

    # Standardize department code strings (e.g., converts integer 1 to padded string '01')
    counts = df_fr[col_dept].value_counts().reset_index()
    counts.columns = ['Department_Code', 'Incidents']
    counts['Department_Code'] = counts['Department_Code'].astype(str).str.strip().str.zfill(2)
    
    # Exclude invalid administrative placeholders
    invalid_codes = {'UNKNOWN', 'INCONNU', 'NAN', 'NONE', 'NOT SPECIFIED'}
    counts = counts[~counts['Department_Code'].str.upper().isin(invalid_codes)]

    # Generate Choropleth map linking Department_Code to properties.code in GeoJSON
    fig = px.choropleth(
        counts,
        geojson=GEOJSON_FRANCE,
        locations='Department_Code',
        featureidkey='properties.code',
        color='Incidents',
        color_continuous_scale="Plasma",
        title="Interactive French Department Risk Map",
        template='plotly_white',
        hover_name=counts['Department_Code'].map(lambda c: f"Department {c}"),
        hover_data={'Department_Code': False, 'Incidents': True}
    )

    # Apply custom hover tooltip
    fig.update_traces(
        hovertemplate="<b>Department %{location}</b><br>Incidents: %{z}<extra></extra>"
    )
    
    # Restrict geographical display bounds tightly over Metropolitan France
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )
    
    # Transparent background layout for dashboard embedding
    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig


def map_departements(df, top_n: int=20):
    # Renders a vertical bar chart ranking the top departments by incident count.
    col_dept = 'Département' if 'Département' in df.columns else 'Department'
    col_country = 'Pays' if 'Pays' in df.columns else 'Country'

    df_fr = df[df[col_country] == 'FRANCE'] if col_country in df.columns else df
    
    if df_fr.empty or col_dept not in df_fr.columns:
        fig = go.Figure()
        fig.add_annotation(text="No department data available for this selection", showarrow=False)
        fig.update_layout(template="plotly_white")
        return fig

    # Group counts and sanitize string representation
    counts = df_fr[col_dept].value_counts().reset_index()
    counts.columns = ['Department', 'Count']
    counts['Department'] = counts['Department'].astype(str).str.strip()
    
    invalid_depts = {'UNKNOWN', 'INCONNU', 'NAN', 'NONE'}
    counts = counts[~counts['Department'].str.upper().isin(invalid_depts)].head(top_n)
    
    # Generate bar chart
    fig = px.bar(
        counts, 
        x='Department', 
        y='Count',
        title=f"Industrial Incidents by French Department (Top {top_n})",
        color='Count',
        color_continuous_scale="Viridis",
        template="plotly_white"
    )
    
    fig.update_traces(hovertemplate="<b>Department Code:</b> %{x}<br><b>Incidents Logged:</b> %{y}<extra></extra>")
    fig.update_layout(
        xaxis_title="French Department Code", 
        yaxis_title="Number of Incidents",
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig


def donut_chart_clp_hazards(df, top_n: int=5):
    # Renders a Donut Chart showing the distribution of CLP regulation danger classes.
    col_clp = 'Classe de danger CLP' if 'Classe de danger CLP' in df.columns else 'CLP Hazard Class'

    if df.empty or col_clp not in df.columns:
        fig = go.Figure()
        fig.add_annotation(text="CLP Hazard Classes not available", showarrow=False)
        fig.update_layout(template="plotly_white")
        return fig
        
    # Clean string inputs and remove unknown values
    s = df[col_clp].astype(str).str.strip()
    invalid_clp = {'NOT SPECIFIED', 'NON SPÉCIFIÉ', 'NONE', 'NAN', 'UNKNOWN'}
    s_clean = s[~s.str.upper().isin(invalid_clp) & (s != '')]

    if s_clean.empty:
        fig = go.Figure()
        fig.add_annotation(text="No CLP hazard data for current filters", showarrow=False)
        fig.update_layout(template="plotly_white")
        return fig
        
    counts = s_clean.value_counts().head(top_n).reset_index()
    counts.columns = ['CLP Class', 'Count']
    
    # Create donut chart using hole=0.45
    fig = px.pie(
        counts,
        names='CLP Class',
        values='Count',
        hole=0.45,
        title=f"Top {top_n} CLP Hazard Classes in France",
        color_discrete_sequence=px.colors.qualitative.Set3,
        template='plotly_white'
    )
    
    fig.update_traces(
        textposition='inside', 
        textinfo='percent+label', 
        hovertemplate="<b>%{label}</b><br>Count: %{value}"
    )
    
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20), showlegend=False)
    return fig


def completeness_bar_chart(report):
    # Renders a stacked horizontal bar chart analyzing data completeness vs missingness across fields.
    fields = ['Dates', 'Departments', 'NAF Code', 'Equipment', 'Root Causes', 'Consequences']
    
    # Extract missing metrics safely using dictionary defaults
    missing_pcts = [
        report.get('missing_dates_pct', 0),
        report.get('missing_deps_pct', 0),
        report.get('missing_naf_pct', 0),
        report.get('missing_equipments_pct', 0),
        report.get('missing_causes_pct', 0),
        report.get('missing_consequences_pct', 0)
    ]
    
    # Calculate completeness complementary percentages
    complete_pcts = [max(0, 100 - p) for p in missing_pcts]
    
    # Construct DataFrame for Plotly stacked bar plot
    df_quality = pd.DataFrame({
        'Field': fields,
        'Completeness (%)': complete_pcts,
        'Missing (%)': missing_pcts
    })
    
    # Build horizontal stacked bar chart
    fig = px.bar(
        df_quality,
        y='Field',
        x=['Completeness (%)', 'Missing (%)'],
        orientation='h',
        title="Data Health Check: Completeness Audit for France Dataset (%)",
        color_discrete_map={'Completeness (%)': '#10B981', 'Missing (%)': '#EF4444'},
        template='plotly_white'
    )
    
    fig.update_layout(
        barmode='stack',
        xaxis_title="Percentage (%)",
        yaxis_title="ARIA Database Fields",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig