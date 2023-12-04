from pygame import Surface
import pygame

from game_of_life import const


class Renderer():
    """Represents a renderer used to draw cells on a window"""
    screen: Surface

    def __init__(self, screen: Surface) -> None:
        self.screen = screen

    def draw_game(self, state: list[list[int]]) -> None:
        """Draws the game screen given the current state"""
        self.screen.fill(const.BLACK)

        for row_index, cell_row in enumerate(state):
            for column_index, cell in enumerate(cell_row):
                if cell == 1:
                    cell_rect: tuple = (
                        column_index * const.CELL_SIZE,
                        row_index * const.CELL_SIZE,
                        const.CELL_SIZE,
                        const.CELL_SIZE
                    )

                    pygame.draw.rect(self.screen, const.WHITE, cell_rect)

        pygame.display.flip()
