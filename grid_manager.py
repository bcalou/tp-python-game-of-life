import copy

import pygame
from constants import *

grid_type = list[list[int]]


class GridManager:
    def __init__(self, initial_grid: grid_type):
        self.grid = initial_grid
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def set_next_grid(self) -> None:
        """
        Sets the next grid according to the rules of John Conway's Game of Life.

        :return: None
        """
        next_grid = copy.deepcopy(self.grid)

        for row_index, row in enumerate(self.grid):
            for cell_index in range(len(row)):
                next_grid[row_index][cell_index] = self.__get_next_cell_state(row_index, cell_index)

        self.grid = next_grid

    def __get_next_cell_state(self, row_index: int, cell_index: int) -> int:
        """
        Returns the next state of the given cell.

        :param row_index: Height index of the cell
        :param cell_index: Width index of the cell
        :return: The next state of the cell (0 : dead or 1 : alive)
        """
        next_cell_state = self.grid[row_index][cell_index]
        neighbors = self.__get_neighbors(row_index, cell_index)

        if next_cell_state == 1:
            if neighbors < 2 or neighbors > 3:
                next_cell_state = 0
        else:
            if neighbors == 3:
                next_cell_state = 1
        '''
                if neighbors > 0:
                    print(f"({row_index}, {cell_index}) : {next_cell_state} for ({neighbors}) neighbors")
        '''

        return next_cell_state

    def __get_neighbors(self, row_index: int, cell_index: int) -> int:
        """
        Returns the number of neighbors of the given cell.

        :param row_index: Height index of the cell
        :param cell_index: Width index of the cell
        :return:
        """
        neighbors = 0

        for neighbor in NEIGHBORS:
            try:
                if self.grid[row_index + neighbor[0]][cell_index + neighbor[1]] == 1:
                    neighbors += 1
            except IndexError:
                pass

        return neighbors

    def draw_grid(self) -> None:
        """
        Draws the current grid.

        :return: None
        """

        # Fill the screen with black
        self.screen.fill(BLACK_COLOR)

        for row_index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(self.screen, WHITE_COLOR,
                                     (cell_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

    def get_grid(self) -> grid_type:
        """
        Returns the current grid.

        :return: The current grid
        """
        return self.grid

    def set_grid(self, grid: grid_type) -> None:
        """
        Sets the current grid.

        :param grid: The new grid
        :return: None
        """
        self.grid = grid
