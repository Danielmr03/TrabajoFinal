from usuario import menu_usuarios
from vehiculo import menu_vehiculos
from administrador import menu_administrador
from utilidades import exportar_datos

def menu_principal():
    def print_logo():
        print("""
┌──────────────────────────────┐
│   ████  █   █  ██  ████  █   │
│   █     ██ ██ █  █ █   █ █   │
│   ████  █ █ █ ████ ████  █   │
│      █  █   █ █  █ █     █   │
│   ████  █   █ █  █ █     █   │
│                              │
│ SMART PARKING - Universidad  │
│        de Antioquia          │
└──────────────────────────────┘
""")

    while True:
        print("\n")
        print_logo()
        print("┌──────────────────────────────┐")
        print("│         MENÚ PRINCIPAL       │")
        print("├──────────────────────────────┤")
        print("│ 1. Registrar usuario         │")
        print("│ 2. Ingresar vehículo         │")
        print("│ 3. Retirar vehículo          │")
        print("│ 4. Modo administrador        │")
        print("│ 5. Salir                     │")
        print("└──────────────────────────────┘")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_vehiculos("ingreso")
        elif opcion == "3":
            menu_vehiculos("retiro")
        elif opcion == "4":
            menu_administrador()
        elif opcion == "5":
            print("\n┌──────────────────────────────┐")
            print("│      >> EXPORTAR DATOS <<    │")
            print("└──────────────────────────────┘")
            confirmar = input("¿Generar reporte CSV? (S/N): ").lower()
            if confirmar == "s":
                exportar_datos()
                print("✓ Archivo 'reporte_smartparking_DD-MM-YYYY.csv' creado |\n¡Hasta pronto!")
            else:
                print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()
