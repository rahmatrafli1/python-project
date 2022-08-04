def selectionsort(S):
    n = len(S)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if S[j] < S[smallest]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]


list1 = [10, 50, 20, 30, 40]
selectionsort(list1)
print(list1)
