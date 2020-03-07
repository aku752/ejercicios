#11.- Una empresa desea conocer el monto total de comisión
#que debe pagar a un vendedor, correspondiente a un conjunto
# de varias ventas realizadas por este, bajo las siguientes condiciones:

#Si la venta es menor a  $1,000.00, se le otorga el 3% de comisión.
#Si la venta es de $1,000.00 o más, el vendedor recibe el 5% de comisión.
def comision(venta):
    if venta < 1000:
        pagar = (venta/100)*3
        total = pagar + venta
        print("Debe pagarle por el 3%: ", total)
    else:
        pagar = (venta/100)*5
        total = pagar + venta
        print("Debe pagarle por el 5%: ", total)


venta = float(input("Digite venta: "))
comision(venta)
