# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


def max_minus(a):
    b = []
    for i in range(0, len(a)):
        if a[i] < 0:
            b.append(a[i])
    print(max(b))


def main():
    a = [-2, 5, 9, -12, 13, 13, -66, 36, 47, -1, 1]
    max_minus(a)


if __name__ == '__main__':
    main()
