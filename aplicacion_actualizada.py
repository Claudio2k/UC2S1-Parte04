# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:18 2023

@author: Claudio
"""
import os

def cargar_personas():
    # Ruta de los archivos de DNI, nombres y apellidos
    dni_file_path = os.path.join(os.path.dirname(__file__), 'dni.txt')
    nombre_file_path = os.path.join(os.path.dirname(__file__), 'nombre.txt')
    apellido_file_path = os.path.join(os.path.dirname(__file__), 'apellido.txt')

    personas = []

    with open(dni_file_path, 'r') as dni_file, \
            open(nombre_file_path, 'r') as nombre_file, \
            open(apellido_file_path, 'r') as apellido_file:
        dniss = dni_file.read().splitlines()
        nombres = nombre_file.read().splitlines()
        apellidos = apellido_file.read().splitlines()

    for dni, nombre, apellido in zip(dniss, nombres, apellidos):
        personas.append({'dni': dni, 'nombre': nombre, 'apellido': apellido})

    return personas

def listar_personas():
    personas = cargar_personas()
    
    print("Listado de personas:")
    for persona in personas:
        print(f"DNI: {persona['dni']}, Nombre: {persona['nombre']}, Apellido: {persona['apellido']}")

def agregar_persona(dni, nombre, apellido):
    # Ruta de los archivos de DNI, nombres y apellidos
    dni_file_path = os.path.join(os.path.dirname(__file__), 'dni.txt')
    nombre_file_path = os.path.join(os.path.dirname(__file__), 'nombre.txt')
    apellido_file_path = os.path.join(os.path.dirname(__file__), 'apellido.txt')

    # Agregar la nueva persona a los archivos
    with open(dni_file_path, 'a') as dni_file, \
            open(nombre_file_path, 'a') as nombre_file, \
            open(apellido_file_path, 'a') as apellido_file:
        dni_file.write(dni + '\n')
        nombre_file.write(nombre + '\n')
        apellido_file.write(apellido + '\n')

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
       
        print("Menú de opciones:")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir")

        while True:
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                listar_personas()
            elif opcion == '2':
                dni = input("Ingrese el DNI: ")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                agregar_persona(dni, nombre, apellido)
                print("Persona agregada con éxito.")
            elif opcion == '3':
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

        break
    else:
        print("Datos incorrectos. Por favor, intente nuevamente.")
        intentos += 1

if intentos == intentos_maximos:
    print("Has excedido el número de intentos permitidos. Programa terminado.")
