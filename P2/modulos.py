# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
   nombre=input("Nombre: ").strip().upper()
   apellidos=input("Apellidos: ").strip().upper()
   print(f"El nombre del alumno es: {nombre} {apellidos}")

#3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):

   nombre=nom
   apellidos=ape
   print(f"El nombre del alumno es: {nombre} {apellidos}")

#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   nombre=input("Nombre: ").strip().upper()
   apellidos=input("Apellidos: ").strip().upper()
   return nombre,apellidos

#4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
   nombre=nom
   apellidos=ape
   return nombre,apellidos


