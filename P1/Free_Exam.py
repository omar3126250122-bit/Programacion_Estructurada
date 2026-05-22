def borrarPantalla():
    print("\033c")

def ventaAutos(opc,autos,acum_pv):
    borrarPantalla()

    while opc=="si":
        marca=input("Ingresa la marca del carro: ").lower()
        origen=input("Ingresa el origen del carro: ").lower()
        costo=(float)(input("Ingresa el costo del carro: "))
        impuest=0
        if origen=="alemania":
            impuesto=0.3
        elif origen=="japon":
            impuesto=0.20
        elif origen=="italia":
            impuesto=0.15
        elif origen=="usa":
            impuesto=0.08
        impuesto_pesos=costo*impuesto
        pv=impuesto_pesos+costo
        autos+=1
        acum_pv=pv
        print(f"El impuesto pagar es: ${impuesto_pesos}")
        print(f"El precio de venta es: ${pv}")
        opc=input("¿Deseas agregar otro registro de un carro? (Si/No): ").strip()
    return autos,acum_pv

OPC="si"
AUTOS=0
ACUM_PV=0

autos,acum_pv=ventaAutos(OPC,AUTOS,ACUM_PV)
print(f"Numero de autos ingresados: #{autos} \n y el total de la venta de los carros ${acum_pv}")

