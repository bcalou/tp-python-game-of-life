import pygame
from game_of_life import constants
from game_of_life.game_manager import GameState


class View():
    """Manage the screen which displays the game"""

    __screen: pygame.Surface
    __done: bool
    __cells_size: float

    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__init_sizes()

    def __init_sizes(self) -> None:
        """set cells size"""

        self.__cells_size = \
            constants.SCREEN_SIZE[0] / len(constants.INITIAL_STATE)

    def draw_current_state(self, game_state: GameState) -> None:
        """draw the state of the game of life"""

        # Clear the screen
        self.__screen.fill((0, 0, 0))

        x_pivot: float = 0
        y_pivot: float = 0

        # Explore the list of cells to display them
        for line in game_state:
            for cell in line:
                if cell == 1:
                    pygame.draw.rect(self.__screen, (255, 255, 255),
                                     (x_pivot, y_pivot,
                                         self.__cells_size, self.__cells_size))

                x_pivot += self.__cells_size

            x_pivot = 0
            y_pivot += self.__cells_size
