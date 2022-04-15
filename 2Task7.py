# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def check_summ(number):
    numbers = list(range(1, number+1))
    if sum(numbers) == number * (number + 1) / 2:
        print('Равенство верно', sum(numbers), ' = ', number * (number + 1) / 2)
    else:
        print('Равенство не верно')


def main():
    try:
        number_user = int(input('Введите n: '))
        check_summ(number_user)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
