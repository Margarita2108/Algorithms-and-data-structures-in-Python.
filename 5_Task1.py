# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections


def profit_enterprise(n):
    enterprise = collections.defaultdict()
    profit_all = 0
    for i in range(n):
        name_enterprise = input(f'\nВведите название {i + 1}-го предприятия: ')
        profit_quarter = [float(i) for i in input(f'Введите прибыль {i + 1}-го предприяния за каждый квартал через пробел: ').split()]
        if len(profit_quarter) != 4:
            profit_quarter = [float(i) for i in input(f'Неверный ввод. должно быть 4 числа \nВведите прибыль {i + 1}-го предприяния за каждый квартал через пробел: ').split()]
        enterprise[name_enterprise] = sum(profit_quarter)
        profit_all = profit_all + sum(profit_quarter)

    profit_midl = profit_all / n
    big_profit = collections.deque()
    smol_profit = collections.deque()
    for i, item in enterprise.items():
        if item >= profit_midl:
            big_profit.append(i)
        else:
            smol_profit.append(i)

    print(f'Средняя прибыль предприятий составила: {profit_midl}')
    print(f'Хорошая у {len(big_profit)} предприятий:')
    for name in big_profit:
        print(name)
    print(f'Остальные {len(smol_profit)}:')
    for name in smol_profit:
        print(name)


def main():
    try:
        n = int(input('Введите количество предприятий: '))
        profit_enterprise(n)
    except ValueError:
        print('Неверный ввод')
        profit_enterprise(n)


if __name__ == '__main__':
    main()
