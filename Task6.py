# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string


def place_letters():
    a = int(input('Введите номер буквы (до 24): '))
    letters = string.ascii_lowercase
    return print('Под номером ', a, ' буква ', string.ascii_lowercase[a-1])


def main():
    try:
        place_letters()
    except IndexError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
