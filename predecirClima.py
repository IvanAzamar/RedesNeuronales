import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1️⃣ Consumir una API del clima (Open-Meteo)
url = "https://api.open-meteo.com/v1/forecast?latitude=66.9394735&longitude=-53.7044768&hourly=temperature_2m"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ API conectada correctamente")
else:
    print("❌ Error al conectar con la API")
    exit()

# 2️⃣ Crear un DataFrame con pandas
horas = data["hourly"]["time"]
temperaturas = data["hourly"]["temperature_2m"]

df = pd.DataFrame({
    "hora": pd.to_datetime(horas),
    "temperatura": temperaturas
})

# Extraer solo la hora (0–23) para entrenar el modelo
df["hora_num"] = df["hora"].dt.hour

print(df.head())

# 3️⃣ Dividir datos para entrenamiento y prueba
X = df[["hora_num"]]  # variable independiente
y = df["temperatura"] # variable dependiente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Entrenar modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5️⃣ Realizar predicciones
y_pred = modelo.predict(X_test)

# 6️⃣ Evaluar el modelo
error = mean_squared_error(y_test, y_pred)
print(f"📉 Error cuadrático medio: {error:.2f}")

# 7️⃣ Graficar resultados
plt.figure(figsize=(10,6))

# Ordenar los valores para una gráfica continua
df_sorted = df.sort_values(by="hora_num")

# Predicción continua para todas las horas
y_line = modelo.predict(df_sorted[["hora_num"]])

# Temperatura real (línea azul)
plt.plot(df_sorted["hora_num"], df_sorted["temperatura"], color='blue', marker='o', label='Temperatura real')

# Predicción del modelo (línea roja)
plt.plot(df_sorted["hora_num"], y_line, color='red', linestyle='--', label='Predicción')

plt.title("Predicción de temperatura por hora (SISMIUT GROENLANDIA)")
plt.xlabel("Hora del día")
plt.ylabel("Temperatura °C")
plt.legend()
plt.grid(True)

# 👇 Forzar que se muestre la gráfica en todos los entornos
plt.show(block=True)
