# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.



from random import randint

# генератор списка чисел
input1 = [3, 28, 75, 99, 57, 85, 84, 21, 38, 40]
input2 = [randint(1, 100) for i in range(10)]
print(input1)
print(input2)

def min_finder(lst: list) -> str:
    min_pos_1 = 0
    min_pos_2 = 1
    if lst[min_pos_1] > lst[min_pos_2]:
        min_pos_1 = 1
        min_pos_2 = 0
    for i in range(2, len(lst)):
        if lst[i] <= lst[min_pos_1]:
            min_pos_2 = min_pos_1
            min_pos_1 = i
        elif lst[i] <= lst[min_pos_2]:
            min_pos_2 = i
    return f'Минимальный элемент № {min_pos_1} со значением {lst[min_pos_1]}. ' \
           f'Второй минимальный элемент № {min_pos_2} со значением {lst[min_pos_2]}'


print(min_finder(input1))
print(min_finder(input2))
