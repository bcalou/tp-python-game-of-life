import pygame
import game_of_life.global_variables as gv

class Game_of_life:
    state_matrix: list[list[int]] = []

    def __init__(self, initial_state: list[list[int]]):
        """
        Constructor of the Game_of_life class.
        """
        self.state_matrix = initial_state

    def count_neighbors(self, x, y, current_state):
        """
        Counts the number of neighbors of a cell.
        """
        count = 0
        for i in range(max(0, x - 1), min(x + 2, len(current_state))):
            for j in range(max(0, y - 1), min(y + 2, len(current_state[0]))):
                count += current_state[i][j]
        count -= current_state[x][y]
        return count
        
    def get_next_state(self, current_state: list[list[int]]) -> list[list[int]]:
        """
        Returns the next state of the game of life.
        """
        next_state = [[0 for _ in range(len(current_state[0]))] for _ in range(len(current_state))]
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                neighbors = self.count_neighbors(i, j, current_state)
                if current_state[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    next_state[i][j] = 0
                elif current_state[i][j] == 0 and neighbors == 3:
                    next_state[i][j] = 1
                else:
                    next_state[i][j] = current_state[i][j]
        return next_state
    
    def draw(self, screen: pygame.Surface):
        """
        Draws the current state of the game of life.
        """
        for i in range(len(self.state_matrix)):
            for j in range(len(self.state_matrix[i])):
                if self.state_matrix[i][j] == 1:
                    pygame.draw.rect(screen, gv.BLACK, (j * gv.CELL_SIZE, i * gv.CELL_SIZE, gv.CELL_SIZE, gv.CELL_SIZE))