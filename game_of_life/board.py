import random


def generate_random_line(width: int) -> list[int]:
    """
    Randomly generates a line of size: `width` with ones and zeroes
    """
    return [random.randint(0, 1) for _ in range(width)]


def generate_random_state(width: int, height: int) -> list[list[int]]:
    """
    Randomly generates a board of size: `width`*`height` with ones and zeroes
    """
    return [generate_random_line(width) for _ in range(height)]


class Board:
    """
    Wrapper for a basic 2D Matrix
    """

    __board: list[list[int]]

    def __init__(self, state: list[list[int]]) -> None:
        """
        Takes the original states of the game as parameter
        """

        self.__width: int = len(state[0])
        self.__height: int = len(state)
        self.__board: list[list[int]] = state

    def get_neighbours_count(self, x: int, y: int) -> int:
        """
        Count the number of neighbour of a cell
        """
        count: int = 0

        # Possible neighbours coordinates
        x_coords: list[int] = [x-1, x,  x+1]
        y_coords: list[int] = [y-1, y, y+1]

        for neighbour_x in x_coords:
            for neighbour_y in y_coords:
                if neighbour_x is not x or neighbour_y is not y:
                    # Counts the number of living cells
                    #   See ALIVE & DEAD definitions in game_of_life.py
                    count += self.get_cell(neighbour_x, neighbour_y)

        return count

    def get_width(self):
        """
        Returns the width of the board
        """
        return self.__width

    def get_height(self):
        """
        Returns the height of the board
        """
        return self.__height

    def get_cell(self, x: int, y: int) -> int:
        """
        Returns the state of a cell at coordinates `x` & `y`

        if the coordinates are invalid, return 0 (DEAD)
        """
        if x >= 0 and x < self.__width and \
           y >= 0 and y < self.__height:
            return self.__board[y][x]
        return 0

    def set_board(self, new_state: list[list[int]]):
        """
        Overwrite the previous board with a new one

        !!! `new_state` must be the same size as the previous board !!!
        """
        self.__board = new_state
