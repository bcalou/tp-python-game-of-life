# import gameStateManager
import pygame

from game_of_life.dictionnary import Coords
from game_of_life.gameStateManager import GameStateManager


class Game:
    screen_size: int = 800
    square_color: (int, int, int) = (0, 0, 0)
    background_color: (int, int, int) = (255, 255, 255)
    tick_number: int = 5

    _y_length: int
    _x_length: int

    _game_state: GameStateManager
    _block_size: int
    _is_game_done: bool

    _screen: pygame.surface.Surface
    _clock: pygame.time.Clock

    def __init__(self, initial_state: list[list[int]]):
        self._y_length = len(initial_state)
        self._x_length = len(initial_state[0])
        self._block_size = self.screen_size // self._y_length
        self._game_state = GameStateManager(initial_state)
        self._is_game_done = False
        pass

    def start_game(self):
        pygame.init()
        self._screen = \
            pygame.display.set_mode((self.screen_size, self.screen_size))
        self._clock = pygame.time.Clock()
        self._loop()

    def _loop(self):
        """Loop the game until user quits"""

        while not self._is_game_done:
            print("Update !")
            self._screen.fill(self.background_color)
            self._update_screen_state()
            pygame.display.flip()

            self._events_check()

            self._clock.tick(self.tick_number)
            self._game_state.go_to_next_state()

        pygame.quit()

    def _update_screen_state(self):
        """Go through the current state, and renders it on the screen"""
        for y_index in range(0, self._y_length):
            for x_index in range(0, self._x_length):

                if self._game_state.get_current_state()[y_index][x_index] == 1:
                    x: int = x_index * self._block_size
                    y: int = y_index * self._block_size
                    self.draw_cell({"x": x, "y": y})

    def draw_cell(self, coords: Coords):
        """Draw a cell on the screen"""
        pygame.draw.rect(self._screen,
                         self.square_color,
                         (
                             coords["x"], coords["y"],
                             self._block_size,
                             self._block_size
                         ))

    def _events_check(self):
        """check if there is any event"""
        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                self._is_game_done = True
