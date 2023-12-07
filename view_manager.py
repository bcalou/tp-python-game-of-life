import pygame
import constants
from game_of_life_manager import Game


class View():
    __screen: pygame.Surface
    __clock: pygame.time.Clock
    __game_manager: Game
    __done: bool
    __cells_size : float

    def __init__(self, game_of_life_manager):
        self.__screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.__game_manager = game_of_life_manager
        self.__clock = pygame.time.Clock()
        self.__done = False
        self.__init_sizes()
        self.__manage_screen()


    def __init_sizes(self):
        """set cells size"""

        self.__cells_size = constants.SCREEN_SIZE[0] / len(constants.INITIAL_STATE)


    def __manage_screen(self):
        """manage what is drawn on the screen and when it's over"""

        # While the game is not over
        while not self.__done:

            # draw the current state of the game
            self.__draw_current_state()

            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    self.__done = True

            # Redraw the game 30 times per second
            pygame.display.flip()
            self.__clock.tick(30)

        pygame.quit()


    def __draw_current_state(self):
        """draw the state of the game of life"""

        self.__screen.fill((0, 0, 0))
        game_state = self.__game_manager.get_next_state()

        x_position: float = 0
        y_position: float = 0

        for line in game_state:
            for cell in line:
                if cell == 1:
                    pygame.draw.rect(self.__screen, (255, 255, 255),
                                    (x_position, y_position,
                                    self.__cells_size, self.__cells_size))

                x_position += self.__cells_size

            x_position = 0
            y_position += self.__cells_size
