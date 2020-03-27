#1.-   Una empresa tiene dos turnos (mañana y tarde) en los
#  que trabajan  n  empleados (la mitad de ellos por la mañana
#  y la otra mitad por la tarde).  Elabore un programa que
#  permita almacenar los sueldos de los empleados agrupados
#  en dos listas.  Imprimir las dos listas de sueldos y además
#  mostrar el salario mayor del primer turno y el salario
#  menor del segundo turno.
empleados = int(input("Cantidad de empleados mañana: "))
sueldo_mañana = []
mayor = 0
menor = 0
for i in range(1, empleados+1):
    sueldo = int(input("Sueldo: "))
    sueldo_mañana.append(sueldo)
    print("cantridsad-->", i)
    if sueldo >= mayor:
        mayor = sueldo
    else:
        menor = sueldo

# empleados = int(input("Cantidad de empleados tarde: "))
# sueldo_mañana = []
# for cantidad in range(empleados):
#     sueldo = int(input("Sueldo: "))
#     sueldo_mañana.append(sueldo)
#
# print("Sueldo de la mañana", sueldo_mañana)
# print("Sueldo de la tarde", sueldo_tarde)
