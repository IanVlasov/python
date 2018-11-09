# В классе карточки будем хранить 15 случайных чисел (или прочерк)
# в формате матрицы. Работа с матрицей будет организована через модуль numpy
#
# Номер колонки определяется по разряду десятков (в официальных правилах), то есть
# Чисел из одной десятки не может быть больше 3 в одной карточке
# Строки заполняем по очереди

import random as rand
from functools import reduce


class Card:
    def __init__(self, owner):
        self._owner = owner
        self._card = self.fill_card()

    @property
    def owner(self):
        return self._owner

    @property
    def card(self):
        return self._card

    def __str__(self):
        first_line = f"\n{' ' + self._owner + ' ':-^27}\n"
        last_line = f"\n{'':-^27}\n"
        card = [[0 for _ in range(9)] for _ in range(3)]
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                card[i][j] = f"{self.card[i][j]:>3}" if self.card[i][j] != 0 else ' - '
            card[i] = ''.join(card[i])
        card = "\n".join(card)
        final_repr = first_line + card + last_line
        return final_repr

    def remove_from_card(self, number):
        for line in self.card:
            if number in line:
                idx = line.index(number)
                line[idx] = 0
                return True
        return False

    def check_negative_answer(self, number):
        if number in reduce(lambda a, b: a + b, self.card):
            return False
        return True

    def check_empty_card(self):
        return all(item == 0 for item in reduce(lambda a, b: a + b, self.card))

    @staticmethod
    def fill_card():
        card = [[0 for _ in range(9)] for _ in range(3)]

        for i, line in enumerate(card):
            filled_columns = rand.sample(range(0, 9), 5)
            for j in filled_columns:
                list_to_check = reduce(lambda a, b: a + b, card)
                if j != 8:
                    low_x = 10 * j
                    high_x = low_x + 9
                    while card[i][j] == 0:
                        to_add = rand.randint(low_x, high_x)
                        card[i][j] = to_add if to_add not in list_to_check else 0

                else:
                    while card[i][j] == 0:
                        to_add = rand.randint(80, 90)
                        card[i][j] = to_add if to_add not in list_to_check else 0

        return card


if __name__ == '__main__':
    new = Card('aa')
    print(new)
    new.remove_from_card(8)
    new.check_empty_card()
    print(new.check_empty_card())
