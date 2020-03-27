#18.- Escriba un algoritmo para leer dos valores  enteros
#     distintos entre si, de tal forma que si el primer
#     número es mayor al segundo, genere una serie descendente,
#     caso contrario muestre una serie ascendente,
#     el factor de incremento o decremento es la unidad.
def generar(num1, num2):
    if num1 > num2:
        print("El primer numero es mayor, DESCENDERA: ")
        for i in range(num1, 0, -1):
            print(i, end=" ")
    else:
        print("El primer numero es menor, ASCENDERA: ")
        for i in range(1, num2+1):
            print(i, end=" ")

numero1 = int(input("Digite primer numero: "))
numero2 = int(input("Digite segundo numero : "))
generar(numero1, numero2)
