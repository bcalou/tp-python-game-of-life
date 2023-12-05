import pygame
from pygame import Surface, SurfaceType

SQUARE_SIZE: int = 5
SQUARE_COLOR: tuple[int, int, int] = (0, 0, 0)
SQUARE_BORDER_COLOR: tuple[int, int, int] = (100, 100, 100)

SCREEN_SIZE: tuple[int, int] = (1000, 750)


class ScreenManager:

    def __init__(self) -> None:
        self.screen: Surface | SurfaceType = pygame.display.set_mode(
            SCREEN_SIZE)
        self.screen.fill((0, 0, 0))

    def draw_grid(self, grid: list[list[int]]) -> None:
        """
        Draws a grid on the screen.

        :param grid: A 2D list representing the grid.
        """
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    self.draw_void(x, y)
                else:
                    self.draw_square(x, y)
        pygame.display.flip()

    def draw_square(self, x: int, y: int) -> None:
        """
        This method is used for drawing a square on the screen at a
        specified position.

        :param x: The x-coordinate of the square's position.
        :param y: The y-coordinate of the square's position.
        """
        pos_x: int = x * SQUARE_SIZE
        pos_y: int = y * SQUARE_SIZE
        pygame.draw.rect(self.screen, SQUARE_BORDER_COLOR,
                         (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(self.screen, SQUARE_COLOR,
                         (pos_x + 1, pos_y + 1, SQUARE_SIZE - 2,
                          SQUARE_SIZE - 2))

    def draw_void(self, x: int, y: int) -> None:
        """
        Draws a void square on the screen at the specified coordinates.

        :param x: The x-coordinate of the square.
        :param y: The y-coordinate of the square.
        """
        pos_x: int = x * SQUARE_SIZE
        pos_y: int = y * SQUARE_SIZE
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))
