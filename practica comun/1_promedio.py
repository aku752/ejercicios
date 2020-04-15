lista = []
sum = 0
for i in range(4):
    practica = int(input("Introduzca nota: "))
    lista.append(practica)
lista.sort()
print("Se elimina la nota de: {}".format(lista[0]))
for i in range(1, 4):
    sum = sum + lista[i]
promedio = sum/3
print("El promedio es: {0:.1f} ".format(promedio))
