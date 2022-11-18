import copy

from game_of_life.dictionnary import GameState, Coords


class GameStateManager:
    POSITIONS_LIST: list[(int, int)] = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    _y_length: int
    _x_length: int

    def __init__(self, initial_state):
        self._state = initial_state
        self._y_length = len(initial_state)
        self._x_length = len(initial_state[0])

    def get_current_state(self) -> GameState:
        return self._state

    def go_to_next_state(self):
        """ go to the next state of the game matrix"""

        next_state: list[list[int]] = copy.deepcopy(self._state)
        for y in range(0, self._y_length):
            for x in range(0, self._x_length):
                next_state[y][x] = self.get_cell_next_state({"y": y, "x": x})

        self._state = next_state

    def get_cell_next_state(self, coords: Coords) -> int:
        """Get the cell next state 
        by calculating number of neighbors
        and applying rules of the game"""
        number_of_neighbors: int = self.get_number_of_neighbors(coords)
        return self.calculate_cell_next_state(number_of_neighbors, coords)

    def calculate_cell_next_state(self, number_of_neighbors, coords: Coords):
        """Calculate the next state of a cell at given coords"""
        current_cell_state: int = self._state[coords["y"]][coords["x"]]
        if current_cell_state == 1 and 2 <= number_of_neighbors <= 3:
            return 1
        elif current_cell_state == 0 and number_of_neighbors == 3:
            return 1
        return 0

    def get_number_of_neighbors(self, coords: Coords) -> int:
        """Return the number of neighbors of a cell"""
        number_of_neighbors: int = 0

        for (y_offset, x_offset) in self.POSITIONS_LIST:
            y = coords["y"] + y_offset
            x = coords["x"] + x_offset
            number_of_neighbors += self.get_cell_value({"x": x, "y": y})

        return number_of_neighbors

    def get_cell_value(self, coords: Coords) -> int:
        """return cell value from given coords"""
        if (
                0 <= coords["y"] < self._y_length and
                0 <= coords["x"] < self._x_length
        ):
            return self._state[coords["y"]][coords["x"]]
