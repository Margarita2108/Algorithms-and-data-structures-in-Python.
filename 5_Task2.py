# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections
import sys


signs = '0123456789ABCDEF'
trans_numbers = collections.defaultdict(int)
counter = 0
for key in signs:
    trans_numbers[key] += counter
    counter += 1


def numbers_control(number):
    for numb in number:
        if signs.find(numb) == -1:
            print('Неверный ввод')
            sys.exit()


def trans_numbers_ten(n):
    num_ten = 0
    num = collections.deque(n)
    num.reverse()
    for i in range(len(num)):
        num_ten += trans_numbers[num[i]] * 16 ** i
    return num_ten


def trans_numbers_sixteen(n):
    num_sixteen = collections.deque()
    while n > 0:
        d = n % 16
        for i in trans_numbers:
            if trans_numbers[i] == d:
                num_sixteen.append(i)
        n //= 16
    num_sixteen.reverse()
    return list(num_sixteen)


def main():
    first_number = list(input('Введите первое число: ').upper())
    second_number = list(input('Введите второе число: ').upper())
    numbers_control(first_number)
    numbers_control(second_number)
    a = trans_numbers_ten(first_number)
    b = trans_numbers_ten(second_number)
    c = trans_numbers_sixteen(a + b)
    d = trans_numbers_sixteen(a * b)
    print(f'Сумма чисел: {c}')
    print(f'Произведение чисел: {d}')


if __name__ == '__main__':
    main()


