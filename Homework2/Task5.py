# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


# Т.к. я не совсем понял условия задачи предлагаю несколько решений.

#  Решение №1

num = list(input('Введите последовательность чисел через пробел: ').split())
numbers = list(map(int, num))
desired = int(input('Введите искомое число: '))


def finder(lst: list, des: int) -> str:
    counter = 0
    for i in range(len(lst)):
        if lst[i] == des:
            counter += 1
    return f'Искомое число {des} встречается {counter} раз.'


print(finder(numbers, desired))

#  Решение №2

lenght = int(input("Сколько будет чисел: "))
digit = int(input("Какую цифру ищем: "))


def counter(leng: int, dig: int):
    cnt = 0
    for i in range(1, leng + 1):
        num = int(input('Введите число: '))
        while num:
            if num % 10 == dig:
                cnt += 1
            num //= 10
    return f'Искомое число {dig} встречается {cnt} раз.'


print(counter(lenght, digit))
