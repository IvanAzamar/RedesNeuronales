import serial
import mysql.connector

# Conexión con Arduino (ajusta el puerto según tu PC)
arduino = serial.Serial('COM3', 9600)  # Linux sería '/dev/ttyUSB0'

# Conexión con MariaDB
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clima"
)
cursor = conexion.cursor()

print("Recolectando datos del Arduino y guardando en MariaDB...")

try:
    while True:
        linea = arduino.readline().decode().strip()
        if linea:
            try:
                t, h = map(float, linea.split(","))
                cursor.execute(
                    "INSERT INTO lecturas (temperatura, humedad) VALUES (%s, %s)", (t, h)
                )
                conexion.commit()
                print(f"Guardado: Temp={t}°C, Hum={h}%")
            except ValueError:
                print("Dato inválido:", linea)
except KeyboardInterrupt:
    print("Detenido manualmente.")
finally:
    arduino.close()
    cursor.close()
    conexion.close()
