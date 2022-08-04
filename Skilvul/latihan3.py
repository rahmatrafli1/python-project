def test123(a, b):
    if a > b:
        return a + b, "OK!"
    else:
        return a - b, "Not OK!"


print(test123(1, 2))
