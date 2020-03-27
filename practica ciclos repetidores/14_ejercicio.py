# 14.- Leer las temperaturas de n regiones y determine:
# el porcentaje de temperaturas por encima de 30º C,
# también el porcentaje de temperaturas por debajo de 0º C

def temperatura(cantidad):
    maximo = 0
    minimo = 0
    fuera = 0
    for region in range(1, cantidad+1):
        temperatura = int(input(f"Digite temperatura de lugar {region}: "))
        if temperatura > 30:
            maximo = maximo + 1
        elif temperatura < 0:
            minimo = minimo + 1
        else:
            fuera = fuera + 1
    total = minimo + maximo + fuera
    print("total: ", total)
    porcentaje_min = (minimo/total) * 100
    porcentaje_max = (maximo/total) * 100
    porcentaje_fuera = (fuera/total) * 100
    print("El porcentaje menor < 0 es: ", porcentaje_min)
    print("El porcentaje mayor > 30 es: ", porcentaje_max)
    print("otros es: ", porcentaje_fuera)




cantidad = int(input("Cantidad de regiones: "))
temperatura(cantidad)
