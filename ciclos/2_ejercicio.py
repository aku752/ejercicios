#2.- El promedio de prácticas de un curso se calcula en base
#a cuatro prácticas calificadas de las cuales se elimina la
#nota menor y se promedian las tres notas más altas.
#Diseñe un algoritmo que determine la nota eliminada y el
#promedio de prácticas de un estudiante.
def promedio(n1, n2, n3 ,n4):
    if n1 < n2 and n1 < n3 and n1 < n4:
        menor = n1
    else:
        if n2 < n1 and n2 < n3 and n2 < n4:
            menor = n2
        else:
            if n3 < n1 and n3 < n2 and n3 < n4:
                menor = n3
            else:
                menor = n4
    print("La nota menor es: ", menor)
    if n1 == menor:
        if n2 == menor:
            if n3 == menor:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n4) / 3
                    print(" La nota es :", nota)
            else:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n4) / 3
                    print(" La nota es :", nota)
        else:
            if n3 == menor:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n4) / 3
                    print(" La nota es :", nota)
            else:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n2 + n3 + n4) / 3
                    print(" La nota es :", nota)
    else:
        if n2 == menor:
            if n3 == menor:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n4) / 3
                    print(" La nota es :", nota)
            else:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
        else:
            if n3 == menor:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)
                else:
                    nota = (n1 + n2 + n4) / 3
                    print(" La nota es :", nota)
            else:
                if n4 == menor:
                    nota = (n1 + n2 + n3) / 3
                    print(" La nota es :", nota)

n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))
n4 = int(input("Nota 4: "))
promedio(n1, n2, n3, n4)
