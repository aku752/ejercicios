# 5.- Una empresa efectúa el control de asistencia de sus empleados
# mediante un lector biométrico, el horario en la entrada es a
# las 8:00 a.m y la salida es a las 16:00 p.m.
# El empleado tiene una tolerancia de 10 minutos en la entrada,
# si llega más allá de los 10 minutos de tolerancia se penaliza
# todos los minutos de atraso (es decir si llega a las 8:12
# se penalizan los 12 minutos). De igual forma no puede
# salir antes del horario establecido en la salida,
# (si lo hace se penaliza los minutos faltantes), pero si
# el empleado entra antes o sale después de sus horarios el
# sistema solo toma en cuenta las 8 horas laborales de trabajo.
# El problema consiste en determinar los minutos de penalización
# para el empleado en cualquier día laboral. Resolver este problema
# para los siguientes casos:
#   Empleado 	Hora Entrada 	Hora Salida 	Penalización
#   1 		            7:55 		16:15 		 0
#   2 		            8:11 		16:00 		 11
#   3 		            8:30 		16:20 		 30
#   4 		            8:05 		16:10		 0
# Se sugiere leer las horas y minutos de entrada y las horas y minutos
# de salida.

def horario(cantidad):
    for i in range(1, cantidad+1):
        ent_h = int(input("Hora entrada: "))
        ent_m = int(input("Minutos entrada: "))
        entrada = f"      {ent_h}:{ent_m}"
        sal_h = int(input("Hora salida: "))
        sal_m = int(input("Minutos salida: "))
        salida = f"      {sal_h}:{sal_m}"
        print("Empleado    Entrada    Salida    Penalizacion ")

        if ent_h < 8:
            if sal_h < 16:
                penal = 60 - sal_m
                print(i, "    ", entrada, salida, "   ", penal)
            else:
                penal = 0
                print(i, "    ", entrada, salida, "   ", penal)
        else:
            if ent_m <= 10:
                if sal_h < 16:
                    penal = 60 - sal_m
                    print(i, "    ", entrada, salida, "   ", penal)
                else:
                    penal = 0
                    print(i, "    ", entrada, salida, "   ", penal)
            else:
                if sal_h < 16:
                    penal = 60 - sal_m
                    penal = ent_m + penal
                    print(i, "    ", entrada, salida, "   ", penal)
                else:
                    penal = ent_m
                    print(i, "    ", entrada, salida, "   ", penal)


empleados = int(input("Cantidad de empleados: "))
horario(empleados)
