def get_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2


result1, result2 = get_root(a=1, c=-8, b=2)
print('Hasil akar-akarnya adalah', result1, 'atau', result2)
