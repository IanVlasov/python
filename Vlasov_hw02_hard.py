# coding: utf-8

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5

i_start = equation.find("=")
i_end = equation.find("x")

k = equation[i_start+1:i_end]
k = float(k.lstrip())

Check = True
try:
    i_start = equation.rindex("+")
except ValueError:
    i_start = equation.rindex("-")  # если уравнение вида kx - b
    Check = False

b = equation[i_start+1:]
b = float(b.lstrip())

y = k * x + b if Check is True else k * x - b
print(y)

# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

import datetime

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date2 = '01.22.1001'
date3 = '1.12.1001'
date4 = '-2.10.3001'


def check_date(date):
    # флаг для определения корректности даты (присваиваем True, если выполнены все условия)
    flag = False
    days_in_month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    date_list = date.split('.', maxsplit=2)

    try:

        day = date_list[0]
        month = date_list[1]
        year = date_list[2]

        if len(day) == 2 and len(month) == 2 and len(year) == 4:
            day = int(day)
            month = int(month)
            year = int(year)
            if (
                1 <= year <= 9999 and
                1 <= day <= days_in_month[month] and
                1 <= month <= 12
            ):

                # Проверка на високосный год
                if month == 2:
                    leap = False
                    if year % 4 == 0 and year >= 1582:
                        if year % 100 != 0:
                            leap = True
                        elif year % 400 == 0:
                            leap = True

                    days_in_feb = 28 if leap is False else 29

                    if day < days_in_feb:
                        flag = True

                else:
                    flag = True

    except IndexError:
        pass

    except ValueError:
        pass

    except KeyError:
        pass

    finally:
        if flag is True:
            print('correct date')
        else:
            print('incorrect date')
        return flag

check_date(date)
check_date(date2)
check_date(date3)
check_date(date4)





# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

import random

N = random.randint(1, 55)

print("Вход: {}".format(N))

floor = 0
block = 1  # переменная для определения, в каком блоке находится комната
sub = 0  # вспомогательная переменная (сравниваем сумму квадратов с номером комнаты)
last_room_in_last_block = 0
flag = True

while flag is True:
    sub += block * block

    if N - sub > 0:
        floor += block
        block += 1
        last_room_in_last_block = sub
    else:
        flag = False

res_num = (N - last_room_in_last_block) % block
res_floor = (N - last_room_in_last_block) // block
floor = floor + res_floor if res_num == 0 else floor + res_floor + 1
left_num = res_num if res_num != 0 else block

print('Выход: {} {}'.format(floor, left_num))
