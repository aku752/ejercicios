#6.- Una agencia de venta de automóviles ofrece planes
# de crédito para la adquisición de los diferentes modelos
# de automóviles.
# Si el automóvil vale más de $15,000 la agencia solicita
# un 35% de pago inicial y el resto debe cubrirse en 24
# mensualidades sin intereses.
# Si el automóvil tiene un precio menor a $15,000 pero
# es mayor o igual a $10.000 se requiere un pago inicial
# del 25% del valor de vehículo y el resto se debe pagar
# en 18 mensualidades sin intereses.
# El algoritmo debe obtener en cada caso a cuánto
# asciende el pago inicial y cuánto debe pagar mensualmente.
def pago(precio):
    if precio > 15000:
        inicial = (precio/100) * 35
        pagar = precio - inicial
        mensual = pagar / 24
        print("Pago inicial: %.2f" % inicial)
        print("Pago de 24 cuotas, mensual: %.2f" % mensual)

precio = int(input("Precio auto: "))
pago(precio)
