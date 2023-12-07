from typing import Any
import pygame

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
        
        self.SCREEN = pygame.display.set_mode((self.WIDTH_GRID, self.WIDTH_GRID))

    def get_grid(self) -> list[list[int]]:
        return self.grid 
    
    def get_width_grid(self) -> int:
        return self.WIDTH_GRID
    
    def build_grid(self):
        
        
        pygame.draw.rect(self.SCREEN, (255, 255, 255), (0, 0, self.WIDTH_GRID, self.WIDTH_GRID))
        for x_pos in range (self.NB_CELLS - 1):
            for y_pos in range (self.NB_CELLS -1):
                current_cell = self.grid[x_pos][y_pos]
                color = self.get_color(current_cell)
                pygame.draw.rect(self.SCREEN, (color, color, color), (y_pos*self.WIDTH_CELL, x_pos*self.WIDTH_CELL, self.WIDTH_CELL, self.WIDTH_CELL))
        
        pygame.display.flip()
        
    # on va créer un nouveau tableau avec les nouvelles valeurs pour ne pas 
    # Avoir de problème si nous les changeont toutes petit à petit 
    def draw_next_state(self):
        new_grid = list[list[int]]
        for x_pos in range(self.NB_CELLS - 1):
            for y_pos in range (self.NB_CELLS - 1):
                current_cell = self.new_state_cell(self.grid[x_pos][y_pos], x_pos, y_pos)
                color = self.get_color(current_cell)
                pygame.draw.rect(self.SCREEN, (color, color, color), (y_pos*self.WIDTH_CELL, x_pos*self.WIDTH_CELL, self.WIDTH_CELL, self.WIDTH_CELL))
                
        pygame.display.flip()     
        
    def get_color(self, cell_state: int) -> int:
        if cell_state == 1 : return 255
        else: return 0
        
    def new_state_cell(self, current_cell_state: int, x_pos: int, y_pos: int) -> int:
        arround_cells = self.cells_alive_arrond_current_cell(x_pos, y_pos)
        if current_cell_state == 0 and arround_cells == 3: return 1
        elif arround_cells == 2: return current_cell_state
        elif current_cell_state == 1 and arround_cells == 3: return 1
        return 0 # elif current_cell_state == 1 and 2 < arround_cells < 3:
    
    def cells_alive_arrond_current_cell(self, x_pos: int, y_pos: int) -> int:
        """compte le nombre de cellules autour de la cellule testée"""
        counter = 0
        # on vérifie tout pour éviter les exexptions
        if x_pos != 0 and y_pos != 0: counter += self.grid[x_pos-1][y_pos-1]
        if x_pos != 0: counter += self.grid[x_pos-1][y_pos]
        if x_pos != 0 and y_pos < 48: counter += self.grid[x_pos-1][y_pos+1]
        if x_pos < 48 and y_pos != 0: counter += self.grid[x_pos+1][y_pos-1]
        if x_pos < 48: counter += self.grid[x_pos+1][y_pos]
        if x_pos < 48 and y_pos < 48: counter += self.grid[x_pos+1][y_pos+1]
        if y_pos != 0: counter += self.grid[y_pos-1][x_pos]
        if y_pos < 48: counter += self.grid[y_pos+1][x_pos]
        return counter
