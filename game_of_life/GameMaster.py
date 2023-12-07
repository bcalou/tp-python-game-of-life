from game_of_life.Consts import Enums
from game_of_life.ScreenManager import ScreenManager
from game_of_life.Matrix import MatrixManager


class GameMaster():

    def __init__(self) -> None:
        '''
            Create a new screen and matrix manager to handle
            the game behaviour.
        '''

        self.__enums: Enums = Enums()

        self.__screen_manager: ScreenManager = ScreenManager(
            self.__enums.SCREEN_WIDTH,
            self.__enums.SCREEN_HEIGHT,
            self.__enums.FPS)

        self.__matrix_manager: MatrixManager = MatrixManager(
            self.__enums.MATRIX_WIDTH,
            self.__enums.MATRIX_HEIGHT)

        self.__matrix_manager.replace_matrix(self.__enums.START_MATRIX)

    def run(self) -> None:
        '''
            Loop while the user don't want to close the game
        '''
        done: bool = False

        while not done:

            done = self.__screen_manager.want_quit()

            self.__screen_manager.refresh_view(
                self.__matrix_manager.get_matrix())

            self.__matrix_manager.update_matrix()

    def quit(self) -> None:
        '''
            Just quit the game.
        '''

        self.__screen_manager.quit()
