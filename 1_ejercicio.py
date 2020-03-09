#1.- En una empresa se tiene a los empleados agrupados por categorías:
# Los de categoría 1 ganan 10.000 Bs
# Los de categoría 2 ganan  7.500 Bs
# Los de categoría 3 ganan  5.000 Bs.
# Los  de categoría 4 ganan  3500 Bs.
# Se requiere un algoritmo que permita determinar cuánto debe pagarse
# a un empleado si se conoce el número de horas que trabajó durante
# el mes (idealmente debería trabajar 160 horas) y la categoría a la
# que pertenece. Se sabe que a todos se les descuenta un 7.5% concepto
# de salud, y si el salario total mensual es menos de 1´000.000, se
# le da un subsidio del 15% sobre su salario mensual (sin descuentos).
# A todos se les descuenta el 7.5% por aporte al fondo solidario y
# si el total ganado es menor # a 1.000 Bs., recibe un subsidio
# del 15% sobre este total, determinar el total ganado y el total neto.
def pagar(categoria, horas):
    if categoria == 1:
        salario_hora = 10000/160
        pagar = salario_hora * horas
        print("Ganado en horas: ", pagar)/
        descuento = (pagar/100) * 7.5
        pagar = pagar - descuento*2
        print("Cancelar: ", pagar)



categoria = int(input("Categoria: "))
horas = int(input("Horas trabajadas: "))
pagar(categoria, horas)
