#Найти сумму и произведение цифр
#трехзначного числа, которое вводит пользователь.

def summ_numb(num):
    return sum(num)

def multipl_numb(num):
    return math.prod(num)

import math

def main():
    numbers = list(input('Введите трехзначное число:   '))
    numbers = [int(num) for num in numbers]
    print('Сумма чисел равна', summ_numb(numbers), 'Произведение чисел чисел равно', multipl_numb(numbers))

if __name__ == '__main__':
    main()