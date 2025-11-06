import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Conexión a la base
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clima"
)

query = "SELECT temperatura, humedad, fecha_hora FROM lecturas"
df = pd.read_sql(query, conexion)
conexion.close()

print(df.head())

# Preparar datos
X = df[['temperatura']]
y = df['humedad']

modelo = LinearRegression()
modelo.fit(X, y)

pendiente = modelo.coef_[0]
intercepto = modelo.intercept_
r2 = modelo.score(X, y)

print(f"\nModelo: humedad = {pendiente:.2f} * temperatura + {intercepto:.2f}")
print(f"Coeficiente R² = {r2:.3f}")

# Graficar
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión lineal')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Humedad (%)')
plt.title('Regresión lineal simple: Temperatura vs Humedad')
plt.legend()
plt.grid(True)
plt.show()
