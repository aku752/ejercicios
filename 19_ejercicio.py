#19- Determine la cantidad de dígitos que tiene un número
#    entero positivo utilizando un ciclo.
def cantidad(numero):
    digito = 1
    while True:
        if numero >= 10:
            numero = numero // 10
            digito = digito + 1
        else:
            return digito

numero = int(input("Digite un numero: "))
cantidad = cantidad(numero)
print("Cantidad de digitos: ", cantidad)
