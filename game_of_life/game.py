import copy

from const import Coordinates, Matrix, DEAD, ALIVE


class GameState:

    def __init__(self, initial_state: Matrix):
        # The state of the game, it is a square matrix
        self._state: Matrix = initial_state
        # The next state of the game
        self._next_state: Matrix = copy.deepcopy(self._state)
        # Size of a line or a column of the matrix
        self._state_size: int = len(self._state)

    def get_state(self) -> Matrix:
        """Returns the actual state"""
        return self._state

    def update_alive_cell_status(self, cell_position: Coordinates):
        """Updates the status (alive/dead) of a cell that is alive, for the
        next game state"""
        # how much alive cells are around our cell
        alive_neighbours: int = self._get_number_of_alive_neighbours(
            cell_position, self._state)

        # Check if the cell must die
        if self._will_die(alive_neighbours):
            # Destroy the cell in the next state
            self._next_state[cell_position[0]][cell_position[1]] = DEAD

    def update_dead_cell_status(self, cell_position: Coordinates):
        """Updates the status (alive/dead) of a cell that is dead, for the
        next game state"""
        # how much alive cells are around our cell
        alive_neighbours: int = self._get_number_of_alive_neighbours(
            cell_position, self._state)

        # Check if the cell will be alive
        if self._will_be_alive(alive_neighbours):
            # Create a cell in the next state
            self._next_state[cell_position[0]][cell_position[1]] = ALIVE

    def update_state(self):
        """Updates the state matrix with the next state of the game"""
        self._state = copy.deepcopy(self._next_state)

    def _will_die(self, alive_neighbours: int) -> bool:
        """Returns true if the cell has not enough or too much neighbours,
        so it must die"""
        return alive_neighbours < 2 or alive_neighbours > 3

    def _will_be_alive(self, alive_neighbours: int) -> bool:
        """Returns true if the cell has exactly 3 neighbours, so it must
         be alive """
        return alive_neighbours == 3

    def _get_neighbours_cells(self, cell_position: Coordinates) -> \
            list[(int, int)]:
        """Returns a list of the 8 neighbours position (line, column) of a cell
            (starting up left corner and going from left to right)
            A neighbour position can be out of the matrix, it is checked after
             with is_neighbour_valid function
            """

        neighbours: list[Coordinates] = [0, 0] * 4

        neighbours[0] = cell_position[0] - 1, cell_position[1] - 1
        neighbours[1] = cell_position[0] - 1, cell_position[1]
        neighbours[2] = cell_position[0] - 1, cell_position[1] + 1

        neighbours[3] = cell_position[0], cell_position[1] - 1
        neighbours[4] = cell_position[0], cell_position[1] + 1

        neighbours[5] = cell_position[0] + 1, cell_position[1] - 1
        neighbours[6] = cell_position[0] + 1, cell_position[1]
        neighbours[7] = cell_position[0] + 1, cell_position[1] + 1

        return neighbours

    def _is_neighbour_valid(self, neighbour_position: Coordinates,
                            max_position: int) -> bool:
        """Returns false if the neighbour is at a forbidden position"""

        if neighbour_position[0] <= -1 or neighbour_position[1] <= -1:
            return False

        if neighbour_position[0] >= max_position or \
                neighbour_position[1] >= max_position:
            return False

        return True

    def _get_number_of_alive_neighbours(self, cell_position: Coordinates,
                                        state: Matrix) -> int:
        """Returns the number of alive cells around a cell"""

        neighbours: list[Coordinates] = self._get_neighbours_cells(
            cell_position)
        alive_neighbours: int = 0

        # Look for the number of 1 in the neighbours of our cell
        for neighbour in neighbours:
            # Check if the neighbour exist
            if self._is_neighbour_valid(neighbour, len(state)):

                if state[neighbour[0]][neighbour[1]] == 1:
                    alive_neighbours += 1

        return alive_neighbours
