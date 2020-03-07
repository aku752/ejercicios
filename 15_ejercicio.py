#15.- Elabore un programa en el que dado
# un entero n > 1, calcule e imprima los elementos
# correspondientes a la conjetura de
# Ullman (en honor al matemático  Ullman)
# que consiste en lo siguiente:
# - Empiece con cualquier entero positivo.
# - Si es par, divídalo entre 2; si es impar multiplíquelo por 3 y agréguele 1.
# - Obtenga enteros sucesivamente repitiendo el proceso.
# Al final se obtendrá el número 1, independientemente del entero inicial. Por ejemplo, cuando el entero inicial es 26, la secuencia será:
# 26	13	40	20	10	5	16	8	4	2	1
def ullman(num):
    print(num)
    for i in range(11):
        if num % 2 == 0:
            num = num // 2
            print(num)
            if num == 1:
                break
        else:
            num = (num * 3) + 1

numero = int(input("Introduzca un numero mayor a 1: "))
ullman(numero)
