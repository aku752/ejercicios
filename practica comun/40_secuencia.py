cortar = 5
sw = 1
for i in range(36):
    binario = sw%2
    if i == cortar:
        cortar = cortar + 6
        print(binario, "\n", end=' ')
    else:
        print(binario, end=' ')
        sw += 1
