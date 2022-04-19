# Определить, какое число в массиве встречается чаще всего.


def most_common_value(b):
    max_counter = 1
    number = b[0]
    for i in range(len(b)-1):
        counter = 1
        for k in range(i+1, len(b)):
            if b[i] == b[k]:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            number = b[i]
    if max_counter > 1:
        print('Число ', number, 'встречается ', max_counter, 'раз')
    else:
        print('Нет повторений')


def main():
    a = [2, 5, 9, 11, 13, 13, 11, 36, 47, 11]
    most_common_value(a)


if __name__ == '__main__':
    main()
