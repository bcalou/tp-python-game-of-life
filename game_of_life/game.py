import sys

PROJECT_PATH = r"D:\DOCUMENTS\Cours ENJMIN\2022-09_Algorithmique et programmation\tp-python-game-of-life\game_of_life"

if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from params import *


class Game:
    def __init__(self, initial_state: Matrix):
        self._INITIAL_STATE: Matrix = initial_state
        self._LINES: int = len(self._INITIAL_STATE)
        self._COLUMNS: int = len(self._INITIAL_STATE[0])
    
    def get_initial_state(self) -> Matrix:
        return self._INITIAL_STATE
    
    def get_lines_quantity(self) -> int:
        return self._LINES
    
    def get_columns_quantity(self) -> int:
        return self._COLUMNS
    
    def get_next_state(self, current_state: Matrix) -> Matrix:
        # print("Getting next_state")
        self._next_state: Matrix = self._create_empty_matrix(self._LINES, self._COLUMNS)

        for y in range(self._LINES):
                for x in range(self._COLUMNS):
                    # print(f'Checking cell [{x}][{y}]')
                    if self._will_the_cell_live(current_state, current_state[y][x], x, y):
                        self._next_state[y][x] = 1
                    else:
                        self._next_state[y][x] = 0
        
        return self._next_state
    
    def _create_empty_matrix(self, lines: int, columns: int) -> Matrix:
        self._empty_matrix: Matrix = []

        for y in range(lines):
            self._empty_matrix.append([])
            for x in range(columns):
                self._empty_matrix[y].append(0)
        
        return self._empty_matrix
    
    def _will_the_cell_live(self, current_state: Matrix, current_state_of_cell: int, x: int, y: int) -> bool:
        # print(f'Checking if cell [{x}][{y}] will live')
        living_cells_around: int = 0

        for surrounding_cell_Y_coord in range(y - 1, y + 2):
            for surrounding_cell_X_coord in range(x - 1, x + 2):
                if 0 <= surrounding_cell_X_coord <= (self._COLUMNS - 1) and 0 <= surrounding_cell_Y_coord <= (self._LINES - 1):
                    # print(f'Checking cell [{surrounding_cell_X}][{surrounding_cell_Y}]')
                    living_cells_around += current_state[surrounding_cell_Y_coord][surrounding_cell_X_coord]
                
        living_cells_around -= current_state[y][x]
        # print(f'Living cells around : {living_cells_around}')
        
        if (
            (current_state_of_cell == 0 and living_cells_around == 3) or
            (current_state_of_cell == 1 and 2 <= living_cells_around <= 3)
        ):
            return True
        else:
            return False
