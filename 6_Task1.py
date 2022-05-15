# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# нахождение второго минимального значения
# Windows 10 Pro x64
# Python 3.10 x64

import random
import sys


def two_min_elem_1(a):              # По времени
    b = sorted(a)                   # O(N log N)
    print(b[0], b[1])               # O(1)
    sum_size_1 = sys.getsizeof(a) + sys.getsizeof(b)
    print(sum_size_1)


def two_min_elem_2(a):
    min_1 = min(a)                  # O(N)
    a.remove(min_1)                 # O(N)
    min_2 = min(a)                  # O(N)
    print(min_1, min_2)             # O(1)
    sum_size_2 = sys.getsizeof(a) + sys.getsizeof(min_1) + sys.getsizeof(min_2)
    print(sum_size_2)


def two_min_elem_3(a):
    min_1 = a[0]                    # O(1)
    min_2 = a[0]                    # O(1)
    for i in range(1, len(a)):      # O(N)
        if a[i] < min_1:            # O(1)
            min_2 = min_1           # O(1)
            min_1 = a[i]            # O(1)
        else:
            if a[i] < min_2:        # O(1)
                min_2 = a[i]        # O(1)
    print(min_1, min_2)             # O(1)
    sum_size_3 = sys.getsizeof(a) + sys.getsizeof(min_1) + sys.getsizeof(min_2)
    print(sum_size_3)


def main():
    try:
        n = int(input('Введите количество элементов: '))
        a = [int(100000 * random.random()) for i in range(n)]
        two_min_elem_1(a)           # 0(N logN)
        two_min_elem_3(a)           # 0(N)
        two_min_elem_2(a)           # 0(N)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()

# Варианты с наиболее эффективным использованием памяти - это вторая и третья,
# первая задействует под констанды почти в 2 раза больше памяти.
# в ней участвуют 2 списка