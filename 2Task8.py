# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.


def check_num(numbers, number):
    counter = 0
    for numb in range(1, numbers + 1):
        num_input = int(input('Введите ' + str(numb) + ' число: '))
        list_num = [int(_) for _ in num_input]
        for num in list_num:
            if num == number:
                counter += 1
    print('Число ', number, 'встретилось ', counter, 'раз')


def main():
    try:
        number_list = int(input('Введите количество чисел: '))
        number_user = int(input('Введите цифру поиска: '))
        check_num(number_list, number_user)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
