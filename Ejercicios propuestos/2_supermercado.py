compra = int(input("Monto de compra: "))
if compra < 100:
    print("Total venta: ", compra)
elif compra >= 100 and compra < 500:
    desc = (compra/100)*5
    total = compra - desc
    print("Total venta 5% descuento: ", total)
elif compra >= 500:
    desc = (compra/100)*8
    total = compra - desc
    print("Total venta 8% descuento: ", total)
