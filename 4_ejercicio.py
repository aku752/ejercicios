# 4.- Escribir un programa que lea el salario de un empleado y
# mediante un algoritmo efectué un incremento salarial
# en base a la siguiente escala:
# Si el salario es menor < 1000 Bs. incremente en un 20%
# Si el salario es mayor o igual a 1000 pero es menor a 3000 Bs. Incremente en un 15%
# Si el salario es mayor o igual a 3000 pero es menor a 6000 Bs. Incremente en un 10%
# Si el salario es mayor o igual a 6000 Bs.   Incremente en un 5%
# El algoritmo debe obtener el incremento y el nuevo salario.
def incremento(salario):
    if salario < 1000:
        print("Incremento de 20%")
        aumento = (salario/100) * 20
        salario = salario + aumento
    elif salario >= 1000 and salario < 3000:
        print("Incremento de 15%")
        aumento = (salario/100) * 15
        salario = salario + aumento
    elif salario >= 3000 and salario < 6000:
        print("Incremento de 10%")
        aumento = (salario/100) * 10
        salario = salario + aumento
    elif salario >= 6000:
        print("Incremento de 5%")
        aumento = (salario/100) * 5
        salario = salario + aumento

    print("Salario aumentado es :", salario)

salario = int(input("Escriba su salario: "))
incremento(salario)
