def filter_data(df, country, date_range, deps):
    # Filters dataset according to user selections.
    filtered = df.copy()
    
    if country and country != "ALL COUNTRIES":
        filtered = filtered[filtered['Pays'] == country]
        
    if date_range and len(date_range) == 2:
        start_year, end_year = date_range
        filtered = filtered[(filtered['Annee'] >= start_year) & (filtered['Annee'] <= end_year)]
        
    if deps and country == "FRANCE":
        filtered = filtered[filtered['Département'].isin(deps)]
        
    return filtered

def compute_kpis(df):
    # Calculates Key Performance Indicators (KPIs) for the filtered dataset.
    total_accidents = len(df)
    
    if total_accidents == 0:
        return {"total": 0, "top_departement": "N/A", "top_naf": "N/A"}

    if not df['Code NAF'].empty:
        top_naf = df['Code NAF'].value_counts().idxmax()
    else:
        top_naf = "N/A"

    if not df['Département'].empty:
        top_departement = df['Département'].value_counts().idxmax()
    else:
        top_departement = "N/A"

    return {"total": total_accidents, "top_departement": top_departement, "top_naf": top_naf}

def get_data_quality_report(df):
    # Generates completeness and data quality audit report.
    total_rows = len(df)
    if total_rows == 0:
        return {"total_rows": 0, "missing_dates_pct": 0, "missing_deps_pct": 0, "missing_naf_pct": 0, "duplicates": 0}
        
    missing_dates = df['Date_parsed'].isna().sum()
    missing_deps = (df['Département'] == 'UNKNOWN').sum()
    missing_naf = (df['Code NAF'] == 'Not specified').sum()

    if 'Numéro ARIA' in df.columns:
        duplicates = df.duplicated(subset=['Numéro ARIA']).sum()
    else:
        duplicates = 0
    
    return {
        "total_rows": total_rows,
        "missing_dates_pct": round((missing_dates / total_rows) * 100, 2),
        "missing_deps_pct": round((missing_deps / total_rows) * 100, 2),
        "missing_naf_pct": round((missing_naf / total_rows) * 100, 2),
        "duplicates": duplicates
    }