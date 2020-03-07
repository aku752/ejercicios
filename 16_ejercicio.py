# 16.-  Leer un numero entero y muestre
# la suma de sus dos primeros dígitos.
def suma_digito(numero, total):
    digito = 1
    sumar = 0
    while True:
        numero = numero // 10
        digito = digito + 1
        if digito >= (total-1):
            modulo = numero % 10
            sumar = sumar + modulo
            if digito == total:
                print("La suma de los dos digitos es: ", sumar)
                break

def cantidad(numero):
    digito = 1
    while True:
        if numero >= 10:
            numero = numero // 10
            digito = digito + 1
        else:
            return digito

num = int(input("introduzca un numero: "))
total = cantidad(num)
suma_digito(num, total)
