import mysql.connector
from conexion import Error, ConexionBD

class leyes:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='3514996941Mg',
                database='coloquio'
            )
        except Error as ex:
            print("Error al intentar la conexión con la base de datos: {0}".format(ex))


    def registrar_ley(self, datos_ley):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO leyes (nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, datos_ley)
            self.conexion.commit()
            print("¡Ley registrada!\n")
        except Error as ex:
            print("Error al intentar registrar la ley: {0}".format(ex))

    def actualizar_ley(self, id_ley, datos_actualizados):
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE leyes SET nro_leyes=%s, fecha=%s, descripcion=%s, categoria=%s, jurisdiccion=%s, or_legislativo=%s, palabra_clave=%s WHERE nro_leyes=%s"
            cursor.execute(sql, (*datos_actualizados, id_ley))
            self.conexion.commit()
            print("¡Ley actualizada!\n")
        except Error as ex:
            print("Error al intentar actualizar la ley: {0}".format(ex))

    def eliminar_ley_por_numero(self, numero):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM leyes WHERE nro_leyes = %s"
            cursor.execute(sql, (numero,))
            self.conexion.commit()
            print("¡Ley eliminada!\n")
        except Error as ex:
            print("Error al intentar eliminar la ley: {0}".format(ex))

    def listar_todas_las_leyes(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM leyes")
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al intentar listar las leyes: {0}".format(ex))

    def buscar_por_numero(self, numero):
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM leyes WHERE nro_leyes = %s"
                cursor.execute(sql, (numero,))
                resultado = cursor.fetchone()
                return resultado
            except mysql.connector.Error as ex:
                print("Error al buscar la ley por número: {0}".format(ex))