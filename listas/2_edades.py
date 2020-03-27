#2.- Almacenar en una lista las edades de n personas, calcular el promedio
#y mostrar las 3 edades mayores.
personas = int(input("Cantidad de personas: "))
lista = []
sum = 0
for i in range(1, personas+1):
    edad = int(input("Edad de persona {}: ".format(i)))
    lista.append(edad)
print("Lista de edades: ", lista)
for i in range(personas):
    sum = sum + lista[i]
lista.sort(reverse=True)
promedio = sum / personas
print("Edades mayores: {}, {}, {}".format(lista[0], lista[1], lista[2]))
print("El promedio de personas es: ", promedio)
