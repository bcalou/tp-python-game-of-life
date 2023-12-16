from game_of_life.Display import Display


class Main:

    __window: Display

    def __init__(self):
        """We just create display of game"""
        self.__window = Display()


Main()
