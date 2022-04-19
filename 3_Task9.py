# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random


def maximum_among_min(m, n):
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(int(random() * 101))
            print(f"{b[j]:<5} ", end=' ')
        a.append(b)
        print()
    for i in range(m):
        print("--    ", end=' ')
    print()

    max_elem = 0
    for i in range(m):
        min_elem = a[0][i]
        for j in range(1, n):
            if min_elem > a[j][i]:
                min_elem = a[j][i]
        print(f"{min_elem:<5} ", end=' ')
        if max_elem < min_elem:
            max_elem = min_elem
    print()
    print('Максимум из минимумов - ', max_elem)


def main():
    maximum_among_min(8, 9)


if __name__ == '__main__':
    main()
