def bubblesort(S):
    n = len(S)
    for i in range(n):
        print(S)  # untuk mengetahui proses yang terjadi
        for j in range(n - 1):
            if S[j] > S[j + 1]:
                S[j], S[j + 1] = S[j + 1], S[j]


list1 = [10, 50, 20, 30, 40]
print("Sebelum:", list1)
bubblesort(list1)
print("Sesudah:", list1)
