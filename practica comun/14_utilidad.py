salario = int(input("Digite salario: "))
antiguedad = int(input("Digite antiguedad: "))
if antiguedad < 1:
    utilidad = (salario/100) * 5
elif 2 > antiguedad >= 1 :
    utilidad = (salario/100) * 7
elif 5 > antiguedad >= 2 :
    utilidad = (salario/100) * 10
elif 10 > antiguedad >= 5 :
    utilidad = (salario/100) * 15
elif antiguedad >= 10 :
    utilidad = (salario/100) * 20
print("Utilidad de: ", utilidad)
