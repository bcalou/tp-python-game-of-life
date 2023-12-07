import pygame
from .parameters import COLORS, SCREEN_SIZE, CELL_SIZE

class Screen:
    def __init__(self):
        """Constructeur"""
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Game of Life")

    def draw_grid(self, grid):
        # Afficher la grille à l'écran
        self.screen.fill(COLORS['white'])
        for row_index, row in enumerate(grid):
            for element_index, element in enumerate(row):
                x = element_index * CELL_SIZE
                y = row_index * CELL_SIZE
                if element == 1:
                    pygame.draw.rect(self.screen, COLORS['pink'], (x, y, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
