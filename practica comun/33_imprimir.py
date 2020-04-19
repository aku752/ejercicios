numero = int(input("Digite un numero: "))
sw = True
decimal = False
i = 0
j = 1
i_dec = 0.2
while sw:
    if decimal:
        k = j
        for m in range(1, 4):
            print(round(i_dec+i, 1), round(k+i_dec, 1))
            k += 1
        i_dec += 0.2
        if i_dec == 1:
            i_dec = 0.2
            decimal = False
            i += 1
            j = i + 1
    else:
        for n in range(1, 4):
            print(i, j)
            j += 1
        if i == numero:
            #Salida definitva
            sw = False
        j = i + 1
        decimal = True
