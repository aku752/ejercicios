#20.- Leer un numero entero y determinar cuántos divisores tiene.

def divisor(numero):
    mitad = numero // 2
    cantidad = 0
    for valor in range(1, numero+1):
        if numero % valor == 0:
            print("Divisor: ", valor)
            cantidad = cantidad + 1
    return cantidad

numero = int(input("Digite un numero entero: "))
respuesta = divisor(numero)
print("Cantidad de divisores", respuesta)
