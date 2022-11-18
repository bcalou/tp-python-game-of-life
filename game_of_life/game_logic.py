"""Ce fichier contient les fonctions qui gèrent la logique du jeu de la vie.
"""

import game_of_life.const as const
from game_of_life.types import *

class GameLogic:
    """Classe qui gère la logique du jeu.
    """

    def __init__(self, grid: Grid, size: Size):
        """Initialise la logique du jeu.
        """
        self.grid: Grid = grid
        self.size: Size = size

    def get_next_state(self) -> Grid:
        """Fonction qui calcule la génération suivante du jeu.
        """
        new_grid = [[0 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                new_grid[y][x] = self.is_alive((x, y))

        self.grid = [line[:] for line in new_grid]
        return new_grid

    def is_alive(self, coords: Coords) -> int:
        """Fonction qui vérifie si une cellule sera vivante ou non.
        """
        neighbours: int = self.get_neighbours(coords)
        if self.grid[coords[1]][coords[0]] == 1:
            if neighbours < 2 or neighbours > 3:
                return 0  # Décès par solitude ou surpopulation

            return 1  # Survie

        elif neighbours == 3:
            return 1  # Naissance

        return 0  # Reste morte

    def get_neighbours(self, coords: Coords) -> int:
        """Fonction qui compte le nombre de voisins d'une cellule.
        """
        neighbours: int = 0
        x: int = coords[0]
        y: int = coords[1]

        for line in range(-1, 2):
            for col in range(-1, 2):
                if (
                    line == 0 and col == 0 or x+line < 0 or
                    x+line >= len(self.grid[0]) or y+col < 0 or
                    y+col >= len(self.grid)
                ):
                    continue

                neighbours += self.grid[y+col][x+line]

        return neighbours

    def rotate_grid(self,grid: Grid, rotations: int) -> Grid:
        """Tourne une grille dans le sens des aiguilles d'une montre du nombre de
        rotations spécifiées.
        """
        old_grid: Grid
        old_grid = [line[:] for line in grid]

        new_grid: Grid 
        for _ in range(rotations):
            new_grid = [
                [old_grid[y][x] for y in range(len(old_grid))]
                for x in range(len(old_grid[0])-1, -1, -1)
            ]
            old_grid = [line[:] for line in new_grid]

        return old_grid
