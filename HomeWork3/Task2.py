# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

# генератор списка чисел
input_array = [randint(1, 100) for i in range(10)]

# вывод списка
print(input_array)


def changer(lst: list) -> list:
    pos_max = 0
    pos_min = 0
    max_val = lst[pos_max]
    min_val = lst[pos_min]
    for i in range(1, len(lst) - 1):
        if lst[i] > max_val:
            pos_max = i
            max_val = lst[i]
        if lst[i] < min_val:
            pos_min = i
            min_val = lst[i]
    lst[pos_max], lst[pos_min] = min_val, max_val
    return lst


print(changer(input_array))
