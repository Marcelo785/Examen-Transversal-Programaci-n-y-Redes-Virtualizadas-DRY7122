import sqlite3
import hashlib

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
""")

integrantes = {
    "Perez Diego": "12345678",
    "Navarro Marcelo": "87654321",
}

for nombre, clave in integrantes.items():
    hash_clave = hashlib.sha256(clave.encode()).hexdigest()
    cursor.execute(
        "INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)",
        (nombre, hash_clave)
    )

conexion.commit()
conexion.close()
print("Base de datos creada con usuarios y contraseñas en hash.")
