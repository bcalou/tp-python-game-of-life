from typing import Any
import pygame
from game_of_life.cell import *

class Grid:
    # grille de cellules sur laquelle évoluront les cellules
    grid: list[list[int]]
    
    def __init__(self,grid: list[list[int]]) -> None:
        """constructeur de la grille"""

        self.grid = grid
        # taille de la grille
        self.WIDTH_GRID: int = 500
        # nombre de cellules   
        self.NB_CELLS = 50
        # # taille d'une cellule 
        self.WIDTH_CELL: int = self.WIDTH_GRID // self.NB_CELLS

    def get_grid(self) -> list[list[int]]:
        return self.grid 
    
    def get_width_grid(self) -> int:
        return self.WIDTH_GRID
    
    # on va créer un nouveau tableau avec les nouvelles valeurs pour ne pas 
    # Avoir de problème si nous les changeont toutes petit à petit 
    def get_next_state(self, state: list[list[int]]) -> list[list[int]]:
        return self.grid
    
    def build_grid(self):
        
        screen = pygame.display.set_mode((self.WIDTH_GRID, self.WIDTH_GRID))
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, self.WIDTH_GRID, self.WIDTH_GRID))
        for x in range (self.NB_CELLS - 1):
            for y in range (self.NB_CELLS -1):
                current_cell = self.grid[x][y]
                color = self.get_color(current_cell)
                pygame.draw.rect(screen, (color, color, color), (y*self.WIDTH_CELL, x*self.WIDTH_CELL, self.WIDTH_CELL, self.WIDTH_CELL))
        
        pygame.display.flip()
        
    def get_color(self, cell_state: int) -> int:
        if cell_state == 1 : return 255
        else: return 0
