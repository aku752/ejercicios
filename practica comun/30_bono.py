sueldo = int(input("Digite sueldo: "))
antiguedad = int(input("Digite años de antiguedad: "))
if antiguedad >= 2 and antiguedad < 5:
    otorgar = (sueldo/100) * 20
elif antiguedad >= 5:
    otorgar = (sueldo/100) * 30
else:
    otorgar = 0
if sueldo <= 1800:
    bono = (sueldo/100) * 25
elif sueldo > 1800 and sueldo <= 3500:
    bono = (sueldo/100) * 15
elif sueldo > 3500:
    bono = (sueldo/100) * 10
print("--------------------------")
print("Bono de ", otorgar, "por antiguedad")
print("Bono de ", bono, "por sueldo")
