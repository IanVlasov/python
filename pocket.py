import random


class Pocket:
    def __init__(self):
        all_numbers = [x for x in range(1, 90)]
        random.shuffle(all_numbers)
        self.pocket = all_numbers
        self.current_keg = None

    def get_next_keg(self):
        self.current_keg = self.pocket[0]
        self.pocket.remove(self.pocket[0])
        print(self)

    def __str__(self):
        return f'Следующий бочонок номер: {self.current_keg:>6}\n' \
               f'Осталось {len(self.pocket):>6}'


if __name__ == '__main__':
    pocket = Pocket()
    print(pocket.pocket)
    pocket.get_next_keg()
    print(pocket.pocket)
    pocket.get_next_keg()