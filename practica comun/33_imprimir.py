numero = int(input("Digite un numero: "))
sw = True
decimal = False
i = 0
j = 1
i_dec = 0.2
while sw:
    if decimal:
        print("-------------------")
        k = j
        for m in range(1, 4):
            print("I= ", round(i_dec+i, 1), "J= ", round(k+i_dec, 1))
            k += 1

        i_dec += 0.2
        if i_dec == 1:
            i_dec = 0.2
            decimal = False
            i += 1
            j = i + 1
    else:
        print("-------------------")
        for n in range(1, 4):
            print("I= ", i, " ", "J= ", j)
            j += 1
        if i == numero:
            #Salida definitiva
            sw = False
        j = i + 1
        decimal = True
