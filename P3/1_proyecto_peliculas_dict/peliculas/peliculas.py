import funciones

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introducir el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):  
    print("\n\t\t...:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    print("\tCaracteristica\t\tValor\n")
    if len(pelis)>0:
        for i in range(0,len(pelis)):
            print(f"{i+1}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        print("\n\t...¡No hay caracteristicas a mostrar de la pelicula!...")    

def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS la caracteristicas(Si/No)? ").lower().strip()
        if opc=="si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro=False
    for i in pelis:   
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i+1}\t\t{pelis[i]}")
            noencontro=True
        funciones.espereTecla() 
        if not(noencontro):
            input("...¡No exite la pelicula que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.pop(caracteristica)
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el valor: ").upper().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas modificar el valor de la caracteristica de la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[caracteristica ]=input("Escribe el nuevo valor de la caracteristica: ").upper().strip()
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")