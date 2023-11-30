from funciones import leyes as GestorLeyes

def menu():
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
            print("========================================================")
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion < 1 or opcion > 5:
                    print("Opción incorrecta, ingrese nuevamente")
                else:
                    opcionCorrecta = True
                    continuar = ejecutarOpcion(opcion)
            except ValueError:
                print("Opción no válida, ingrese un número válido.")

def ejecutarOpcion(opcion):
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
            return False

        else:
            print("Opción no válida. Intente nuevamente.")

        return True

menu()