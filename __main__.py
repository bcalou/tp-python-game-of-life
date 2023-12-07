from game_of_life.GameMaster import GameMaster


def main():

    game: GameMaster = GameMaster()

    game.run()

    done = False

    game.quit()


main()
