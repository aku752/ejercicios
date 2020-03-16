from math import sqrt
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
d = b*2 - 4*a*c
print("a = ", a)
print("b = ", b)
print("c = ", c)
if d > 0:
    x1 = -b + sqrt(d)/2*a
    x2 = -b - sqrt(d)/2*a
    print("x1 = ", x1)
    print("x2= ", x1)
elif d == 0:
    x1 = -b/2*a
    x2 = -b/2*a
    print("x1 = ", x1)
    print("x2 = ", x2)
else:
    print("Los valores son imaginarios")
