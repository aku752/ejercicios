#5.- Almacenar en una lista los nombres de varias personas,
#y luego insertar entre cada nombre un número correlativo
#de 1 a n.
#Sea la lista:
#		L=[“Juan ”,”Maria”,”Carlos”,”Jose”,”Carol”]
#		L=[1, ”Juan”, 2 ,”Maria, 3, …….]
personas = int(input("Cantidad de personas: "))
lista = []
for i in range(personas):
    nombre = str(input("Escriba nombre {}: ".format(i+1)))
    lista.append(nombre)
j = 0
for i in range(personas):
    lista.insert(j, i+1)
    j = j + 2
print("La lista intercalada es: ", lista)
