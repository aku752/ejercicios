numero_cita = int(input("Digite cita: "))
if numero_cita <= 3:
    costo_cita = 200
    total = numero_cita*costo_cita
elif numero_cita <= 5:
    costo_cita = 150
    total = (numero_cita-3) * costo_cita + 600
elif numero_cita <= 8:
    costo_cita = 100
    total = (numero_cita-5) * costo_cita + 900
else:
    costo_cita = 50
    total = (numero_cita-8) * costo_cita + 1200
print("Costo de cita: ", costo_cita)
print("Total: ", total)
