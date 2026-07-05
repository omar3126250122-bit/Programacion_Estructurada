import funciones
      
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    pelis.append(peli)
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    print("\tCodigo\t\tPelicula\n")
    for i in range(0,len(pelis)):
        print(f"{i+1}\t\t{pelis[i]}")
    funciones.espereTecla()
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        pelis=pelis.clear()
        funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        print("\tCodigo\t\tPelicula\n")
        for i in range(0,len(pelis)):
          if peli==pelis[i]:
             print(f"{i+1}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("...¡No exite la pelicula que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    posiciones=[]
    print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
                opc=""
                while opc!="si" and opc!="no":
                  opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                  posiciones.append(i)
        if len(posiciones)>0:
            for i in range(0,len(posiciones)):
                pelis.remove(peli)
            funciones.accionExitosa()
    else:
        input("...¡No exite la pelicula que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    posiciones=[]
    print("\n\t\t...:::: MODIFICAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
                opc=""
                while opc!="si" and opc!="no":
                  opc=input("¿Deseas modificar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                  pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                  funciones.accionExitosa()
    else:
        input("...¡No exite la pelicula que estas buscando, verifique!...")