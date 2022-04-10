#  Пользователь вводит две буквы.
#  Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string
import math


def letters_place():
    a = input('Введите первую букву: ')
    b = input('Введите вторую окончания: ')
    letters = string.ascii_lowercase
    index_a = letters.index(a)
    index_b = letters.index(b)
    return print(a, ' стоит на ', index_a + 1, 'месте.\n', b, ' стоит на ', index_b + 1, 'месте.\n'
                'Между ними ', int(math.fabs(index_b-index_a)), 'буквы')


def main():
    try:
        letters_place()
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
