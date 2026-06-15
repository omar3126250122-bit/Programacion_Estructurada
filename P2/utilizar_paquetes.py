from paquete1 import modulos,modulo_paquete

modulos.borrarPantalla()

nom="Daniel"
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
msj=modulo_paquete.funcion4(nom,ape)

print(f"Nombre: {name}\nApellido: {lastname}\nEdad: {modulo_paquete.edad}")

print(msj)
