import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='3514996941Mg',
                database='coloquio'
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as ex:
            print("Error al intentar conexión con la base de datos: {0}".format(ex))

    def cerrar_bd(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada correctamente.")
