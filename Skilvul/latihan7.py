from functools import reduce

a = [1, 2, 3]
n = reduce(lambda x, y: x + (x*y), a)
print(n)
