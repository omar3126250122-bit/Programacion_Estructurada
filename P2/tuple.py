"""   
  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.
"""
print("\033c")

paises1 = ("México","Canada","EUA")

print(paises1)

varios =("Hola",True,33,3.1416)


print(paises1)
print(varios)

for i in paises1:
    print(i)

for i in range(0,len(paises1)):
    print(paises1[i])

i=0
while i<len(paises1):
    print(paises1[i])
    i+=1


print(f"El pais que inagura la copa del mundo 2026 es: {paises1[0]}")

edades = (23,24,18,20,20,23,24,19,24)

cuantos = edades.count(24)
print(cuantos)

#Crear un programa que me lea un numero y me diga en que posiciones se encuetra 
edades = (23,24,18,20,20,23,24,19,24)
print(edades)
numero =(int)(input("Dame el numero a buscar: "))
posicion = edades.index(numero)
print(f"El numero {numero} se encontro en la posicion: {posicion}")

#Utilizando listas
numero =(int)(input("Dame el numero a buscar: "))
posiciones=[]
for i in range(0,len(edades)):
  if (numero==edades[i]):  
    posiciones.append(i)

posiciones = tuple(posiciones)

for i in posiciones:
  print(f"El numero {numero} se encontro en la posicion: {i}")


#Utilizando Set
numero =(int)(input("Dame el numero a buscar: "))
posiciones={""}
posiciones.clear()
for i in range(0,len(edades)):
  if (numero==edades[i]):  
    posiciones.add(i)

posiciones = tuple(posiciones)

for i in posiciones:
  print(f"El numero {numero} se encontro en la posicion: {i}")




