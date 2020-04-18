password = 2002
sw = True
while sw:
    salida = int(input("Escriba su contraseña: "))
    if salida == password:
        print("Acceso permitido...")
        sw = False
    else:
        print("Invalido")
