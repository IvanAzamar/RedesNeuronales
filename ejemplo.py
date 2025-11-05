import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer datos directamente con pandas
url = "https://jsonplaceholder.typicode.com/users"
df = pd.read_json(url)

# 2. Extraer solo columnas relevantes
df["ciudad"] = df["address"].apply(lambda x: x["city"])
df["longitud_nombre"] = df["name"].apply(len)

# 3. Gráfica: longitud de los nombres
plt.figure(figsize=(10,6))
plt.bar(df["name"], df["longitud_nombre"], color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.title("Longitud de nombres de usuarios")
plt.xlabel("Nombre")
plt.ylabel("Número de caracteres")
plt.tight_layout()
plt.show()

# 4. Gráfica: número de usuarios por ciudad
ciudad_counts = df["ciudad"].value_counts()

plt.figure(figsize=(8,5))
ciudad_counts.plot(kind="bar", color="lightgreen")
plt.xticks(rotation=45, ha="right")
plt.title("Número de usuarios por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Cantidad de usuarios")
plt.tight_layout()
plt.show()
