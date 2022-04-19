# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# Несколько способов, через сортировку слишком легко))

def two_min_elem_1(a):
    b = sorted(a)
    print(b[0], b[1])


def two_min_elem_2(a):
    min_1 = min(a)
    a.remove(min_1)
    min_2 = min(a)
    print(min_1, min_2)


def two_min_elem_3(a):
    min_1 = a[0]
    min_2 = a[0]
    for i in range(1, len(a)):
        if a[i] < min_1:
            min_2 = min_1
            min_1 = a[i]
        else:
            if a[i] < min_2:
                min_2 = a[i]
    print(min_1, min_2)


def main():
    a = [9, 13, 2, 5, 9, 12, 13, 52, 95, 66, 36, 47, 11]
    two_min_elem_1(a)
    two_min_elem_3(a)
    two_min_elem_2(a)


if __name__ == '__main__':
    main()
