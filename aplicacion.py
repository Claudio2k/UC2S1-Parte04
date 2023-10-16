# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:30:06 2023

@author: user
"""

import os

def validar_datos(login, clave):
    # Ruta de los archivos de login y clave
    login_file_path = os.path.join(os.path.dirname(__file__), 'login.txt')
    clave_file_path = os.path.join(os.path.dirname(__file__), 'clave.txt')

    # Verificar si login y clave coinciden
    with open(login_file_path, 'r') as login_file, open(clave_file_path, 'r') as clave_file:
        logins = login_file.read().splitlines()
        claves = clave_file.read().splitlines()

    return (login in logins) and (clave in claves)

intentos_maximos = 2
intentos = 0

while intentos < intentos_maximos:
    login_input = input("Ingrese su login: ")
    clave_input = input("Ingrese su clave: ")

    if validar_datos(login_input, clave_input):
        print("Datos correctos. Acceso permitido.")
       
        # (Para este ejemplo, solo mostramos un mensaje)
        print("Menú de opciones:")
        print("Datos Persona")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir")
        break
    else:
        print("Datos incorrectos. Por favor, intente nuevamente.")
        intentos += 1

if intentos == intentos_maximos:
    print("Has excedido el número de intentos permitidos. Programa terminado.")
