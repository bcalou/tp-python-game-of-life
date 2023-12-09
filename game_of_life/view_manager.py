import pygame
from game_of_life import constants
from game_of_life.game_manager import Game


class View():
    """Manage the screen which displays the game"""

    __screen: pygame.Surface
    __clock: pygame.time.Clock
    __game_manager: Game
    __done: bool
    __cells_size: float

    def __init__(self, game_of_life_manager: Game) -> None:
        self.__screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__game_manager = game_of_life_manager
        self.__clock = pygame.time.Clock()
        self.__done = False
        self.__init_sizes()
        self.__manage_clock()

    def __init_sizes(self) -> None:
        """set cells size"""

        self.__cells_size = \
            constants.SCREEN_SIZE[0] / len(constants.INITIAL_STATE)

    def __manage_clock(self) -> None:
        """manage when to draw on screen"""

        # While the game is not over
        while not self.__done:

            # draw the current state of the game
            self.__draw_current_state()

            self.__check_end()

            # Redraw the game 30 times per second
            pygame.display.flip()
            self.__clock.tick(30)

        pygame.quit()

    def __draw_current_state(self) -> None:
        """draw the state of the game of life"""

        # Clear the screen
        self.__screen.fill((0, 0, 0))
        game_state = self.__game_manager.get_next_state()

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

    def __check_end(self) -> None:
        """check if the user presses the close button"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__done = True
