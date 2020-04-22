actual = int(input("Digite año: "))
if actual%4 == 0 and actual%100 != 0 or actual%400 == 0:
    print("Es año bisiesto")
else:
    print("No es año bisiesto")
