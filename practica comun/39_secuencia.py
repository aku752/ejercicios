n = int(input("Digite cantidad de numeros(n): "))
m = n
for i in range(1, n+1):
    # print(i, end=' ')
    for j in range(1, m+1):
        print(j, end=' ')
    m -= 1
    print("\n")
