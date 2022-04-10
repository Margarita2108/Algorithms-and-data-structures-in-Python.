# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.


import random
import string


def random_1():
    a = int(input('Введите ограничение min: '))
    b = int(input('Введите ограничение max: '))
    return print('Случайное целое число: ', random.randint(a, b))


def random_2():
    a = float(input('Введите ограничение min: '))
    b = float(input('Введите ограничение max: '))
    return print('Случайное вещественное число: ', random.random()*(b - a) + a)


def random_3():
    a = input('Введите начальную букву: ')
    b = input('Введите букву окончания: ')
    letters = string.ascii_lowercase
    index_a = letters.index(a)
    index_b = letters.index(b)
    return print('Случайная буква: ', letters[random.randint(index_a, index_b)])


def main():
    try:
        type_rand = input('Введите:\n1 - для генерации целого числа\n'
                          '2 - для генерации вещественного числа\n'
                          '3 - для генерации буквы\n')
        if type_rand == '1':
            return random_1()
        elif type_rand == '2':
            return random_2()
        elif type_rand == '3':
            return random_3()
        else:
            print('Неверный выбор')
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
