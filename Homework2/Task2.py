# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)

number = int(input('Введите число: '))


def reverse_num(num: int) -> int:
    reverse = 0
    while num:
        a = num % 10
        reverse = reverse * 10 + a
        num //= 10
    return reverse

print(reverse_num(number))
