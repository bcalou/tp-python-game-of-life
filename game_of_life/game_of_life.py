import pygame
from pygame import Surface
from game_of_life.board import Board, matrix, row


DEAD: int = 0
ALIVE: int = 1


class GameOfLife:
    """
    GameOfLife implements the cellular automaton developped by John Conway

    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    """

    def __init__(self, initial_state: matrix) -> None:
        """
        Takes the original states of the game as parameter
        """
        self.__board: Board = Board(initial_state)

    def get_cell_next_state(
            self,
            cell_state: int,
            neighbour_count: int
            ) -> int:
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

        # We start from an empty board and fill it cell by cell
        new_state: matrix = []
        for y in range(self.__board.get_height()):
            # Same apply for the rows
            new_row: row = []
            for x in range(self.__board.get_width()):
                neighbour_count: int = self.__board.get_neighbours_count(x, y)
                cell_state: int = self.__board.get_cell(x, y)

                # Compute the next state of the cell and
                # add it to the current row
                new_row.append(
                    self.get_cell_next_state(cell_state, neighbour_count)
                )

            new_state.append(new_row)

        self.__board.set_board(new_state)

    def print_state(self, screen: Surface, pixel_size: int) -> None:
        """Print cell to the screen according to the state"""
        for y in range(self.__board.get_height()):
            for x in range(self.__board.get_width()):
                # Different colors if cell is ALIVE or DEAD
                #   See ALIVE and DEAD definitions
                # ALIVE*220+35 = 255     DEAD*220+35 = 35
                color: int = self.__board.get_cell(x, y)*220 + 35

                # Width & Height are pixel_size - 1
                # It leaves a 1px gap between each cells
                pygame.draw.rect(screen, (color, color, color),
                                 (x*pixel_size, y*pixel_size,
                                 pixel_size-1, pixel_size-1))
