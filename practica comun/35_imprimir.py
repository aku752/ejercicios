n = int(input("Digite numero(N): "))
for i in range(n):
    i += 1
    j = k = i
    j *= j
    k *= j
    print("\n", i," ", j, " ", k)
    print("\n", i," ", j+1, " ", k+1)
