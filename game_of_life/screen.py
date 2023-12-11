"""Fichier de la classe Screen en python"""

import pygame
from game_of_life.grid import Grid
from .parameters import COLORS, PRESET_COLOR, SCREEN_SIZE, CELL_SIZE


class Screen:
    """Classe représantant l'écran de jeu'"""

    def __init__(self):
        """Constructeur"""

        # Initialiser l'écran de jeu avec pygame
        pygame.init()
        self.__screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Game of Life")

    def draw_grid(self, grid: Grid):
        """Afficher la grille à l'écran"""

        # Mettre à jour l'écran en affichant la grille passée en paramètre
        self.__screen.fill(COLORS['black'])  # Fond d'écran
        for row_index, row in enumerate(grid.matrix):
            for cell_index, cell in enumerate(row):
                if cell == 1:
                    # Dessine une cellule à carré pour chaque cellule à 1
                    x = cell_index * CELL_SIZE
                    y = row_index * CELL_SIZE
                    pygame.draw.rect(
                        self.__screen, PRESET_COLOR,
                        (x, y, CELL_SIZE, CELL_SIZE)
                    )

        pygame.display.flip()
