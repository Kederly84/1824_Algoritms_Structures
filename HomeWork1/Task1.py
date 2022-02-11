# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введи число: ')


def operations_of_numbers(a: str) -> int:
    sum_digits = 0
    product_of_num = 1
    if a.isdigit():
        for i in a:
            sum_digits = sum_digits + int(i)
            product_of_num = product_of_num * int(i)
        return f'Сумма чисел = {sum_digits}. Произведение чисел равно = {product_of_num}'
    else:
        return "Это не число"


print(operations_of_numbers(number));
