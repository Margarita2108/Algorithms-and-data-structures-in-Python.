# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы..

import random


def mergers_sort(a):
    if len(a) <= 1:
        return a
    left_side = mergers_sort(a[:len(a) // 2])
    right_side = mergers_sort(a[len(a) // 2:])
    i = 0
    j = 0
    res = []
    while i < len(left_side) or j < len(right_side):
        if i >= len(left_side):
            res.append(right_side[j])
            j += 1
        elif j >= len(right_side):
            res.append(left_side[i])
            i += 1
        elif left_side[i] < right_side[j]:
            res.append(left_side[i])
            i += 1
        else:
            res.append(right_side[j])
            j += 1
    return res


def main():
    try:
        n = int(input('Введите количество элементов массива: '))
        a = [random.randint(0, 50) for _ in range(n)]
        print(a)
        print(mergers_sort(a))
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
