from typing import List
import pygame

class Grid:
    def __init__(self, grid: List[List[int]]) -> None:
        pygame.init()

        self.grid = grid
        self.WIDTH_GRID = 500
        self.NB_CELLS = 49
        self.WIDTH_CELL = self.WIDTH_GRID // self.NB_CELLS
        self.SCREEN = pygame.display.set_mode((self.WIDTH_GRID, self.WIDTH_GRID))

    def get_grid(self) -> List[List[int]]:
        return self.grid

    def get_width_grid(self) -> int:
        return self.WIDTH_GRID

    def build_grid(self):
        pygame.draw.rect(self.SCREEN, (255, 255, 255), (0, 0, self.WIDTH_GRID, self.WIDTH_GRID))
        for x_pos in range(self.NB_CELLS):
            for y_pos in range(self.NB_CELLS):
                current_cell = self.grid[x_pos][y_pos]
                color = self.get_color(current_cell)
                pygame.draw.rect(self.SCREEN, (color, color, color), (y_pos * self.WIDTH_CELL, x_pos * self.WIDTH_CELL, self.WIDTH_CELL, self.WIDTH_CELL))

        pygame.display.flip()

    def draw_next_state(self):
        new_grid = [[0] * self.NB_CELLS for _ in range(self.NB_CELLS)]
        for x_pos in range(self.NB_CELLS):
            for y_pos in range(self.NB_CELLS):
                current_cell = self.new_state_cell(self.grid[x_pos][y_pos], x_pos, y_pos)
                color = self.get_color(current_cell)
                new_grid[x_pos][y_pos] = current_cell
                pygame.draw.rect(self.SCREEN, (color, color, color),
                                 (y_pos * self.WIDTH_CELL, x_pos * self.WIDTH_CELL, self.WIDTH_CELL, self.WIDTH_CELL))

        self.grid = new_grid
        pygame.display.flip()

    def get_color(self, cell_state: int) -> int:
        return 255 if cell_state == 1 else 0

    def new_state_cell(self, current_cell_state: int, x_pos: int, y_pos: int) -> int:
        arround_cells = self.cells_alive_arrond_current_cell(x_pos, y_pos)
        if (current_cell_state == 0 and arround_cells == 3) or (current_cell_state == 1 and arround_cells in [2, 3]):
            return 1
        return 0

    def cells_alive_arrond_current_cell(self, x_pos: int, y_pos: int) -> int:
        counter = 0
        if x_pos > 0 and y_pos > 0: counter += self.grid[x_pos - 1][y_pos - 1]
        if x_pos > 0: counter += self.grid[x_pos - 1][y_pos]
        if x_pos > 0 and y_pos < self.NB_CELLS - 1: counter += self.grid[x_pos - 1][y_pos + 1]
        if x_pos < self.NB_CELLS - 1 and y_pos > 0: counter += self.grid[x_pos + 1][y_pos - 1]
        if x_pos < self.NB_CELLS - 1: counter += self.grid[x_pos + 1][y_pos]
        if x_pos < self.NB_CELLS - 1 and y_pos < self.NB_CELLS - 1: counter += self.grid[x_pos + 1][y_pos + 1]
        if y_pos > 0: counter += self.grid[x_pos][y_pos - 1]
        if y_pos < self.NB_CELLS - 1: counter += self.grid[x_pos][y_pos + 1]

        return counter
