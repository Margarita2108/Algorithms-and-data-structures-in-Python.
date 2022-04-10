# Найти сумму и произведение цифр
# трехзначного числа, которое вводит пользователь.

import math


def main():
    numbers = list(input('Введите трехзначное число:   '))
    numbers = [int(num) for num in numbers]
    print('Сумма чисел равна', sum(numbers), 'Произведение чисел чисел равно', math.prod(numbers))


if __name__ == '__main__':
    main()
