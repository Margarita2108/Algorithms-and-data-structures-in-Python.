# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.


def between_elem(a):
    max_ind = a.index(max(a))
    min_ind = a.index(min(a))
    if max_ind > min_ind:
        del a[max_ind:]
        del a[0:min_ind+1]
    else:
        del a[min_ind:]
        del a[0:max_ind + 1]
    print(a)
    print(sum(a))


def main():
    a = [9, 13, 2, 5, 9, 12, 13, 52, 95, 66, 36, 47, 11]
    between_elem(a)


if __name__ == '__main__':
    main()
