from math import sqrt
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
x1 = 0
x2 = 0
d = b*2 - 4*a*c
if d > 0:
    x1 = -b + sqrt(d)/2*a
    x2 = -b - sqrt(d)/2*a
elif d == 0:
    x1 = -b/2*a
    x2 = -b/2*a
else:
    print("Los valores son imaginarios")
