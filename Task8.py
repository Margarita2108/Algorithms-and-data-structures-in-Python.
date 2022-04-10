# Определить, является ли год, который ввел пользователем, високосным или невисокосным.


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return print('Год высокосный')
    else:
        return print('Год не высокосный')


def main():
    try:
        year = int(input('Введите год: '))
        leap_year(year)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
