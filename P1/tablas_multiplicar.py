'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
# print("\033c")

# num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

# num=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

# multi=num_tabla* num
# print(f"{num_tabla} X {num} = {multi} ")
# num+=1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control 
  2.- Sin funciones

'''

# print("\033c")

# num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))


# for num in range(1,11):
#   multi=num_tabla* num
#   print(f"{num_tabla} X {num} = {multi} ")

# num=1
# while num<=10:
#   multi=num_tabla* num
#   print(f"{num_tabla} X {num} = {multi} ")
#   num+=1


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control 
  2.- Con funciones

'''

print("\033c")

def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
  
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

num=1

num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control 
  2.- Con funciones

'''

print("\033c")

def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
  
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

for num in range(1,11):
  num=tabla(num_tabla,num)