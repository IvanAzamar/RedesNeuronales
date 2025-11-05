import requests
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency

# Consumir la API
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

# Verificar conexión
if response.status_code == 200:
    data = response.json()
    print("Datos recibidos correctamente.")
else:
    print("Error al conectar con la API:", response.status_code)

# Ver el contenido
print(data.keys())

# Crear DataFrame con tasas
df = pd.DataFrame(list(data["rates"].items()), columns=["currency", "rate"])

# Mostrar primeros datos
print(df.head())
print(df.describe())
