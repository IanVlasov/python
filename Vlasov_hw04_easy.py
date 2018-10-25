# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

list_rand = [random.randint(-10, 10) for _ in range(15)]
print(list_rand)

new_list = [itm * itm for itm in list_rand]
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["Бананы", "Яблоки", "Персики", "Груши", "Ананасы"]
fruits2 = ["Яблоки", "Абрикосы", "Сливы", "Ананасы", "Персики"]

fruits_result = [itm for itm in fruits1 if itm in fruits2]

print(fruits_result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# используем list_rand из первого задания

list_multiple3 = [itm for itm in list_rand if itm % 3 == 0]
list_pos = [itm for itm in list_rand if itm > 0]
list_not_multiple4 = [itm for itm in list_rand if not itm % 4 == 0]

print(list_multiple3)
print(list_pos)
print(list_not_multiple4)
