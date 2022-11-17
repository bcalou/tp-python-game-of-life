"""This file contains the utils to read and write a GOL map in a file.
"""


def read_map(name: str) -> tuple[list[tuple[int, int]], tuple[int, int]]:
    """Returns the alive cells from a file.
    """
    alive_cells: list[tuple[int, int]] = []
    x: int = 0
    y: int = 0
    try:
        # Read the file
        path: str = f"saves/{name}.gol"
        with open(path, "r") as file:
            for y, line in enumerate(file):
                for x, cell in enumerate(line):
                    if cell == "1":
                        alive_cells.append((x, y))
    except FileNotFoundError:
        return ([], (-1, -1))
    return alive_cells, (x + 1, y + 1)


def write_map(
    name: str,
    alive_cells: list[tuple[int, int]],
    size: tuple[int, int]
) -> bool:
    """Write a map in a file.
    """
    try:
        # Write the file
        path: str = f"saves/{name}.gol"
        with open(path, "w") as file:
            for y in range(size[1]):
                for x in range(size[0]):
                    if (x, y) in alive_cells:
                        file.write("1")
                    else:
                        file.write("0")
                file.write("\n")
    except FileNotFoundError:
        return False
    return True


def grid_to_alives(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Convert a grid to a list of alive cells.
    """
    alive_cells: list[tuple[int, int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]:
                alive_cells.append((x, y))
    return alive_cells


def alives_to_grid(
    alive_cells: list[tuple[int, int]],
    size: tuple[int, int]
) -> list[list[int]]:
    """Convert a list of alive cells to a grid.
    """
    grid: list[list[int]]
    grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    for cell in alive_cells:
        grid[cell[1]][cell[0]] = 1
    return grid
