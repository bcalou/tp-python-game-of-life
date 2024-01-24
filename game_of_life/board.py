import pygame

from game_of_life.types import Coordinates
from game_of_life.state import State

Screen = pygame.surface.Surface


class Board:
    """Handles the visual rendering of the board"""
    COLOR_ALIVE: tuple[int, int, int] = (255, 255, 255)
    COLOR_DEAD: tuple[int, int, int] = (0, 0, 0)
    SCREEN_SIZE: tuple[int, int] = (1000, 1000)

    def __init__(self, initial_state: State):
        self.__screen: Screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # Get the ideal width and height for a cell
        screen_width, screen_height = self.__screen.get_size()
        ideal_cell_width = screen_width // initial_state.get_width()
        ideal_cell_height = screen_height // initial_state.get_height()

        # Keep the lowest of these values as the final cell size
        self.__cell_size = min(ideal_cell_width, ideal_cell_height)

    def clear(self):
        """Clear the whole board"""
        self.__screen.fill(self.COLOR_DEAD)

    def draw_cell(self, coordinates: Coordinates):
        """Draw a cell at the given position"""
        pygame.draw.rect(
            self.__screen,
            self.COLOR_ALIVE,
            [
                coordinates[0] * self.__cell_size,
                coordinates[1] * self.__cell_size,
                self.__cell_size,
                self.__cell_size
            ]
        )

    def commit(self):
        """Commit the changes to the screen"""
        pygame.display.flip()
