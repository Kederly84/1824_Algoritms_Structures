# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

number = int(input('Введите число: '))


def num_check(num: int):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result


def num_theory(num: int):
    return num * (num + 1) / 2


for i in range(1, number + 1):
    print(num_check(i) == num_theory(i))