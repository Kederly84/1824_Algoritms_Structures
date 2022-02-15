# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = input('Введите первую букву (регистр важен): ')
b = input('Введите вторую букву (регистр важен): ')


def letter_function(a: str, b: str) -> str:
    if a.isupper():
        pos_a = ord(a) - ord('A') + 1
        pos_b = ord(b.upper()) - ord('A') + 1
    else:
        pos_a = ord(a) - ord('a') + 1
        pos_b = ord(b.lower()) - ord('a') + 1
    if pos_a == pos_b:
        return f'Это одна и та же буква. Позиция буквы {pos_a}. Между ними 0 букв.'
    elif pos_a > pos_b:
        return f'Вы что то сделали не так.'
    else:
        letters = pos_b - pos_a - 1
        return f'Позиция первой буквы {pos_a}. Позиция второй буквы {pos_b}. Между ними {letters} букв.'

print(letter_function(a, b))
