from game_of_life.Consts import START_MATRIX, SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from game_of_life.ScreenManager import ScreenManager
from game_of_life.Matrix import MatrixManager


class GameMaster():

    def __init__(self) -> None:
        '''
            Create a new screen and matrix manager to handle
            the game behaviour.
        '''

        self.__screen_manager: ScreenManager = ScreenManager(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            FPS)

        self.__matrix_manager: MatrixManager = MatrixManager(START_MATRIX)

    def run(self) -> None:
        '''
            Loop while the user don't want to close the game
        '''
        done: bool = False

        while not done:

            done = self.__screen_manager.wants_to_quit()

            self.__screen_manager.refresh_view(
                self.__matrix_manager.get_matrix())

            self.__matrix_manager.update_matrix()

    def quit(self) -> None:
        '''
            Just quit the game.
        '''

        self.__screen_manager.quit()
