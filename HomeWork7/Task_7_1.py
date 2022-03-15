# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint

# генератор списка чисел
input_array = [randint(0, 10) for i in range(10)]


def median(nums):
    arr_sum = 0
    for num in nums:
        arr_sum += num

    left_sum = 0
    for i in range(len(nums)):
        arr_sum -= nums[i]
        if left_sum == arr_sum:
            return i
        left_sum += nums[i]


print(input_array)
print(median(input_array))
