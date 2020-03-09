#3.- El Hospital Regional de la UCB está haciendo un estudio
# del costo que representa la atención de pacientes en la
# Unidad de Tratamiento Intensivo. Los pacientes están clasificados
# en cuatro categorías (numeradas de 1 a 4), dependiendo
# del tipo de atención que requieren. La categoría 1
# representa Bs. 1200 diarios, mientras que la 2 involucra
# Bs. 1500, la 3 Bs.1700 y la 4 Bs. 2000 mil. Además,
# los pacientes muy jóvenes (menores de 15 años), y los de
# edad avanzada, (mayores de 70 años), involucran un costo
# adicional de 20%. Necesitamos un algoritmo que calcule
# el costo total de un paciente particular que ha pasado
# una determinada cantidad de días en la UTI
# (Unidad de Terapia Intensiva) del hospital.
def atencion(categoria, edad, dias):
    if categoria == 1:
        if edad < 15 or edad > 70:
            costo = (1200/100) * 20
            total = (costo + 1200) * dias
            print("Total a pagar: ", total)
        else:
            total = 1200 * dias
            print("Total a pagar: ", total)
    if categoria == 2:
        if edad < 15 or edad > 70:
            costo = (1500/100) * 20
            total = (costo + 1500) * dias
            print("Total a pagar: ", total)
        else:
            total = 1500 * dias
            print("Total a pagar: ", total)
    if categoria == 3:
        if edad < 15 or edad > 70:
            costo = (1700/100) * 20
            total = (costo + 1700) * dias
            print("Total a pagar: ", total)
        else:
            total = 1700 * dias
            print("Total a pagar: ", total)
    if categoria == 4:
        if edad < 15 or edad > 70:
            costo = (2000/100) * 20
            total = (costo + 2000) * dias
            print("Total a pagar: ", total)
        else:
            total = 2000 * dias
            print("Total a pagar: ", total)

categoria = int(input("Categoria: "))
edad = int(input("Edad: "))
dias = int(input("Dias atendido: "))

atencion(categoria, edad, dias)
