#13.- Leer un número entero y determinar la
#suma de sus dígitos pares.
def suma(num):
    sumar = 0
    while True:
        modulo = num % 10
        num = num // 10
        if modulo % 2 == 0:
            sumar = sumar + modulo
        if num < 1:
            break

    print("La suma de pares es:", sumar)

numero = int(input("digite numero:"))
suma(numero)
