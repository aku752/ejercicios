edad = int(input("Digite edad: "))
promedio = float(input("Digite promedio: "))
if edad > 18 and promedio >= 9:
    beca = 2000
elif edad > 18 and promedio >= 7.5:
    beca = 1000
elif edad > 18 and 6 <= promedio < 7.5:
    beca = 500
elif edad <= 18 and promedio >= 9:
    beca = 3000
elif edad <= 18 and 8 <= promedio < 9:
    beca = 2000
elif edad <= 18 and 6 <= promedio < 8:
    beca = 100
elif edad <= 18 and promedio < 6:
    beca = 0
if beca:
    print("La beca corresponde un total de: ", beca)
else:
    print("Se le enviara una invitacion")
