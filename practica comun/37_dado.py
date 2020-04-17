from random import *
lanzar = int(input("Cantidad lanzamientos: "))
par = impar = 0
print("\nResultados de lanzamientos: ")
for i in range(lanzar):
    numero = randint(1, 6)
    print(numero, end=' ')
    par_impar = numero%2
    if par_impar:
        impar +=1
    else:
        par +=1
print("\n\nCantidad de pares: ", par)
print("Cantidad de impares: ", impar)
