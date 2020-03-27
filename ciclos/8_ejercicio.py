#8.-  Escriba un programa que presente en pantalla la tabla de
# multiplicar entre 1 y 10 (verifique este valor),
# para un valor que ingrese el usuario.
# Ej: El usuario ingresa el 6, el programa debería imprimir:
#			6 * 1 = 6
#			6 * 2 = 12
#			…….
#			6 * 9 = 54
#			6* 10 = 60
def multiplicar(valor):
    for i in range(1, 10):
        print(valor, " x ", i, " = ", valor*i)

valor = int(input("Ingrese valor: "))
multiplicar(valor)
