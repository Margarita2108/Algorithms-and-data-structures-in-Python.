# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def multiples():
    counter = [0, 0, 0, 0, 0, 0, 0, 0]
    for numb in range(2, 100):
        for num in range(2, 10):
            if numb % num == 0:
                counter[num-2] += 1
    for num in range(2, 10):
        print(num, ' - ', counter[num-2])


def main():
    multiples()


if __name__ == '__main__':
    main()
