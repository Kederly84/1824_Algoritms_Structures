# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

values = [i for i in range(2, 10)]
finish = 99


def checker(a: list, finish: int) -> dict:
    result = {}
    for i in a:
        result[i] = finish // i
    return result


print(checker(values, finish))
