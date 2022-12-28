from random import randint
from utils.type import Color
from game_of_life.tile import Tile
from pygame.draw import line as draw_line
from pygame.surface import Surface as pySurface


class Grid:
    def __init__(self, width: int, height: int, tile_size: int, is_custom: bool = False):
        self.cols: int = width
        self.rows: int = height
        self.tile_size: int = tile_size

        self.blank_state = [[Tile(x, y, self.tile_size, 0) for x in range(self.cols)] for y in range(self.rows)]

        if is_custom:
            self.state = self.blank_state
        else:
            self.state = [[Tile(x, y, tile_size, randint(0, 1)) for x in range(width)] for y in range(height)]

    def draw_state(self, screen: pySurface):
        """
            Responsible to draw the current state
            :return:
        """
        for row in self.state:
            for tile in row:
                tile.draw(screen)

        # Draw the grid
        height: int = self.rows * self.tile_size
        width: int = self.cols * self.tile_size
        grey: Color = Color(100, 100, 100)

        for row in range(self.rows + 1):
            # Calculate the y coordinate of each line
            y = row * self.tile_size

            # Draw horizontal line
            draw_line(screen, grey, (0, y), (width, y))

            for col in range(self.cols + 1):  # Same logic for x and vertical lines
                x = col * self.tile_size
                draw_line(screen, grey, (x, 0), (x, height))

    def update_state(self) -> None:
        """
            Responsible to apply rules of the gol and update the state
            :return: nothing
        """

        # At init next_state is a zero matrix
        next_state = self.blank_state

        for x in range(self.cols):
            for y in range(self.rows):

                # Check rules
                if 2 <= self.get_neighbours_number(x, y) <= 3:  # 2 <= n < 3 and n == 3 stay alive
                    next_state[y][x].set_state(1)
                elif 3 < self.get_neighbours_number(x, y):
                    next_state[y][x].set_state(0)

        # Pass the current state to the next
        self.state = next_state

    def get_neighbours_number(self, x: int, y: int) -> int:
        """
            Check the number of neighbours
            :param x: position x of the tile in the map
            :param y: position y of the tile in the map
            :return: neighbours number
        """
        number: int = 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                if 0 <= x + dx < self.cols and 0 <= y + dy < self.rows:
                    number += 1 if self.state[y + dy][x + dx].state == 1 else 0

        return number
