import sys
from card import Card
from pocket import Pocket
from end_of_game_conditions import (
    ComputerWin,
    UncorrectMove,
    PlayerWin,
    Draw
)


class Game:
    def __init__(self):
        print('Приветствую!')
        ans = input('Как тебя зовут?\n')

        self._pocket = Pocket()
        self._comp_card = Card('Компьютер')
        self._players_card = Card(str(ans))
        move_number = 1

        while move_number < 90:
            self.continue_game()
            move_number += 1

    @property
    def pocket(self):
        return self._pocket

    @property
    def comp_card(self):
        return self._comp_card

    @property
    def players_card(self):
        return self._players_card

    @staticmethod
    def check_move_and_win(card, new_keg):
        win_flag = False
        move_flag = card.remove_from_card(new_keg)
        if move_flag:
            win_flag = card.check_empty_card()
        return move_flag, win_flag

    def move(self, ans=None):
        if ans is None:
            comp_flags = self.check_move_and_win(self.comp_card, self.pocket.current_keg)
            if comp_flags[1] is True:
                player_flags = self.check_move_and_win(self.players_card, self.pocket.current_keg)
                if player_flags[1] is True:
                    raise Draw
                raise ComputerWin

        elif ans == 'y':
            player_flags = self.check_move_and_win(self.players_card, self.pocket.current_keg)
            if player_flags[0] is False:
                raise UncorrectMove
            elif player_flags[1] is True:
                raise PlayerWin

        else:
            move_flag = self.players_card.check_negative_answer(self.pocket.current_keg)
            if not move_flag:
                raise UncorrectMove

    def continue_game(self):
            try:
                self.pocket.get_next_keg()
                print(self.players_card)
                print(self.comp_card)
                ans = ''

                while (ans != 'y' and ans != 'n'):
                    ans = input('Зачеркнуть цифру? y/n\n')

                self.move()
                self.move(ans)

            except PlayerWin as exep:
                print(exep)
                sys.exit()

            except ComputerWin as exep:
                print(exep)
                sys.exit()

            except Draw as exep:
                print(exep)
                sys.exit()

            except UncorrectMove as exep:
                print(exep)
                sys.exit()
