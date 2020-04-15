a = int(input("Digite lado A: "))
b = int(input("Digite lado B: "))
c = int(input("Digite lado C: "))
if a == b == c:
    print("El triangulo es equilatero")
elif a != b and a != c and b != c:
    print("Es triangulo es escaleno")
else:
    print("Es triangulo isosceles")
