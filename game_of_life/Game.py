from game_of_life.params import *


class Game:

    """Class managing lives and deaths of the cells. Game of life's god"""

    def __init__(self, initial_state: Matrix):
        self._initial_state: Matrix = initial_state
        self._rows_quantity: int = len(self._initial_state)
        self._columns_quantity: int = len(self._initial_state[0])

    def get_initial_state(self) -> Matrix:
        return self._initial_state

    def get_rows_quantity(self) -> int:
        return self._rows_quantity

    def get_columns_quantity(self) -> int:
        return self._columns_quantity

    def get_next_state(self, current_state: Matrix) -> Matrix:

        """Creating matrix of the next generation's state"""

        self._next_state: Matrix = (
            self._create_empty_matrix(self._rows_quantity, self._columns_quantity)
        )

        # Walking through the whole matrix and checking each cell's state in
        # the next generation one by one
        for row in range(self._rows_quantity):
            for column in range(self._columns_quantity):
                self._next_state[row][column] = (
                    self._will_the_cell_live(current_state, column, row)
                )

        return self._next_state

    def _create_empty_matrix(self, rows_quantity: int, columns_quantity: int) -> Matrix:

        """Creating an empty matrix to be filled by the above method"""

        self._empty_matrix: Matrix = []

        for row in range(rows_quantity):
            self._empty_matrix.append([])
            for column in range(columns_quantity):
                self._empty_matrix[row].append(0)

        return self._empty_matrix

    def _will_the_cell_live(self, current_state: Matrix, cell_X_coord: int, cell_Y_coord: int) -> bool:

        """
        The reel master here.
        Method computing whether a cell will live in the next generation.
        """

        current_state_of_cell: int = current_state[cell_Y_coord][cell_X_coord]
        living_cells_around: int = 0

        # Walking through the surrounding cells (row above, current row and row
        # below with previous column, current column and next column)
        for surrounding_cell_Y_coord in range(cell_Y_coord - 1, cell_Y_coord + 2):
            for surrounding_cell_X_coord in range(cell_X_coord - 1, cell_X_coord + 2):

                # Checking if we are on a side of the matrix
                if (
                    0 <= surrounding_cell_X_coord <= (self._columns_quantity - 1) and
                    0 <= surrounding_cell_Y_coord <= (self._rows_quantity - 1)
                ):
                    # If not, taking into account the surrounding cell
                    living_cells_around += current_state[surrounding_cell_Y_coord][surrounding_cell_X_coord]

        # Excluding the cell to check because it has been taken into account by
        # the above loop
        living_cells_around -= current_state[cell_Y_coord][cell_X_coord]

        # Applying the rules of the game
        if (
            (current_state_of_cell == 0 and living_cells_around == 3) or
            (current_state_of_cell == 1 and 2 <= living_cells_around <= 3)
        ):
            return True
        else:
            return False
