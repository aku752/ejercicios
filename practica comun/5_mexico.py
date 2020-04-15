lista = []
familia = int(input("Cantidad de familiares: "))
costo = 1250*familia
iva = (costo/100) * 12
total = costo + iva
print("Costo: ", costo)
print("Iva: ", iva)
print("Cantidad a pagar: ", total)
