a = int(input("Digite numer A: "))
b = int(input("Digite numer B: "))
c = int(input("Digite numer C: "))
if a + b == c:
    print("Iguales")
elif a + c == b:
    print("Iguales")
elif b + c == a:
    print("Iguales")
else:
    print("Distintos")
