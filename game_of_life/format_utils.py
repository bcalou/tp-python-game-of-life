"""This file contains the utils to read and write a GOL map in a file.
"""

import game_of_life.const as const
from game_of_life.types import *


class FormatToolbox:
    """Class that manages the file reading and writing.
    """
    def __init__(self):
        self.save_path: str = "saves/"
        self.template_path: str = "saves/templates/"
        self.extension: str = ".gol"

    def read_map(self, name: str) -> MapData:
        """Returns the alive cells from a file.
        """
        alive_cells: AliveCells = []
        x: int = 0
        y: int = 0
        try:
            # Read the file
            path: str = f"{self.save_path}{name}{self.extension}"
            with open(path, "r") as file:
                for y, line in enumerate(file):
                    for x, cell in enumerate(line):
                        if cell == "1":
                            alive_cells.append((x, y))
        except FileNotFoundError:
            return ([], (-1, -1))
        
        return alive_cells, (x + 1, y + 1)


    def write_map(
        self,
        name: str,
        alive_cells: AliveCells,
        size: tuple[int, int]
    ):
        """Write a map in a file.
        """
        # Write the file
        path: str = f"{self.save_path}{name}{self.extension}"
        with open(path, "w") as file:
            for y in range(size[1]):
                for x in range(size[0]):
                    if (x, y) in alive_cells:
                        file.write("1")
                    else:
                        file.write("0")
                file.write("\n")


    def grid_to_alives(self, grid: Grid) -> AliveCells:
        """Convert a grid to a list of alive cells.
        """
        alive_cells: AliveCells = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    alive_cells.append((x, y))
        return alive_cells


    def alives_to_grid(
        self,
        alive_cells: AliveCells,
        size: tuple[int, int]
    ) -> Grid:
        """Convert a list of alive cells to a grid.
        """
        grid: Grid
        grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

        for cell in alive_cells:
            grid[cell[1]][cell[0]] = 1
        return grid
