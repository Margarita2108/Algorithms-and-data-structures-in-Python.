# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


def min_max_change(a):
    max_ind = a.index(max(a))
    min_ind = a.index(min(a))
    print(a)
    a[max_ind], a[min_ind] = a[min_ind], a[max_ind]
    print(a)


def main():
    a = [2, 5, 9, 12, 13, 52, 95, 66, 36, 47, 11]
    min_max_change(a)


if __name__ == '__main__':
    main()
