import mysql.connector

class GestorUsuarios:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_usuario(self, usuario, contrasena):
        try:
            cursor = self.conexion.cursor()

            insercion = "INSERT INTO usuarios (nombre, contraseña) VALUES (%s, %s)"
            datos_usuario = (usuario, contrasena)
            print("Intentando insertar datos:", datos_usuario)

            cursor.execute(insercion, datos_usuario)
            self.conexion.commit()

            cursor.close()

            print("¡Usuario registrado exitosamente!")

        except mysql.connector.Error as ex:
            print("Error al intentar registrar usuario:")
            print("Tipo de error:", type(ex))
            print("Mensaje de error completo:", str(ex))

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

#Mensaje de error completo: Unread result found, Me da este error a la hora de registrar usuarios,
#fuera de eso el programa funciona perfectamente, no he podido encontrar solución al mismo
