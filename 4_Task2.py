# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


import timeit
import math


def prime_numbers_1(n): # O(N^3)
    if n == 1:                              # O(1)
        print('Простое число под № 1 - 2')  # O(1)
    else:
        prime_numbers = [_ for _ in range(3, int(math.log(n)*2*n))]     # O(N)
        for index in range(len(prime_numbers)):                         # O(N)
            for number in prime_numbers[index + 1:]:                    # O(N)
                if number % prime_numbers[index] == 0:                  # O(1)
                    prime_numbers.remove(number)                        # O(N)
        print('Простое число под № ', n, '- ', prime_numbers[(n - 1)])  # O(1)


def prime_numbers_2(n):     # O(N^2)
    prime_numbers = [2]                     # O(1)
    if n == 1:                              # O(1)
        print('Простое число под № 1 - 2')  # O(1)
    else:
        counter = 1                         # O(1)
        number = 1                          # O(1)
        while counter < n:                  # O(N)
            number += 1
            a = []
            for i in prime_numbers:         # O(N)
                if number % i != 0:
                    a.append(0)             # O(1)
                else:
                    a.append(1)             # O(1)
            if sum(a) == 0:
                prime_numbers.append(number)    # O(1)
                counter += 1                    # O(1)
        print('Простое число под № ', n, '- ', prime_numbers[-1]) # O(1)


def main():
    try:
        n = int(input('Введите номер простого числа: '))
        start_time = timeit.default_timer()
        prime_numbers_1(n)
        print(timeit.default_timer() - start_time)
        start_time = timeit.default_timer()
        prime_numbers_2(n)
        print(timeit.default_timer() - start_time)
    except ValueError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()


# 1 - Используя алгоритм «Решето Эратосфена» O(N^3)
# 2 - Без использования «Решета Эратосфена»  O(N^2)

# оба варианта очень долго отрабатывают при больших колличествах данных
# но так как второй вариант все таки в степени 2 он отрабатывает быстрее
# время ощутимо меняется после  1000-ного простого числа

#  Значений: 1
# 1 -   2.9800052288919687e-05
# 2 -   1.0699965059757233e-05

#  Значений: 5
# 1 -   6.890000076964498e-05
# 2 -   3.519997699186206e-05

#  Значений: 10
# 1 -   0.00010579999070614576
# 2 -   6.859999848529696e-05

#  Значений: 100
# 1 -   0.004769899998791516
# 2 -   0.003802000021096319

#  Значений: 1000
# 1 -   0.5545778999803588
# 2 -   0.5298761000158265

#  Значений: 5000
# 1 -   17.58109249995323
# 2 -   14.840119700005744

#  Значений: 10000
# 1 -   108.58235159999458
# 2 -   67.72288610000396

#  Значений: 20000
# 1 -   560.8896280000336
# 2 -   263.82204969995655
