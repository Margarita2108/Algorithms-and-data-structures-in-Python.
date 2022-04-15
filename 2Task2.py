# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

def recalculation_figures(number):
    nums = [int(_) for _ in number]
    even_num = 0
    odd_num = 0
    for num in nums:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    return print('В числе ', even_num, 'четных и ', odd_num, ' нечетных цифр')


def main():
    try:
        number = input('Введите число: ')
        recalculation_figures(number)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
