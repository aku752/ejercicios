horas = int(input("Horas de estacionamiento: "))
if horas <= 2:
    costo = 5
    total = costo*horas
elif horas <= 5:    costo = 4
    total = costo*horas
elif horas <= 10:
    costo = 3
    total = costo*horas
elif horas > 10:
    costo = 2
    total = costo*horas
print("-----------------------------")
print("Total a cobrar: ", total, "Bs")
