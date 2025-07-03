import os
import csv
from datetime import datetime


RUTA_USUARIOS = os.path.join("src", "datos", "usuarios.csv")
RUTA_INGRESOS = os.path.join("src", "datos", "ingresos.csv")
RUTA_RETIROS = os.path.join("src", "datos", "retiros.csv")
MAX_CELDAS = 50


def buscar_usuario(documento):
    try:
        with open(RUTA_USUARIOS, mode="r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila[0] == documento:
                    return True
    except FileNotFoundError:
        pass
    return False


def obtener_celda_disponible():
    ocupadas = set()
    try:
        with open(RUTA_INGRESOS, mode="r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                ocupadas.add(int(fila[1]))
    except FileNotFoundError:
        pass

    for celda in range(1, MAX_CELDAS + 1):
        if celda not in ocupadas:
            return celda
    return None


def liberar_celda(celda):
    pass  


def calcular_tiempo_y_costo(inicio, fin):
    total_min = int((fin - inicio).total_seconds() // 60)
    horas = total_min // 60
    cuartos = (total_min % 60) // 15
    total = (horas * 7000) + (cuartos * 1500)
    if total < 7000:
        total = 7000
    return horas, cuartos, total


def exportar_datos():
    print("📁 Datos exportados automáticamente.")
