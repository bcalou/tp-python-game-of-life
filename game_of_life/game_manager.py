from game_of_life import constants


class Game():
    """Manage the simulation of the game of life"""

    __current_state: list[list[int]]
    __grid_size_x: int
    __grid_size_y: int

    def __init__(self) -> None:
        self.__current_state = constants.INITIAL_STATE
        self.__grid_size_x = len(constants.INITIAL_STATE[0])
        self.__grid_size_y = len(constants.INITIAL_STATE)

    def get_next_state(self) -> list[list[int]]:
        """Calculate and return the current state of the simulation
        by killing or creating cells"""

        new_state: list[list[int]] = []

        for line in range(self.__grid_size_y):
            new_line: list[int] = []

            for cell in range(self.__grid_size_x):
                neighbors_count: int = self.__count_neighbors(cell, line)

                # A cell is created when surrounded by 3 other cells
                if neighbors_count == 3:
                    new_line.append(1)

                # And dies when too much or not enough cells are around
                elif neighbors_count > 3 or neighbors_count <= 1:
                    new_line.append(0)

                # Otherwise the cell keeps living or not existing
                else:
                    new_line.append(self.__current_state[line][cell])

            new_state.append(new_line)

        self.__current_state = new_state

        return self.__current_state

    def __count_neighbors(self, position_x: int, position_y: int) -> int:
        """return how many neighbors a cell has"""

        neighbors: int = 0

        x: int = position_x - 1
        y: int = position_y - 1

        for modif_y in range(3):
            new_y: int = y + modif_y
            for modif_x in range(3):
                new_x = x + modif_x
                # We do not count the cell itself nor anything outside the grid
                if (new_x != position_x or new_y != position_y) \
                    and self.__is_cell_on_the_grid(new_x, new_y) \
                        and self.__current_state[new_y][new_x] == 1:
                    neighbors += 1

        return neighbors

    def __is_cell_on_the_grid(self, x, y) -> bool:
        """Test if a given cell exists on the grid or not,
        meaning coordinates should be between 0,0 and the size of the grid"""

        return 0 <= x < self.__grid_size_x and y < self.__grid_size_y
