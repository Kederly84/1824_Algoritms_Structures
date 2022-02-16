# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите длину ряда: '))


def sum_of_progression(num: int) -> float:
    counter = 0
    start_pos = 1
    result = 0
    while counter < num:
        result += start_pos
        start_pos /= -2
        counter += 1
    return result


print(sum_of_progression(n))
