# coding: utf-8

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    last_num = int(number * (10 ** (ndigits + 1))) % 10

    if last_num >= 5:
        result = "%.{}f".format(ndigits) % (int(number * (10 ** (ndigits)) + 1) / (10 ** (ndigits)))
        return result

    result = "%.{}f".format(ndigits) % (int(number * (10 ** (ndigits))) / (10 ** (ndigits)))
    return result


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    Flag = "Это не номер билета -_-"

    if type(ticket_number) == int and len(str(ticket_number)) == 6:

        first_block = str(ticket_number // 1000)
        second_block = str(ticket_number % 1000)

        result1 = 0
        result2 = 0

        for char in first_block:
            result1 += int(char)

        for char in second_block:
            result2 += int(char)

        if result1 == result2:
            Flag = "Съешьте его скорее, это же счастливый билет!!!"
        else:
            Flag = "Несчастливый =("

    return Flag

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))