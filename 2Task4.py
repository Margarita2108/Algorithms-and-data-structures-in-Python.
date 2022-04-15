# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def sum_elem(numb):
    counter = 0
    sum_el = 1
    sum_all = 0
    while counter < numb:
        sum_all = sum_all + sum_el
        sum_el = -(sum_el/2)
        counter += 1
    return print(sum_all)


def main():
    try:
        number = int(input('Введите количество элементов: '))
        sum_elem(number)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
