# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их
#
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import timeit
import random


def two_min_elem_1(a):
    b = sorted(a)       # O(N log N)
    print(b[0], b[1])   # O(1)


def two_min_elem_2(a):
    min_1 = min(a)      # O(N)
    a.remove(min_1)     # O(N)
    min_2 = min(a)      # O(N)
    print(min_1, min_2) # O(1)


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


def main():
    start_time = timeit.default_timer()
    a = [int(10000000*random.random()) for i in range(10000000)]
    print(timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    two_min_elem_1(a)                                   # итоговая сложность 0(N logN) ~время выполнения 9.2 сек на 10 млн значений
    print(timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    two_min_elem_3(a)                                   # итоговая сложность 0(N) ~время выполнения 1,8 сек на 10 млн значений
    print(timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    two_min_elem_2(a)                                   # итоговая сложность 0(N) ~время выполнения 0,4 сек на 10 млн значений
    print(timeit.default_timer() - start_time)


if __name__ == '__main__':
    main()
