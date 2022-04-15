# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def ascii_tabl(column):
    counter = 0
    for numb in list(range(32, 128)):
        counter += 1
        if counter % column == 0:
            print(f"{numb:<3} - ", chr(numb), '     ')
        else:
            print(f"{numb:<3} - ", chr(numb), '     ', end='')


def main():
    try:
        ascii_tabl(10)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
