horas = int(input("Horas: "))
precio = int(input("Precio por hora: "))
if horas <= 40:
    total = horas*precio
else:
    extra = horas - 40
    if extra <= 8:
        total = extra*precio*2
        print("Horas dobles: ", extra)
    else:
        trabajo_doble = 8 * 2
        pago_doble = precio*trabajo_doble
        triple = extra - 8
        precio_triple = triple*precio*3
        total = precio_triple + pago_doble
        print("Horas dobles: 8  ","monto: ", pago_doble)
        print("Horas triples: ", triple, "monto:", precio_triple)
print("----------------------")
print("Total a pagar: ", total)
