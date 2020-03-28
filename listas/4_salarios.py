#4.- Almacenar en una lista los nombres y los salarios de n empleados,
# luego eliminar a  los empleados que tienen un sueldo mayor a 10000
#(tanto el sueldo como su nombre).
empleados = int(input("Cantidad de empleados: "))
lista = []
menor = []
for i in range(empleados):
    nombre = str(input("\nNombre: "))
    salario = int(input("Salario: "))
    lista.append([nombre,salario])
nuevo = lista
print("\nLista de empleados: ", lista)
for i in range(empleados):
    salario = lista[i][1]
    if salario <= 10000:
        menor.append(lista[i])

print("\nEmpleados con salario menor a 10000: ", menor)
