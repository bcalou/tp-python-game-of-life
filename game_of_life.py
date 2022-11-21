import pygame
import copy
from game_of_life.params import *
from game_of_life.game import Game


class Display:

    """Class managing the display of the game thanks to the pygame library"""

    def __init__(self, window_size: tuple, current_game: Game):
        self._game = current_game
        self._WINDOW_SIZE: tuple = window_size
        self._WINDOW_NAME: str = "Game of life"
        self._SQUARE_X_SIZE: int = self._WINDOW_SIZE[0] // self._game.get_columns_quantity()
        self._SQUARE_Y_SIZE: int = self._WINDOW_SIZE[1] // self._game.get_lines_quantity()
        self._frequency: int = 4
        self._generation: int = 1
        self._current_state: Matrix = copy.deepcopy(self._game.get_initial_state())
        self._is_playing: bool = True
        self._done: bool = False
        self._init_pygame()
        self._display()

    def _init_pygame(self):

        """Pygame library initialization and setting"""

        pygame.init()
        self._screen: pygame.surface.Surface = (
            pygame.display.set_mode(self._WINDOW_SIZE)
        )
        pygame.display.set_caption(self._WINDOW_NAME)
        self._clock = pygame.time.Clock()
        self._font = pygame.font.SysFont("calibri", 50)

    def _display(self):

        """Method managing user events and content refreshing"""

        # While the game is not over
        while not self._done:

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    self._done = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self._increase_speed()
                    elif event.key == pygame.K_DOWN:
                        self._decrease_speed()
                    """elif event.key == pygame.K_SPACE:
                        self._playpause()"""

            self._display_current_state()
            self._current_state = self._game.get_next_state(self._current_state)
            self._generation += 1
            self._clock.tick(self._frequency)

        pygame.quit()

    def _increase_speed(self):

        """Increasing the pygame's clock frequency (here, the speed of the game)"""

        if self._frequency < 128:
            self._frequency = self._frequency * 2
        print(f'Frequency : {self._frequency} Hz')

    def _decrease_speed(self):

        """Decreasing the pygame's clock frequency (here, the speed of the game)"""

        if self._frequency > 1:
            self._frequency = self._frequency // 2
        print(f'Frequency : {self._frequency} Hz')

    """def _playpause(self):
        # à revoir car mettre la fréquence à 0 n'arrête pas la simulation
        if self._is_playing:
            self._clock.tick(0)
            self._is_playing = False
        else:
            self._clock.tick(self._frequency)
            self._is_playing = True"""

    def _display_current_state(self):

        """Waking through the whole matrix to draw each cell one by one"""
        
        for y in range(self._game.get_lines_quantity()):
            for x in range(self._game.get_columns_quantity()):
                if self._current_state[y][x] == 1:
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255)

                pygame.draw.rect(self._screen, color, (x * self._SQUARE_X_SIZE, y * self._SQUARE_Y_SIZE, self._SQUARE_X_SIZE, self._SQUARE_Y_SIZE))

        self._text = self._font.render(f'{self._generation}', True, (255, 0, 0))
        self._screen.blit(self._text, (0, 0))
        pygame.display.flip()


new_game = Game(INITIAL_STATE)
Display(WINDOW_SIZE, new_game)
