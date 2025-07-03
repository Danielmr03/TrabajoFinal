import csv
import re
import os

RUTA_USUARIOS = os.path.join("src", "datos", "usuarios.csv")

def validar_nombre(nombre):
    return nombre.isalpha() and len(nombre) >= 3

def validar_documento(documento):
    return documento.isdigit() and 3 <= len(documento) <= 15

def validar_placa(placa):
    return bool(re.match(r"^[A-Z]{3}[0-9]{3}$", placa.upper()))

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")

    nombre = input("Ingrese el nombre: ").strip()
    apellido = input("Ingrese el apellido: ").strip()
    documento = input("Ingrese el número de documento: ").strip()
    placa = input("Ingrese la placa del vehículo (ej. ABC123): ").strip().upper()

    errores = []

    if not validar_nombre(nombre):
        errores.append("❌ El nombre debe tener al menos 3 letras y no contener números.")

    if not validar_nombre(apellido):
        errores.append("❌ El apellido debe tener al menos 3 letras y no contener números.")

    if not validar_documento(documento):
        errores.append("❌ El documento debe contener entre 3 y 15 dígitos numéricos.")

    if not validar_placa(placa):
        errores.append("❌ La placa debe tener el formato correcto: 3 letras seguidas de 3 números.")

    if errores:
        print("\n".join(errores))
        return

    
    with open(RUTA_USUARIOS, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([documento, nombre, apellido, placa])
        print(f"✅ Usuario registrado exitosamente.")

def menu_usuarios():
    registrar_usuario()
