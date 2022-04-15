# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def max_num(numbers):
    max_sum_numb = 0
    max_numb = 0
    for numb in range(1, numbers + 1):
        num_input = int(input('Введите ' + str(numb) + ' число: '))
        list_num = [int(_) for _ in num_input]
        if sum(list_num) > max_sum_numb:
            max_sum_numb = sum(list_num)
            max_numb = num_input

    print('Число ', max_numb, 'его ссумма ', max_sum_numb, 'раз')


def main():
    try:
        number_list = int(input('Введите количество чисел: '))
        max_num(number_list)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
