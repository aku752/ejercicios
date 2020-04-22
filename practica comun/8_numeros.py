a = int(input("Digite numero A: "))
b = int(input("Digite numero B: "))
if a == b:
    resp = a*b
    print("-----------------------------------")
    print("Son iguales, se multiplicara: ")
elif a > b:
    resp = a - b
    print("-----------------------------------")
    print("El primero es mayor que el segundo, se restara: ")
else:
    print("Se sumara: ")
    resp = a + b
print("Resultado: ", resp)
