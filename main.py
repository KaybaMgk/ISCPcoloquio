from login import GestorLogin, GestorUsuarios
from funciones import leyes as GestorLeyes

def ejecutar_programa():
    gestor_login = GestorLogin()
    gestor_usuarios = GestorUsuarios(gestor_login.conexion)
    intentos = 0
    max_intentos = 3
    salir_programa = False

    while intentos < max_intentos and not salir_programa:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if gestor_login.iniciar_sesion(usuario, contrasena):
            continuar = True
            while continuar:
                opcionCorrecta = False
                while not opcionCorrecta:
                    print("==================== MENÚ PRINCIPAL ====================")
                    print("1.- Listar leyes")
                    print("2.- Registrar ley")
                    print("3.- Actualizar ley")
                    print("4.- Eliminar ley")
                    print("5.- Salir")
                    print("6.- Registrar usuario")
                    print("========================================================")
                    try:
                        opcion = int(input("Seleccione una opción: "))
                        if opcion < 1 or opcion > 6:
                            print("Opción incorrecta, ingrese nuevamente")
                        else:
                            opcionCorrecta = True
                            continuar, salir_programa = ejecutarOpcion(opcion, gestor_login, gestor_usuarios, salir_programa)
                    except ValueError:
                        print("Opción no válida, ingrese un número válido.")

                    if opcion == 5:
                        continuar = False
                        salir_programa = True
        else:
            intentos += 1
            if intentos < max_intentos:
                print(f"Intento fallido. Le quedan {max_intentos - intentos} intentos.")
            else:
                print("Ha excedido el número de intentos. Cerrando programa.")
                return

def ejecutarOpcion(opcion, gestor_login, gestor_usuarios, salir_programa):
    gestor_leyes = GestorLeyes()

    if opcion == 1:
        leyes = gestor_leyes.listar_todas_las_leyes()
        if leyes:
            for ley in leyes:
                print(ley)
        else:
            print("No se encontraron leyes.")

    elif opcion == 2:
        nro_leyes = input("Ingrese el número de la ley: ")
        fecha = input("Ingrese la fecha de la ley (YYYY-MM-DD): ")
        descripcion = input("Ingrese la descripción de la ley: ")
        categoria = input("Ingrese la categoría de la ley: ")
        jurisdiccion = input("Ingrese la jurisdicción de la ley: ")
        or_legislativo = input("Ingrese el órgano legislativo de la ley: ")
        palabra_clave = input("Ingrese la palabra clave de la ley: ")

        datos_nueva_ley = (nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave)
        gestor_leyes.registrar_ley(datos_nueva_ley)

    elif opcion == 3:
        numero_a_actualizar = input("Ingrese el número de la ley a actualizar: ")
        ley_a_actualizar = gestor_leyes.buscar_por_numero(numero_a_actualizar)
        if ley_a_actualizar:
            fecha = input("Ingrese la nueva fecha de la ley (YYYY-MM-DD): ")
            descripcion = input("Ingrese la nueva descripción de la ley: ")
            categoria = input("Ingrese la nueva categoría de la ley: ")
            jurisdiccion = input("Ingrese la nueva jurisdicción de la ley: ")
            or_legislativo = input("Ingrese el nuevo órgano legislativo de la ley: ")
            palabra_clave = input("Ingrese la nueva palabra clave de la ley: ")

            datos_actualizados = (numero_a_actualizar, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave)
            gestor_leyes.actualizar_ley(numero_a_actualizar, datos_actualizados)
        else:
            print("La ley no existe.")

    elif opcion == 4:
        numero_a_eliminar = input("Ingrese el número de la ley a eliminar: ")
        gestor_leyes.eliminar_ley_por_numero(numero_a_eliminar)

    elif opcion == 5:
        print("¡Gracias por usar este sistema!")
        salir_programa = True

    elif opcion == 6:
        nuevo_usuario = input("Ingrese el nombre de usuario: ").strip()
        nueva_contrasena = input("Ingrese la contraseña: ").strip()

        if nuevo_usuario and nueva_contrasena:
            gestor_usuarios.registrar_usuario(nuevo_usuario, nueva_contrasena)
            print("Usuario registrado exitosamente.")
            return True, salir_programa
        else:
            print("Nombre de usuario y contraseña no pueden estar vacíos. Intente nuevamente.")

    else:
        print("Opción no válida. Intente nuevamente.")

    return True, salir_programa

if __name__ == "__main__":
    ejecutar_programa()
