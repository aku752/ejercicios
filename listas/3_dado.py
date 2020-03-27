#3.- Almacenar en una lista el lanzamiento de un dado 10 veces,
# determine qué cara salió más veces y que cara salió menos veces
from random import *
dado = []
caras = []
menores = []
mayores = []
for i in range(10):
    suerte = randint(1,6)
    dado.append(suerte)
print("Lanzamiento de dado: ",dado)
for i in range(6):
    cantidad = dado.count(i+1)
    caras.append(cantidad)
print("\nDado caras [1, 2, 3, 4, 5, 6]\nCantidad  ", caras)
num_max = max(caras)
inicial = num_max
for valor in caras:
    if valor != 0:
        if valor <= inicial:
            menor = valor
            inicial = valor
for i in range(6):
    if num_max == caras[i]:
        mayores.append(i+1)
    elif menor == caras[i]:
        menores.append(i+1)
print("\nSalio mas veces, una cantidad de: ", num_max)
print("Las caras del dado fueron el: ", mayores)
print("\nSalio menos veces, una cantidad de: ", menor)
print("Las caras del dado fueron el: ", menores)
