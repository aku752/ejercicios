a = int(input("Digite primer numero: "))
b = int(input("Digite segundo numero: "))
if b > a:
    for i in range(a, b+1):
        print(i)
elif a > b:
    for i in range(a, b-1, -1):
        print(i)
else:
    print("Numeros iguales")
