from game_of_life import const
from game_of_life.game import Game


def main():
    game: Game = Game(const.INITIAL_STATE)
    game.start()


main()
