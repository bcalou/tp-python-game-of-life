from game_of_life.constants import NEIGHBORS, SCREEN_SQUARE_SIZE, GRID_SIZE, \
    initial_state, first_square_pos, matrix2


class GridManager:

    def __init__(self) -> None:
        self.__grid: matrix2 = [
            [0 for _ in range(SCREEN_SQUARE_SIZE[0])]
            for _ in range(SCREEN_SQUARE_SIZE[1])
        ]

        self.initialize_grid()

    def initialize_grid(self) -> None:
        """
        Initializes the grid with the initial state defined in constants.
        The initial state is centered in the grid.
        """
        for init_y in range(len(initial_state)):
            for init_x in range(len(initial_state[init_y])):
                # add the first square position to the initial to center it
                x = init_x + first_square_pos[0]
                y = init_y + first_square_pos[1]
                self.__grid[y][x] = initial_state[init_y][init_x]

    def update_grid(self) -> None:
        """
        Updates the grid based on the current state of the cells.
        """
        temp_grid: matrix2 = [[0 for _ in range(GRID_SIZE[0])] for
                              _ in range(GRID_SIZE[1])]

        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[y])):
                temp_grid[y][x] = self.get_next_state(x, y)

        self.__grid = temp_grid

    def get_next_state(self, x: int, y: int) -> int:
        """
        Calculate and return the next state of a cell in the grid.

        :param x: The x-coordinate of the cell.
        :param y: The y-coordinate of the cell.
        :return: The next state of the cell (0 or 1).
        """
        neighbors: int = self.count_neighbors(x, y)
        if neighbors == 3:
            return 1

        if neighbors < 2 or neighbors > 3:
            return 0

        return self.__grid[y][x]

    def count_neighbors(self, x: int, y: int, ) -> int:
        """
        :param x: x-coordinate of the cell
        :param y: y-coordinate of the cell
        :return: Number of neighbors around the given cell
        """
        count: int = 0
        for neighbor in NEIGHBORS:
            if 0 <= x + neighbor[0] < GRID_SIZE[0] and \
                    0 <= y + neighbor[1] < GRID_SIZE[1]:
                count += self.__grid[y + neighbor[1]][x + neighbor[0]]
        return count

    def get_grid(self):
        """
        :return: The grid.
        """
        return self.__grid
