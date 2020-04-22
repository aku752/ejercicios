actual = int(input("Ingrese año actual: "))
nacimiento = int(input("Ingrese año de nacimiento: "))
edad = actual - nacimiento
print("-----------------------------")
print("Edad: ", edad)
if 0 < edad <= 12:
    print("Se encuentra en etapa de niño")
if 13 < edad <= 17:
    print("Se encuentra en etapa de adolescente")
if 18 < edad <= 25:
    print("Se encuentra en etapa de joven")
if 26 < edad <= 59:
    print("Se encuentra en etapa de adulto")
if edad >= 60:
    print("Se encuentra en etapa de anciano")
