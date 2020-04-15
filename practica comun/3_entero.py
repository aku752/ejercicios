numero = int(input("Introduzca numero: "))
valor = numero%2
if valor == 0:
    if numero > 0:
        print("El numero {} es par positivo".format(numero))
    elif numero == 0:
        print("El numero es cero")
    else:
        print("El numero {} es par negativo".format(numero))
else:
    if numero > 0:
        print("El numero {} es impar positivo".format(numero))
    else:
        print("El numero {} es impar negativo".format(numero))
