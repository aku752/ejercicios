#1.-   Una empresa tiene dos turnos (mañana y tarde) en los
#  que trabajan  n  empleados (la mitad de ellos por la mañana
#  y la otra mitad por la tarde).  Elabore un programa que
#  permita almacenar los sueldos de los empleados agrupados
#  en dos listas.  Imprimir las dos listas de sueldos y además
#  mostrar el salario mayor del primer turno y el salario
#  menor del segundo turno.
empleados = int(input("Cantidad de empleados mañana: "))
mitad = empleados // 2
sueldo_mañana = []
sueldo_tarde = []
for i in range(1, empleados+1):
    if i <= mitad:
        sueldo = int(input("Sueldo de empleado {}, turno mañana: ".format(i)))
        sueldo_mañana.append(sueldo)
    else:
        sueldo = int(input("Sueldo de empleados {}, turno tarde: ".format(i)))
        sueldo_tarde.append(sueldo)
print("\nSueldo turno mañana: ", sueldo_mañana)
sueldo_mañana.sort(reverse=True)
print("Sueldo mayor primer turno es de: ", sueldo_mañana[0])
print("\nSueldo turno tarde: ", sueldo_tarde)
sueldo_tarde.sort()
print("Sueldo menor segundo turno es de: ", sueldo_tarde[0])
