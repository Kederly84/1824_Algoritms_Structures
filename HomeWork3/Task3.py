# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

# генератор списка чисел
input_array = [randint(1, 100) for i in range(10)]
print(input_array)


def sum_array(lst: list) -> int:
    pos_max = 0
    pos_min = 0
    max_val = lst[pos_max]
    min_val = lst[pos_min]
    list_sum = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > max_val:
            pos_max = i
            max_val = lst[i]
        if lst[i] < min_val:
            pos_min = i
            min_val = lst[i]
    for _ in range(min(pos_min, pos_max) + 1, max(pos_min, pos_max)):
        list_sum += lst[_]
    return list_sum


print(sum_array(input_array))
