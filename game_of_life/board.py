"""
Board class
"""

import pygame

from game_of_life.types import Coordinates, Screen
from game_of_life.state import State


class Board:
    """Handles the visual rendering of the board"""
    COLOR_ALIVE: tuple[int, int, int] = (255, 255, 255)
    COLOR_DEAD: tuple[int, int, int] = (0, 0, 0)
    SCREEN_SIZE: tuple[int, int] = (1000, 1000)
    FRAMES_PER_SECOND: int = 10

    def __init__(self, initial_state: State):
        self._screen: Screen = pygame.display.set_mode(Board.SCREEN_SIZE)

        self._cell_size: int = self._get_cell_size(initial_state)

    def clear(self):
        """Clear the whole board"""
        self._screen.fill(Board.COLOR_DEAD)

    def draw_cell(self, coordinates: Coordinates):
        """Draw a cell at the given position"""
        pygame.draw.rect(
            self._screen,
            Board.COLOR_ALIVE,
            [
                coordinates[0] * self._cell_size,
                coordinates[1] * self._cell_size,
                self._cell_size,
                self._cell_size
            ]
        )

    def commit(self):
        """Commit the changes to the screen"""
        pygame.display.flip()

    def _get_cell_size(self, initial_state: State) -> int:
        """Compute a safe cell size so that the whole animation can be seen"""

        screen_width, screen_height = self._screen.get_size()

        # Get the ideal width and height for a cell
        ideal_cell_width: int = screen_width // initial_state.get_width()
        ideal_cell_height: int = screen_height // initial_state.get_height()

        # Return the lowest of these values
        return min(ideal_cell_width, ideal_cell_height)
