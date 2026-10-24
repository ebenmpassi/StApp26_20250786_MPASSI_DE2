import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data():
    # Loads and preprocesses the ARIA dataset with Streamlit caching.
    df = pd.read_csv("data/ARIA.csv")
    
    # Date parsing
    df['Date_parsed'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Annee'] = df['Date_parsed'].dt.year
    
    # Country cleaning
    df['Pays'] = df['Pays'].fillna('NOT SPECIFIED').str.upper().str.strip()
    
    # Department formatting
    df['Département'] =df['Département'].fillna('UNKNOWN').astype(str).str.split('.').str[0].str.zfill(2)
    
    # Text strings cleaning
    df['Code NAF'] = df['Code NAF'].fillna('Not specified').str.strip()
    df['Type d\'accident'] = df['Type d\'accident'].fillna('Not specified').str.strip()
    
    return df