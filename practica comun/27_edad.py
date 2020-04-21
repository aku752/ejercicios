personas = []
edades = []
for i in range(3):
    persona = str(input("Nombre: "))
    edad = int(input("Edad: "))
    personas.append(persona)
    edades.append(edad)
    print("---------------------")
edades.sort()
print(edades)
