from typing import Any
from game_of_life.cell import *

class Grid:
    # grille sur laquelle les cellules se déplaceront
    grid: list[list[Cell]]
    # hauteur de la grille
    height: int
    # largeur de la grille
    width: int
    
    def __init__(self, grid: list[list[Cell]], height: int, width: int) -> None:
        """constructeur"""
        self.grid = grid
        self.height = height
        self.width = width

    def get_grid(self) -> list[list[Cell]]:
        return self.grid

    def get_height(self) -> int:
        return self.height
    
    def get_width(self) -> int:
        return self.width
    
    # on va créer un nouveau tableau avec les nouvelles valeurs pour ne pas 
    # Avoir de problème si nous les changeont toutes petit à petit 
    def get_next_state(self, state: list[list[Cell]]) -> list[list[Cell]]:
        return self.grid
