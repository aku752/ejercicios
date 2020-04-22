numeros = []
for i in range(3):
    num = int(input("Digite numero: "))
    numeros.append(num)
numeros.sort()
print("-----------------------")
print("El mayor es: ", numeros[2])
