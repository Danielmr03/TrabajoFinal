import json
import csv
import os
from datetime import datetime
from utilidades import RUTA_USUARIOS, RUTA_INGRESOS, RUTA_RETIROS

RUTA_ADMIN = os.path.join("src", "datos", "admin.json")

def menu_administrador():
    print("\n--- ACCESO ADMINISTRADOR ---")
    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    if not autenticar(usuario, clave):
        print("❌ Acceso denegado.")
        return

    print("✅ Acceso concedido.")
    mostrar_reportes()

def autenticar(usuario, clave):
    try:
        with open(RUTA_ADMIN, "r") as file:
            data = json.load(file)
            return data.get(usuario) == clave
    except FileNotFoundError:
        return False

def mostrar_reportes():
    print("\n--- REPORTES ADMIN ---")

    usuarios = sum(1 for _ in open(RUTA_USUARIOS)) if os.path.exists(RUTA_USUARIOS) else 0
    ingresados = sum(1 for _ in open(RUTA_INGRESOS)) if os.path.exists(RUTA_INGRESOS) else 0
    retirados = sum(1 for _ in open(RUTA_RETIROS)) if os.path.exists(RUTA_RETIROS) else 0

    pagos = []
    tiempos = []

    try:
        with open(RUTA_RETIROS, mode="r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                pagos.append(int(fila[6]))
                inicio = datetime.strptime(fila[2], "%Y-%m-%d %H:%M:%S")
                fin = datetime.strptime(fila[3], "%Y-%m-%d %H:%M:%S")
                tiempos.append((fin - inicio).total_seconds() / 60)
    except:
        pass

    print(f"🔸 Usuarios registrados: {usuarios}")
    print(f"🔸 Vehículos en parqueadero: {ingresados}")
    print(f"🔸 Vehículos retirados: {retirados}")
    print(f"🔸 Total recaudado: ${sum(pagos):,.0f}")
    if tiempos:
        print(f"🔸 Tiempo promedio de estadía: {sum(tiempos)/len(tiempos):.1f} minutos")
        print(f"🔸 Máximo: {max(tiempos):.1f} min, Mínimo: {min(tiempos):.1f} min")
