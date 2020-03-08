#9- Leer el valor de un bien (costo original), su vida útil (años)
# y muestre por pantalla su depreciación en cada año,
# hasta alcanzar su vida útil.
#		Factor depreciación (fd) = costo/vida útil
#		Depreciacion1 = Depreciacion0 (Costo original) – fd
#Ejemplo:   Valor del bien = 1000 Bs.	Vida Útil = 5 años
#			Año	Valor depreciado
#			  1		800
#			  2     600
#			  3		400
#			  4		200
#			  5       0
def calcular(costo, vida):
    print("Año     Valor depreciado")
    factor_depre = costo / vida
    for tiempo in range(1, vida+1):
        costo = costo - factor_depre
        print(tiempo, "      ", costo)

costo = int(input("Introduzca costo: "))
vida = int(input("Introduzca vida util: "))
calcular(costo, vida)
