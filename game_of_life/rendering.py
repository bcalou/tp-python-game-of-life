from pygame import Surface
import pygame

from game_of_life import const, array2d


class Renderer():
    """Represents a renderer used to draw cells on a window"""
    screen: Surface

    def __init__(self, screen: Surface) -> None:
        self.screen = screen

    def draw_cell(self, cell_row: int, cell_column: int) -> None:
        """Draws a single cell on the grid"""
        cell_rect: tuple = (
                        cell_row * const.CELL_SIZE,
                        cell_column * const.CELL_SIZE,
                        const.CELL_SIZE,
                        const.CELL_SIZE
                    )

        pygame.draw.rect(self.screen, const.WHITE, cell_rect)

    def clear(self) -> None:
        """Clears the game canvas"""
        self.screen.fill(const.BLACK)

    def update(self) -> None:
        """Displays all changes made on the canvas"""
        pygame.display.flip()
