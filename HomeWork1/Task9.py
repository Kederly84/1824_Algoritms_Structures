#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))


def compare(a: int, b: int, c: int) -> str:
    if b < a < c or c < a < b:
        return a
    elif a < b < c or c < b < a:
        return b
    else:
        return c


print(f'Среднее число {compare(a, b, c)}')

