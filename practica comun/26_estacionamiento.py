horas = int(input("Horas de estacionamiento: "))
if horas <= 2:
    costo = 5
    total = costo*horas
elif horas <= 5:
    costo = 4
    total = (horas-2)*costo + 10
elif horas <= 10:
    costo = 3
    total = (horas-5)*costo + 22
elif horas > 10:
    costo = 2
    total = (horas-10)*costo + 31
print("-----------------------------")
print("Total a cobrar: ", total, "Bs")
