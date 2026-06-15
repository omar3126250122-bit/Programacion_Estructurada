# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()

nom = "Daniel"
ape = "Carreon"
name,lastname = modulos.funcion4(nom,ape)
print(f"Nombre: {name} \n Apellido: {lastname}")

#2da formar de utilizar modulos
from modulos import borrarPantalla,funcion1,funcion4

borrarPantalla()
funcion1()

nom = "Daniel"
ape = "Carreon"
name,lastname = funcion4(nom,ape)
print(f"Nombre: {name} \n Apellido: {lastname}")

