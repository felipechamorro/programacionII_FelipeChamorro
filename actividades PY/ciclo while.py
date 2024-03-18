def mostrar_menu():
    print("Menú de opciones:")
    print("1. Personas")
    print("2. Vehículos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresa un número válido.")

def main():
    while True:
        mostrar_menu()
        opcion_seleccionada = seleccionar_opcion()

        if opcion_seleccionada == 1:
            print("Has presionado la opción Personas.")
        elif opcion_seleccionada == 2:
            print("Has presionado la opción Vehículos.")
        elif opcion_seleccionada == 3:
            print("Has presionado la opción Universidades.")
        elif opcion_seleccionada == 4:
            print("Has presionado la opción Notas.")
        elif opcion_seleccionada == 5:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
