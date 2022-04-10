# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.


def line_coopd():
    x1 = float(input('Введите х первой точки: '))
    y1 = float(input('Введите у первой точки: '))
    x2 = float(input('Введите х второй точки: '))
    y2 = float(input('Введите у второй точки: '))

    k = (y1 - y2)/(x1 - x2)
    b = y1 - k * x1

    print('Формула прямой у=', k, 'x+', b)


def main():
    try:
        line_coopd()
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()

