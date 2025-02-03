def area_trapezoid(a, b, h):
    S_t = 0.5 * (a + b) * h
    return S_t


a = 2
b = 4
h = 2
print(f'Площадь трапеции со сторонами {a},  {b}  высотой {h} равна: {area_trapezoid(a, b, h)}')

