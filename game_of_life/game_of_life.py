import random


DEAD: int = 0
ALIVE: int = 1


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


class GameOfLife:
    """
    GameOfLife implements the cellular automaton developped by John Conway

    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    """

    def __init__(self, initial_state: list[list[int]]) -> None:
        """
        Takes the original states of the game as parameter
        """
        self.__width: int = len(initial_state[0])
        self.__height: int = len(initial_state)
        self.__state: list[list[int]] = initial_state

    def next_state(self) -> None:
        """
        Updates the internal state of the game according to Conway's
        original rules of Game of life
        """
        next_state: list[list[int]] = []
        for y, row in enumerate(self.__state):
            new_row: list[int] = []
            for x in range(len(row)):
                neighbour_count: int = self.get_neighbours_count(x, y)
                
                # A cell stays/becomes alive if it has 3 neighbours
                if neighbour_count == 3:
                    new_row.append(ALIVE)
                # A cell stays alive/dead if it has 2 neighbours
                elif neighbour_count == 2:
                    new_row.append(self.__state[y][x])
                # With <2 or >3 neighbour, a cell dies
                else:
                    new_row.append(DEAD)
            next_state.append(new_row)

        self.__state = next_state

    def get_neighbours_count(self, x: int, y: int) -> int:
        """
        Count the number of neighbour of a cell
        """
        count: int = 0

        x_coords: list[int] = [x-1, x,  x+1]
        y_coords: list[int] = [y-1, y, y+1]

        for neighbour_x in x_coords:
            for neighbour_y in y_coords:
                if neighbour_x is not x or neighbour_y is not y:
                    count += self.get_cell(neighbour_x, neighbour_y)

        return count

    def get_cell(self, x: int, y: int) -> int:
        """
        Returns the state of a cell at coordinates `x` & `y`

        if the coordinates are invalid, return 0 (DEAD)
        """
        if x >= 0 and x < self.get_width() and \
           y >= 0 and y < self.get_height():
            return self.__state[y][x]
        return 0

    def get_width(self) -> int:
        """
        Returns the width of the board
        """
        return self.__width

    def get_height(self) -> int:
        """
        Returns the height of the board
        """
        return self.__height
