#  Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def mean_numb():
    numbers = [float(i) for i in input('Введите три разных числа через пробел: ').split()]
    for numb in numbers:
        if numb != max(numbers) and numb != min(numbers):
            print('Среднее число - ', numb)
        continue


def main():
    try:
        mean_numb()
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
