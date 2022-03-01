# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = list(input('Введите числа через пробел: ').split())
numbers = list(map(int, num))


def finder(lst: list):
    first_num = 0
    second_num = 0
    find_num = 0
    compare_num = 0
    for i in lst:
        compare_num = i
        while i:
            second_num += i % 10
            i //= 10
        if second_num >= first_num:
            find_num = compare_num
    return f'Искомое число {find_num}'


print(finder(numbers))
