# coding: utf-8

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math


def fibonacci(n, m):

    def fn(n):
        if n != 0:
            fi = (1 + math.sqrt(5)) / 2
            result_in = int(((fi ** n - ((-fi) ** (-n))) / (fi - ((-fi) ** (-1)))))
            return result_in
        result_in = 1
        return result_in

    if type(n) == int and type(m) == int and 0 <= n < m:
        result = []
        counter = n

        while counter != m + 1:
            result.append(fn(counter))
            counter += 1
        return result
    else:
        print("неверные аргументы!")


print(fibonacci(1, 8))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    left = 0
    right = len(origin_list) - 1
    while left <= right:
        for i in range(left, right, +1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        right -= 1

        for i in range(right, left, -1):
            if origin_list[i] < origin_list[i - 1]:
                origin_list[i], origin_list[i - 1] = origin_list[i - 1], origin_list[i]
        left += 1

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def custom_filter(func, iterator):

    if hasattr(func, '__call__'):
        result = [item for item in iterator if func(item)]
        return result
    elif isinstance(func, None):
        result = [item for item in iterator if item]
        return result

    print("введите корректные данные")


def test(x):
    flag = True if x < 10 else False
    return flag


x = [2, 15, 18, 7, -30]
print(custom_filter(test, x))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a, b, c, d):
    flag = False

    if [isinstance(a, tuple) and
            isinstance(b, tuple) and
            isinstance(c, tuple) and
            isinstance(d, tuple) and
            len(a) == len(b) == len(c) == len(d) == 2]:

        all_points = [a, b, c, d]

        for point in all_points:
            if not all([isinstance(item, int) for item in point]):
                return flag

        all_points = sort_to_max(all_points)
        first_pair = (all_points[0][0] - all_points[1][0], all_points[0][1] - all_points[1][1])
        second_pair = (all_points[2][0] - all_points[3][0], all_points[2][1] - all_points[3][1])

        if first_pair == second_pair:
            flag = True
            return flag

    return flag


a = (4, 3)
b = (1, 1)
c = (3, 0)
d = (6, 2)

print(is_parallelogram(a, b, c, d))
