from copy import deepcopy
import constants


class Game():
    __current_state: list[list[int]]

    def __init__(self):
        self.__current_state = deepcopy(constants.INITIAL_STATE)

    def get_next_state(self) -> list[list[int]]:
        """Calculate and return the current state of the simulation 
        by killing or creating cells"""

        new_state: list[list[int]] = deepcopy(self.__current_state)

        for line in range(len(self.__current_state)):
            for cell in range(len(self.__current_state[line])):
                neighbors_count: int = self.__count_neighbors(cell, line)

                # A cell is created when surrounded by 3 other cells
                if neighbors_count == 3:
                    new_state[line][cell] = 1
                elif neighbors_count > 3 or neighbors_count <= 1:
                    new_state[line][cell] = 0

        self.__current_state = deepcopy(new_state)
        return new_state


    def __count_neighbors(self, position_x: int, position_y: int) -> int:
        """return how many neihbors a case has"""

        neighbors: int = 0

        x: int = position_x - 1
        y: int = position_y - 1

        for i in range(3):
            for j in range(3):
                if (x + j != position_x or y + i != position_y) \
                    and x + j >= 0 and y + i >= 0 \
                        and x + j < len(self.__current_state[position_y]) \
                            and y + i < len(self.__current_state) \
                                and self.__current_state[y + i][x + j] == 1:
                    neighbors += 1

        return neighbors
