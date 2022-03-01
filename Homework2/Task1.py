# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

from unittest import TestCase


number = int(input('Введите число: '))


def numbers(a: int) -> str:
    if a == 0:
        return f'Одна четная цифра'
    even = 0
    odd = 0
    while a:
        counter = a % 10
        if counter % 2 == 0 or counter == 0:
            even += 1
        else:
            odd += 1
        a -= counter
        a //= 10
    return f'Количество четных цифр = {even}, нечетных = {odd}'


print(numbers(number))
