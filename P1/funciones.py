
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
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

#Invocar las funciones
funcion1()

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
funcion3(nombre,apellidos)

nombre,apellidos=funcion2()
print(f"El nombre del alumno es: {nombre} {apellidos}")

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
nombre,apellidos=funcion4(nombre,apellidos)
print(f"El nombre del alumno es: {nombre} {apellidos}")
