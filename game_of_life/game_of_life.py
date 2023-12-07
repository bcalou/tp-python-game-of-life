from game_of_life.board import Board


DEAD: int = 0
ALIVE: int = 1


class GameOfLife:
    """
    GameOfLife implements the cellular automaton developped by John Conway

    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    """

    def __init__(self, initial_state: list[list[int]]) -> None:
        """
        Takes the original states of the game as parameter
        """
        self.__board: Board = Board(initial_state)

    def game_rules(self, cell_state: int, neighbour_count: int) -> int:
        """
        Defines the rule of the game of life.

        Returns the cell state for the next iteration

        A children class with different rules 
        must overwrite this function
        """
        # A cell stays/becomes alive if it has 3 neighbours
        if neighbour_count == 3:
            return ALIVE
        # A cell stays alive/dead if it has 2 neighbours
        elif neighbour_count == 2:
            return cell_state
        # With <2 or >3 neighbour, a cell dies
        return DEAD

    def next_state(self) -> None:
        """
        Updates the internal state of the game according to the rules defined
        in method `GameOfLife.game_rules()`
        """
        new_state: list[list[int]] = []
        for y in range(self.get_height()):
            new_row: list[int] = []
            for x in range(self.get_width()):
                neighbour_count: int = self.__board.get_neighbours_count(x, y)
                cell_state: int = self.get_cell(x, y)

                new_row.append(self.game_rules(cell_state, neighbour_count))

            new_state.append(new_row)

        self.__board.set_board(new_state)

    def get_width(self) -> int:
        """
        Returns the width of the board
        """
        return self.__board.get_width()

    def get_height(self) -> int:
        """
        Returns the height of the board
        """
        return self.__board.get_height()

    def get_cell(self, x: int, y: int) -> int:
        """
        Returns the state of a cell at coordinates `x` & `y`

        if the coordinates are invalid, return 0 (DEAD)
        """
        return self.__board.get_cell(x, y)
