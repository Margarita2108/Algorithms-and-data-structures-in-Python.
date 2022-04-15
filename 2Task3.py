# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

def mirror(number):
    numb_dec = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        numb_dec = numb_dec * 10
        numb_dec = numb_dec + remainder
    return print(numb_dec)


def main():
    try:
        number = int(input('Введите целое число: '))
        mirror(number)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
