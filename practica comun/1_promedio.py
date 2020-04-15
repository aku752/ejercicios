lista = []
menor = 0
sum = 0
for i in range(4):
    practica = int(input("Introduzca nota: "))
    lista.append(practica)
lista.sort()
for i in range(1, 4):
    print(i)
    sum = sum + lista[i]
promedio = sum/3
print("El promedio es: {0:.1f} ".format(promedio))
