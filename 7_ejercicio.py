# 7.- Elabore un algoritmo que imprima los números
# del 1 al 100 excepto los múltiplos de 5 o 7
def imprimir():
    mult5 = 5
    mult7 = 7
    for valor in range(1, 101):
        if valor == mult5 or valor == mult7:
            if valor == mult5:
                mult5 = mult5 + 5
            if valor == mult7:
                mult7 = mult7 +7
        else:
            print(valor)

imprimir()
