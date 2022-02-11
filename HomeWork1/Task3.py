# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

a = input('Введите координаты первой точки x,y через запятую: ')
b = input('Введите координаты второй точки x,y через запятую: ')


def the_equation(a: str, b: str) -> str:
    a_cord = list(map(int, a.split(',')))
    b_cord = list(map(int, b.split(',')))
    res_x = (b_cord[1] - a_cord[1]) / (b_cord[0] - a_cord[1])
    res_y = a_cord[1] - a_cord[0] * (b_cord[1] - a_cord[1]) / (b_cord[0] - a_cord[0])
    if res_y < 0:
        return f'y = x * {res_x} - {abs(res_y)}'
    elif res_y == 0:
        return f'y = x * {res_x}'
    else:
        return f'y = x * {res_x} + {res_y}'

print(the_equation(a, b))
