import csv
import os
from datetime import datetime
from utilidades import calcular_tiempo_y_costo, buscar_usuario, obtener_celda_disponible, liberar_celda, RUTA_INGRESOS, RUTA_RETIROS, MAX_CELDAS

def menu_vehiculos(accion):
    if accion == "ingreso":
        ingreso_vehiculo()
    elif accion == "retiro":
        retiro_vehiculo()

def ingreso_vehiculo():
    print("\n--- INGRESO DE VEHÍCULO ---")
    documento = input("Ingrese el documento del usuario: ").strip()

    if not buscar_usuario(documento):
        print("❌ El usuario no está registrado.")
        return

    celda = obtener_celda_disponible()
    if celda is None:
        print("❌ No hay espacios disponibles.")
        return

    hora_ingreso = datetime.now()
    datos = [documento, celda, hora_ingreso.strftime("%Y-%m-%d %H:%M:%S")]
    
    with open(RUTA_INGRESOS, mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)

    print(f"✅ Vehículo ingresado en la celda {celda} a las {hora_ingreso.strftime('%H:%M')}.")

def retiro_vehiculo():
    print("\n--- RETIRO DE VEHÍCULO ---")
    documento = input("Ingrese el documento del usuario: ").strip()

    
    registros = []
    encontrado = None

    with open(RUTA_INGRESOS, mode="r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == documento:
                encontrado = fila
            else:
                registros.append(fila)

    if not encontrado:
        print("❌ No se encontró un vehículo registrado con ese documento.")
        return

    
    celda = encontrado[1]
    hora_ingreso = datetime.strptime(encontrado[2], "%Y-%m-%d %H:%M:%S")
    hora_salida = datetime.now()

    horas, cuartos, total = calcular_tiempo_y_costo(hora_ingreso, hora_salida)

    
    with open(RUTA_RETIROS, mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([documento, celda, hora_ingreso.strftime("%Y-%m-%d %H:%M:%S"),
                           hora_salida.strftime("%Y-%m-%d %H:%M:%S"), horas, cuartos, total])

    
    with open(RUTA_INGRESOS, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(registros)

    liberar_celda(celda)
    print(f"✅ Vehículo retirado. Total a pagar: ${total:,.0f} COP")
