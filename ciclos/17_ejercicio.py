#17. Escribir un algoritmo que verifique si un número es perfecto o no,
# se dice que un número es perfecto si la suma de sus divisores es igual al número.
# Por ejemplo:
#   El 6 tiene como divisores 1,2  y 3, entonces 1+2+3 =6
#   el número 6 es perfecto
#   El 9 tiene como divisores 1, 3, entonces 1+3=4 no es perfecto.
def numero_perfecto(numero):
    mitad = numero // 2
    perfecto = 0
    suma = 0
    for valor in range(1, numero):
        if numero % valor == 0:
            suma = suma + valor
            perfecto = perfecto + valor
    if perfecto == numero:
        print("Es un numero perfecto: ", perfecto)
    else:
        print("No es un numero perfecto: ", numero)
        print("Total de la suma: ", suma)

numero = int(input("Digite un numero entero: "))
numero_perfecto(numero)
