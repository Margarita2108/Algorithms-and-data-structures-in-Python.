# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


def matrix(m, n):
    a = []
    for i in range(n):
        b = [int(i) for i in input('Введите 4 числа через пробел: ').split()]
        while len(b) < 4:
            b = [int(i) for i in input('Чисел не достаточно. Введите 4 числа через пробел: ').split()]
        del b[4:]
        b.append(sum(b))
        a.append(b)
    for ind in range(n):
        i = 0
        for k in a[ind]:
            if i < m-1:
                print(f"{k:<5} ", end=' ')
                i += 1
            else:
                print(f"{k:<5} ")


def main():
    try:
        matrix(5, 4)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
