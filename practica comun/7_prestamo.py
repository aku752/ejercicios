prestamo = int(input("Introduzca prestamo: "))
tasa = int(input("Digite la tasa %: "))
adicional = (prestamo/100) * tasa
total = prestamo + adicional
print("Total a pagar: ", total)
