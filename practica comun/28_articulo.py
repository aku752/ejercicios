articulo = int(input("Costo de articulo: "))
a = 15
b = 12
c = 10
if articulo >= 200:
    descuento = (articulo/100) * a
    total = articulo - descuento
    porcentaje = a
elif 200 > articulo >= 100:
    descuento = (articulo/100) * b
    total = articulo - descuento
    porcentaje = b
elif articulo < 100:
    descuento = (articulo/100) * c
    total = articulo - descuento
    porcentaje = c
print("Porcentaje de descuento%: ", porcentaje, "%" )    
print("Descuento de: ", round(descuento,2), "Bs")
print("Total a pagar: ", round(total, 2), "Bs")
