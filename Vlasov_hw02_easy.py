# coding: utf-8

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list = ["яблоко", "банан", "киви", "арбуз"]

for count, item in enumerate(list, 1):
    print("{}. {:>10}".format(count, item))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

print('=' * 50)

list1 = []
list2 = []
i = 0

while i != 10:
    list1.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    i += 1

print(list1)
print(list2)

intersec = set.intersection(set(list1), list2)

print(intersec)

for item in intersec:
    while list1.count(item) != 0:
        list1.remove(item)

print(list1)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

print('=' * 50)

list1 = []
i = 0

while i != 10:
    list1.append(random.randint(-100, 100))
    i += 1

print(list1)

i = 0
while i < len(list1):
    item = list1[i]
    list1[i] = item / 4 if item % 2 == 0 else item * 2
    i += 1

print(list1)