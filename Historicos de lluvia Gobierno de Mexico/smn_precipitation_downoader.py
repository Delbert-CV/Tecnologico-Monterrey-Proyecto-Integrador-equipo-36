import os
import requests
import time

# Importante:
# - Este script está pensado para crear el folder "descargas_smn" en el mismo directorio donde se corra este script.
# - Esta información se procesa luego con el script smn_precipitation_builder.py, el cual consolida toda la data de precipitacion disponibles en la
#   pagina del SMN (Servicio Meteorológica Nacional)

# Folder sobre el que se descargará la información de precipitación por estado
# Desde la pagina de la SMN
os.makedirs("descargas_smn", exist_ok=True)

# Rango de años y meses que se quieren descargar
years = range(2014, 2026)
months = range(1, 13)


for year in years:
    for month in months:
        
        #  URL para descargar los archivos CSV
        url = f"https://smn.conagua.gob.mx/tools/RESOURCES/com_archivo_datos_resumenes/{year}{month:02d}010000Lluv.csv"
        
        # Nombre del archivo a descargar
        filename = f"descargas_smn/{year}_{month:02d}_000_Lluv.csv"
        
        try:
            r = requests.get(url, timeout=10)
            
            if r.status_code == 200 and len(r.content) > 50:
                with open(filename, "wb") as f:
                    f.write(r.content)
                
                print(f"✅ Se descargó {filename}")
            
            else:
                print(f"⚠️ No se encontró: {url}")
                
                
        except Exception as e:
            print(f"❌ Hubo un error con {url}: {e}")
        
        time.sleep(10)
        