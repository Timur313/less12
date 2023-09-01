from classes.PlayerCardClass import PlayerCard
from classes.KegsClass import Kegs
from classes.PlayersClass import Player
import sys


if __name__ == '__main__':

    kegs = Kegs()

    player1 = Player()
    player1.name = "Игрок 1 (Ваша карточка)"
    player1.ptype = "man"
    player1.card = PlayerCard(kegs.base_num)
    player1.card.create_card()

    player2 = Player()
    player2.name = "Игрок 2"
    player2.ptype = "comp"
    player2.card = PlayerCard(kegs.base_num)
    player2.card.create_card()

    go_exit = False

    while len(kegs.remm_num) > 0:
        kegs.get_random_num()
        kegs.print_num()

        print(f"Карточка игрока: {player1.name}")
        player1.card.print_card()

        print(f"Карточка игрока: {player2.name}")
        player2.card.print_card()

        player1.action_remove(kegs.this_val)
        player2.action_remove(kegs.this_val)

        print("\n\n")

        if player1.status and player2.status:
            go_exit = True
            print("!!! Победила дружба !!!")
        elif player1.status:
            go_exit = True
            print(f"!!! Победил игрок {player1.name} !!!")
        elif player2.status:
            go_exit = True
            print(f"!!! Победил игрок {player2.name} !!!")

        if go_exit:
            sys.exit()

