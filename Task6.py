# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше
# или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random


def guess_number(number):
    counter = 0
    while counter < 10:
        try:
            number_user = int(input('Введите число: '))
        except ValueError:
            print('Нужно вводить число. Потеря попытки.')
        if number_user == number:
            return print('Правильно')
        else:
            counter += 1
            if number_user > number:
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
    return print('Загаданное число - ', number)


def main():
    try:
        number = random.randint(0, 100)
        guess_number(number)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
