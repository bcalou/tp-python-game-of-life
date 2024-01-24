"""
State class
"""

from typing import Callable

from game_of_life.types import Coordinates, CellState, CellsMatrix


class State:
    """Represents the state of a game of life at a specific moment"""
    DEAD: CellState = 0
    ALIVE: CellState = 1

    # The relative positions of the 8 potential neighbours for a cell
    NEIGHBOURHOOD_COORDINATES: list[Coordinates] = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    ]

    def __init__(self, cells: CellsMatrix):
        self.__cells: CellsMatrix = cells
        self.__height: int = len(cells)
        self.__width: int = len(cells[0])

    def get_height(self) -> int:
        """Get the height of the matrix"""

        return self.__height

    def get_width(self) -> int:
        """Get the width of the matrix"""

        return self.__width

    def for_each_cell(self, function: Callable) -> None:
        """Execute the given function for each cell, passing the coordinates"""
        for cell_x in range(self.__width):
            for cell_y in range(self.__height):
                function((cell_x, cell_y))

    def for_each_cell_alive(self, function: Callable) -> None:
        """Execute the given function for each cell which is alive"""
        self.for_each_cell(
            lambda coordinates: (
                function(coordinates) if self.is_alive(coordinates) else None
            )
        )

    def is_alive(self, coordinates: tuple[int, int]) -> bool:
        """Check that the cell at the given coordinates exists and is alive"""

        # Test that the cell is inside the matrix's bounds and alive
        return (
            self.__cell_exists(coordinates)
            and self.get_cell_state(coordinates) == self.ALIVE
        )

    def get_cell_state(self, coordinates: Coordinates) -> CellState:
        """Get the state of the cell for at the given coordinates

        [1] and [0] are inverted because the first level of the array is the
        rows, which correspond to the the y coordinate
        """

        if not self.__cell_exists(coordinates):
            return self.DEAD

        return self.__cells[coordinates[1]][coordinates[0]]

    def set_cell_state(
        self,
        coordinates: Coordinates,
        cell_state: CellState
    ) -> None:
        """Set the state of the cell for at the given coordinates

        [1] and [0] are inverted because the first level of the array is the
        rows, which correspond to the the y coordinate
        """
        self.__cells[coordinates[1]][coordinates[0]] = cell_state

    def get_neighbours_count(self, coordinates: Coordinates) -> int:
        """Get the number of cells alive around the given one"""

        return sum(
            self.get_cell_state((coordinates[0] + x, coordinates[1] + y))
            for x, y in self.NEIGHBOURHOOD_COORDINATES
        )

    def get_new_empty_state(self) -> 'State':
        """Get a new state of the same size, filled with dead cells"""

        empty_state = [
            ([self.DEAD] * self.__width) for _ in range(self.__height)
        ]

        return State(empty_state)

    def __cell_exists(self, coordinates: Coordinates) -> bool:
        """Returns wether the given cell coordinates exists"""

        return (
            0 <= coordinates[0] < self.__width
            and 0 <= coordinates[1] < self.__height
        )
