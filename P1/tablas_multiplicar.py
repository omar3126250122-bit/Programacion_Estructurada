'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
print("\033c")
tabla=(int)(input("Que tabla deseas imprimir: "))
'''
print(f"{tabla} * 1 = {tabla}")
print(f"{tabla} * 2 = {tabla*2}")
print(f"{tabla} * 3 = {tabla*3}")
print(f"{tabla} * 4 = {tabla*4}")
print(f"{tabla} * 5 = {tabla*5}")
print(f"{tabla} * 6 = {tabla*6}")
print(f"{tabla} * 7 = {tabla*7}")
print(f"{tabla} * 8 = {tabla*8}")
print(f"{tabla} * 9 = {tabla*9}")
print(f"{tabla} * 10 = {tabla*10}")
'''

'''
for i in range(1,11):
  print(f"{tabla} * {i} = {tabla*i}")
'''

'''
cont=1
while cont<=10:
  print(f"{tabla} * {cont} = {tabla*cont}")
  cont+=1
'''
def tablaMultiplicar(tabla):
  msj=(f"{tabla} * 1 = {tabla}\n{tabla} * 2 = {tabla*2}\n{tabla} * 3 = {tabla*3}\n{tabla} * 4 = {tabla*4}\n{tabla} * 5 = {tabla*5}\n{tabla} * 6 = {tabla*6}\n{tabla} * 7 = {tabla*7}\n{tabla} * 8 = {tabla*8}\n{tabla} * 9 = {tabla*9}\n{tabla} * 10 = {tabla*10}")
  return msj
  
mensaje=tablaMultiplicar(tabla)
print(mensaje)


