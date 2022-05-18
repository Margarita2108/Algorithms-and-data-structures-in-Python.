# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return a


def main():
    try:
        n = int(input('Введите количество элементов массива: '))
        a = [random.randint(-100, 100) for _ in range(n)]
        print(a)
        print(bubble_sort(a))
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
