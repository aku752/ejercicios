#12.- En el rango de 1 a n (leído desde el teclado determine
# la cantidad de múltiplos de 5 que existen en dicho rango.
def multiplos(rango):
    c = 0
    for i in range(1, rango+1):
        numero = int(input("Digite numero: "))
        if numero % 5 == 0:
            c = c + 1
    print("Cantidad de multiplos: ", c)

rango = int(input("Digite cantidad a introducir: "))
multiplos(rango)
