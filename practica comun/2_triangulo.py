lista = []
for i in range(3):
    promedio = int(input("Introduzca lados: "))
    lista.append(promedio)
if lista[0] == lista[1] == lista[2]:
    print("El triangulo es equilatero")
elif lista[0] != lista[1] != lista[2]:
    print("Es triangulo es escaleno")
else:
    print("Es triangulo isosceles")
