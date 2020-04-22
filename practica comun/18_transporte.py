distancia = int(input("Distancia recorrida: "))
peso = int(input("Digite peso: "))
if distancia < 200:
    total_costo = 2.5*peso
elif 800 >= distancia >= 200:
    total_costo = 3.5*peso + 2.5*peso
elif distancia > 800:
    total_costo = 5.5*peso + 3.5*peso + 2.5*peso
print("----------------------")
print("Peso transportado: ", peso, "Kg")
print("Ingreso recibido: ", total_costo, "Bs")
