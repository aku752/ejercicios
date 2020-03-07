#10.- Dado un numero entero, determine cuantas veces se repite
#un digito que se lea desde el teclado.
#Ej:
#Sea num= 28365535    y el digito a ingresar   dig=5
#El resultado a obtener será 3, puesto que el 5 se repite 3 veces
def cantidad(numero, digito):
    c = 0
    while True:
        if numero >= 10:
            modulo = numero % 10
            numero = numero // 10
            if numero == digito:
                c = c + 1
                print(f"El digito en {numero} se repite {c}")
                break
        else:
            if numero == digito:
                print("El digito se repite 1 vez" )
                break
            else:
                print("No hay digitos que se repiten")
                break

numero = int(input("Introduzca numero: "))
digito = int(input("Digito a buscar: "))

cantidad(numero, digito)
