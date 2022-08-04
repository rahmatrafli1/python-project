list_umur = [1, 10, 30, 20, 15]
for a in filter(lambda x: x % 2 == 0, list_umur):
    print(a, end=' ')
