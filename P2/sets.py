"""
Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

set1 = {"Hola","123","123","Mexico","Holanda",123,3.1416}
print(set1)

set1.add("Ganador")
print(set1)

set1.pop()
print(set1)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
emails = []
resp="si"

while resp=="si":
	emails.append(input("Ingresa el email del alumno: "))
	resp=input("¿Quieres ingresar otro email? (Si/No)").lower().strip()

set_email={}
set_email=set(emails)
print(set_email)

#Solucion 2
emails = set()
resp = "si"

while resp == "si":
    email = input("Ingresa el email del alumno: ").strip().lower()
    emails.add(email)
    
    resp = input("¿Quieres ingresar otro email? (Si/No): ").lower().strip()

print("Emails sin duplicados:")
for email in emails:
    print(email)

