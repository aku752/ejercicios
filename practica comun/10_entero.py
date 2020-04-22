numero = int(input("Digite numero: "))
par_impar = numero%2
if numero == 0:
    print("Es Zero")
elif numero > 0:
    if par_impar:
        print("Positivo impar")
    else:
        print("Positivo par")
elif numero < 0:
    if par_impar:
        print("Negativo impar")
    else:
        print("Negativo par")
