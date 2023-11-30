import mysql.connector
from conexion import Error, ConexionBD

class GestorLogin:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='3514996941Mg',
                database='coloquio'
            )
        except mysql.connector.Error as ex:
            print("Error al intentar la conexión con la base de datos: {0}".format(ex))

    def iniciar_sesion(self, usuario, contrasena):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s"
            cursor.execute(consulta, (usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado:
                print("¡Inicio de sesión exitoso!")
                return True
            else:
                print("Datos incorrectos. Inicio de sesión fallido.")
                return False

        except mysql.connector.Error as ex:
            print("Error al intentar iniciar sesión: {0}".format(ex))
