centinela = int(input("Cantidad de regiones: "))
lista = []
menor = 0
for i in range(centinela):
    temperatura = int(input("\nDigite temperatura: "))
    lista.append(temperatura)
    if temperatura < 0:
        menor += 1
lista.sort()
print("\nTemperatura maxima: ", lista[centinela-1])
print("Cantidad de temperaturas debajo zero: ", menor)
