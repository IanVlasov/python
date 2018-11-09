class UncorrectMove(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Неверный ход! Вы проиграли!'


class ComputerWin(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'К сожалению, компьютер победил\n' \
               'Повезет в следующий раз!'


class PlayerWin(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return 'Поздравляем! Вы победили!'


class Draw(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Ого! Ничья! Редкий случай!'


if __name__ == '__main__':
    try:
        raise PlayerWin
    except PlayerWin as ex:
        print(ex)