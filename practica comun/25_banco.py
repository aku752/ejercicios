tarjeta = int(input("Cantidad de tarjetas: "))
tipo = int(input("Determine el tipo: "))

if tarjeta >= 2:
    print("------------------------------")
    print("El cliente cuenta con mas de 2 tarjetas")
    print("Se aplicara el mayor tipo, o la que el cliente quiera")
    elegir = str(input("Desea elegir otro tipo?? S/N: "))
    elegir.lower()
    if elegir == "s":
        print("------------------------------")
        tipo = int(input("Determine el nuevo tipo: "))
        if tipo == 1:
            aumento = 25
        elif tipo == 2:
            aumento = 35
        elif tipo == 3:
            aumento = 40
        else:
            aumento = 50
    elif elegir == "n":
        aumento = 50
    else:
        print("------------------------------")
        print("No escogio ninguna opcion se aplicara el mayor tipo")

else:
    if tipo == 1:
        aumento = 25
    elif tipo == 2:
        aumento = 35
    elif tipo == 3:
        aumento = 40
    else:
        aumento = 50
print("------------------------------")
print("Cantidad de tarjetas: ", tarjeta)
print("Nuevo limite de credito es de: ", aumento, "%")
