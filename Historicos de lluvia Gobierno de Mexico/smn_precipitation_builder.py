import pandas as pd
import numpy as np
import unicodedata
import time
import os
import re

#  IMPORTANTE:
#       - Este Script debe usarse después de descargar la data por medio del script smn_precipitation_downloader.py 
#       - Abril de 2023 tiene las columnas en desorden, por lo que corregimos las mismas manualmente, y es  necesario tomar esto en cuenta si se quiere correr este script.

def remove_accents(text):
    if pd.isna(text):
        return text
    
    return ''.join(
        c for c in unicodedata.normalize('NFKD', str(text))
        if not unicodedata.combining(c)
    )

def clean_text(text):
    if pd.isna(text):
        return text
    text = remove_accents(text)
    return re.sub(r'[^A-Za-z0-9\s]', '', text).upper()



current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir    = os.path.join(current_dir, "descargas_smn")

years  =  range(2014,2026)
months = range(1,13)

all_df = []

for year in years:
    for month in months:
        path_to_load = os.path.join(data_dir, f"{year}_{month:02d}_000_Lluv.csv")
        
        
        if os.path.exists(path_to_load):
            df = pd.read_csv(path_to_load, encoding='latin1', usecols=range(6), engine='python')
            df.columns = ['lon', 'lat', 'state', 'cve_sih', 'name', 'precipitation(mm)'] 
            df['year-month'] = f"{year}-{month:02d}" 
            all_df.append(df)
            
df_final  = pd.concat(all_df, ignore_index=True)

string_cols = ['state', 'cve_sih', 'name']

for col in string_cols:
    df_final[col] = df_final[col].apply(remove_accents)
    
for col in string_cols:
    df_final[col] = df_final[col].apply(clean_text)

df_final.to_csv('precipitation_per_area_historical.csv', index=False)
        