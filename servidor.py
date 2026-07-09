import sqlite3
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

PUERTO = 5800

def validar_usuario(nombre, clave):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
    fila = cursor.fetchone()
    conexion.close()
    if fila is None:
        return False
    hash_ingresado = hashlib.sha256(clave.encode()).hexdigest()
    return hash_ingresado == fila[0]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        formulario = """
        <html><body>
        <h2>Examen DRY7122 - Login</h2>
        <form method="POST">
            Usuario: <input name="usuario"><br>
            Contraseña: <input name="clave" type="password"><br>
            <input type="submit" value="Ingresar">
        </form>
        </body></html>
        """
        self.wfile.write(formulario.encode())

    def do_POST(self):
        largo = int(self.headers['Content-Length'])
        datos = parse_qs(self.rfile.read(largo).decode())
        usuario = datos.get("usuario", [""])[0]
        clave = datos.get("clave", [""])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if validar_usuario(usuario, clave):
            self.wfile.write(f"<h3>Acceso concedido para {usuario}</h3>".encode())
        else:
            self.wfile.write(b"<h3>Usuario o contrasena incorrectos</h3>")

if __name__ == "__main__":
    print(f"Servidor corriendo en http://0.0.0.0:{PUERTO}")
    HTTPServer(("0.0.0.0", PUERTO), Handler).serve_forever()
