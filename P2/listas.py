print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros = [23,33,45,8,24,0,100]
print(numeros)

lista =""
for i in numeros:
   lista =lista + str(i) + ", "
   lista+=f"{i}, "
print("["+lista+"]")


lista =""
for i in range(0,len(numeros)):
   lista =lista + str(numeros[i]) + ", "
   lista+=f"{numeros[i]}, "

print("["+lista+"]")

lista =""
cont=0
while cont<len(numeros):
   lista =lista + str(numeros[cont]) + ", "
   cont+=1    
print("["+lista+"]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1er Forma
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip()

if palabra in palabras:
   print(f"Encontre la palabras: {palabra} en la lista")
else:
   print(f"No encontre la palabra {palabra} en la lista")

#2DA FORMA
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip()
fl=False
for i in palabras:
    if i == palabra:
        fl=True
    
if fl:
    print(f"Encontre la palabras: {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


    
#3er FORMA
cont = 0
mensaje2 = (f"No se encontro {palabra}")
while cont != len(palabras):
    if palabra == palabras[cont]:
        mensaje2 = (f"Encontre la palabra {palabra}")
    cont+=1
print(mensaje2)
#Ejemplo 3 Añadir elementos a la lista
lista = []

#opc 1:
true=True
while true:
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    true=input("Ingresa True/False para continuar: ").strip()
    if true=="False":
        true=False

#opc 2:
true="true"
while true=="true":
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    true=input("Ingresa Si/No para continuar: ").strip().lower()

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda =[
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]
print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
elemento=""
for r in range(0,3): 
    for c in range(0,2):
            elemento+=f"{agenda[r][c]}, "
    elemento+="\n"
print(elemento)