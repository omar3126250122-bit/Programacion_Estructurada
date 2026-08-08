import mysql.connector
import time
from Libros import libros
import pwinput
import getpass
from Prestamos import prestamos
from Usuarios import usuarios
import re

ROJO = "\033[1;31m"
VERDE = "\033[1;32m"
AZUL = "\033[1;34m"
AMARILLO = "\033[1;38;5;130m"
RESET = "\033[0m"
def accionExitosa():
    texto = f"{VERDE}\u2705 Acción exitosa....{RESET}"
    escritura_lenta_print(texto)
    espereTecla()

def accionNoExitosa():
    texto = f"{ROJO}\u274C Acción no exitosa....{RESET}"
    escritura_lenta_print(texto)
    espereTecla()

def espereTecla():
    getpass.getpass(f"{VERDE}\n\t\u2328\uFE0F ...¡Oprima ENTER para continuar!...{RESET}")

def escritura_lenta_print(texto, velocidad=0.01):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="biblioteca"
        ) 
        return conexion
    except:
        texto = f"{ROJO}...¡Por el momento no es posible conectar la aplicacion con la base de datos, intentalo mas tarde!...{RESET}"
        escritura_lenta_print(texto)
        return None

def menuLibros():
    conexionBD = conectar()
    print("\033c")
    texto = f"\t\t{AZUL}....:::: MENU DE LIBROS ::::....\n{VERDE}1.-\u2795 Agregar libros\n2.-\U0001F441\uFE0F\u200D\U0001F5E8\uFE0F Consultar libros\n3.-\U0001F50D Buscar un libro\n4.-\U0001F5D1\uFE0F Borrar libros\n5.-\U0001F9F9 Vaciar los libros\n6.-\u270F\uFE0F Actualizar libros\n7.-\U0001F4CA Reporte de los libros\n8.-\u2B05\uFE0F Atras\n{RESET}"

    escritura_lenta_print(texto)

    texto = f"{AMARILLO}\U0001F449 Ingrese una opcion: \033[s"
    escritura_lenta_print(texto)
    
    opc = ""
    while opc != "8":
        opc = input("\033[u\033[J").strip()
        
        match opc:
            case "1":
                libros.agregarLibros(conexionBD)
            case "2":
                libros.mostrarLibros(conexionBD)
            case "3":
                libros.buscarLibros(conexionBD)
            case "4":
                libros.borrarLibros(conexionBD)
            case "5":
                libros.limpiarLibros(conexionBD)
            case "6":
                libros.modificarLibros(conexionBD)
            case "7":
                libros.generarReporteExcel(conexionBD)
            case "8":
                menuPrincipalRecepcion()
            case _:
                print(f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}")
                espereTecla()

def menu():
    bienvenida()
    ingreso = login()

    while len(ingreso) != 1:
        texto = f"\n{ROJO}Usuario o contraseña incorrecta....{RESET}\033[s"
        escritura_lenta_print(texto)
        espereTecla() 
        print("\033[6A\033[J", end="", flush=True)

        ingreso = login()

    rol = str(ingreso[0][3]).lower().strip()
    matricula=str(ingreso[0][0]).strip()
    if rol == "trabajador":
        menuPrincipalRecepcion()
    else:
        menuPrincipalAlumno(matricula)

def menuPrincipalRecepcion():
    print("\033c")
    texto = f"\t\t{AZUL}....:::: MENU PRINCIPAL RECEPCION ::::....\n{VERDE}1.-\U0001F4DA Gestion de libros\n2.-\U0001F4DD Gestion de prestamos\n3.-\U0001F465 Gestion de usuarios\n4.-\U0001F6AA Cerrar sesion\n{RESET}"
    escritura_lenta_print(texto)
    texto = f"{AMARILLO}\U0001F449 Ingrese una opcion: \033[s"
    escritura_lenta_print(texto)
    opc=""
    while opc!="4":
        opc = input("\033[u").strip()
        match opc:
            case "1":
                menuLibros()
            case "2":
                menuPrestamos()
            case "3":
                menuUsuarios()
            case "4":
                texto = f"{VERDE}\nCerrando sesion con exito...{RESET}"
                escritura_lenta_print(texto)
                espereTecla()
                menu()
            case _:
                print(f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}")
                espereTecla()
                print("\033[u\033[J", end="", flush=True)

def menuPrincipalAlumno(matricula):
    ejecutando = True
    conexionBD = conectar()

    print("\033c", end="", flush=True) 
    
    texto_titulo = f"{AZUL}" + "....:::: MENÚ PRINCIPAL ALUMNOS ::::....".center(80) + f"\n{RESET}"
    escritura_lenta_print(texto_titulo)

    texto_opciones = f"{AMARILLO}1.-\U0001F50D Buscar libros\n2.-\U0001F4C5 Agendar un préstamo\n3.-\U0001F4DA Mis préstamos\n4.-\U0001F464 Mi perfil\n5.-\U0001F6AA Cerrar sesión{RESET}\n"
    escritura_lenta_print(texto_opciones)

    texto_input = f"\n{AMARILLO}\U0001F449 Ingrese una opción: {RESET}\033[s"
    escritura_lenta_print(texto_input)

    while ejecutando:
        opcion = input("\033[u").strip() 
        match opcion:
            case "1":
                libros.buscarLibrosAlumno(matricula, conexionBD)
                menuPrincipalAlumno(matricula)
                return
            case "2":
                prestamos.agregarPrestamosAlumno(matricula, conexionBD)
                menuPrincipalAlumno(matricula)
                return
            case "3":
                prestamos.mostrarPrestamosAlumno(matricula, conexionBD)
                menuPrincipalAlumno(matricula)
                return
            case "4":
                usuarios.modificarUsuariosAlumno(matricula, conexionBD)
                menuPrincipalAlumno(matricula)
                return
            case "5":
                texto_salida = f"\n{VERDE}Cerrando sesión...{RESET}\n"
                escritura_lenta_print(texto_salida)
                espereTecla()
                ejecutando = False
            case _:
                texto_error = f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}"
                print(texto_error, flush=True)
                espereTecla()
                print("\033[u\033[J", end="", flush=True)

    if conexionBD:
        conexionBD.close()
    menu()

def login():
    try:
        conexionBD = conectar()
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            patron_matricula = r'^\d{1,11}$'
            patron_password = r'^\S{4,20}$'

            escritura_lenta_print(f"{AMARILLO}\U0001F194 Matrícula: \033[s")
            matricula = input("\033[u").strip()

            while matricula == "" or not re.match(patron_matricula, matricula):
                if matricula == "":
                    print(f"\n{ROJO}La matrícula no puede estar vacía.{RESET}")
                else:
                    print(f"\n{ROJO}Matrícula inválida.{RESET}")
                    
                espereTecla()
                print("\033[u\033[J", end="", flush=True)
                matricula = input("\033[u").strip()
            escritura_lenta_print(f"{AMARILLO}\U0001F512 Contraseña: \033[s")
            password = pwinput.pwinput("\033[u").strip()

            while password == "" or not re.match(patron_password, password):
                if password == "":
                    print(f"\n{ROJO}La contraseña no puede estar vacía.{RESET}")
                else:
                    print(f"\n{ROJO}Contraseña inválida. Mínimo 4 caracteres (sin espacios).{RESET}")
                    
                espereTecla()
                print("\033[u\033[J", end="", flush=True)
                password = pwinput.pwinput("\033[u").strip()
            cursor.execute("SELECT * FROM usuarios WHERE matricula = %s AND password = %s", (matricula, password))
            return cursor.fetchall()
        else:
            return []
    except:
        print(f"\n{ROJO}Error en la conexión o consulta{RESET}")
        return []

def bienvenida():
    print("\033c")
    texto = f"\t\t{AZUL}\u2728....:::: \U0001F4D6 BIENVENIDO AL SISTEMA DE LA BIBLIOTECA \U0001F4D6 :::....\u2728\n{RESET}"
    escritura_lenta_print(texto)

def menuPrestamos():
    conexionBD = conectar()
    if conexionBD is None:
        espereTecla()
        return

    print("\033c")
    texto = f"\t\t{AZUL}....:::: MENU DE PRESTAMOS ::::....\n{VERDE}1.-\U0001F4DD Registrar préstamo\n2.-\U0001F441\uFE0F\u200D\U0001F5E8\uFE0F Consultar préstamos\n3.-\U0001F50D Buscar un préstamo\n4.-\U0001F5D1\uFE0F Eliminar un préstamo\n5.-\U0001F9F9 Vaciar historial\n6.-\u270F\uFE0F Actualizar préstamo\n7.-\U0001F4CA Reportes de préstamos\n8.-\u2B05\uFE0F Atras\n{RESET}"
    escritura_lenta_print(texto)
    
    texto = f"{AMARILLO}\U0001F449 Ingrese una opcion: \033[s"
    escritura_lenta_print(texto)
    opc=""
    while opc!="8":
        opc = input("\033[u").strip()
        match opc:
            case "1":
                prestamos.agregarPrestamos(conexionBD)
            case "2":
                prestamos.mostrarPrestamos(conexionBD)
            case "3":
                prestamos.buscarPrestamos(conexionBD)
            case "4":
                prestamos.borrarPrestamos(conexionBD)
            case "5":
                prestamos.limpiarPrestamos(conexionBD)
            case "6":
                prestamos.modificarPrestamos(conexionBD)
            case "7":
                prestamos.generarReporteExcel(conexionBD)
            case "8":
                menuPrincipalRecepcion()
            case _:
                print(f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}")
                espereTecla()
                print("\033[u\033[J", end="", flush=True)

def menuUsuarios():
    conexionBD = conectar()
    if conexionBD is None:
        espereTecla()
        return

    print("\033c")
    texto = f"\t\t{AZUL}....:::: MENU DE USUARIOS ::::....\n{VERDE}1.-\U0001F464 Registrar usuario\n2.-\U0001F441\uFE0F\u200D\U0001F5E8\uFE0F Consultar usuario\n3.-\U0001F50D Buscar un usuario\n4.-\U0001F5D1\uFE0F Eliminar un usuario\n5.-\U0001F9F9 Vaciar usuarios\n6.-\u270F\uFE0F Actualizar usuario\n7.-\U0001F4CA Reportes de usuario\n8.-\u2B05\uFE0F Atras\n{RESET}"
    escritura_lenta_print(texto)

    texto = f"{AMARILLO}\U0001F449 Ingrese una opcion: \033[s"
    escritura_lenta_print(texto)
    opc=""
    while opc!="8":
        opc = input("\033[u").strip()
        match opc:
            case "1":
                usuarios.agregarUsuarios(conexionBD)
            case "2":
                usuarios.mostrarUsuarios(conexionBD)
            case "3":
                usuarios.buscarUsuarios(conexionBD)
            case "4":
                usuarios.borrarUsuarios(conexionBD)
            case "5":
                usuarios.limpiarUsuarios(conexionBD)
            case "6":
                usuarios.modificarUsuarios(conexionBD)
            case "7":
                usuarios.generarReporteExcel(conexionBD)
            case "8":
                menuPrincipalRecepcion()
            case _:
                print(f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}")
                espereTecla()
                print("\033[u\033[J", end="", flush=True)