import pygame
from matrice import *
from pygame.surface import Surface



def update_screen(screen: Surface, current_state: list[list[int]]):
    # Ecran reinitialisé
    screen.fill((0, 0, 0))

    # Affichage
    for y in range(len(current_state)):
        for x in range(len(current_state[y])):
            # Les cellules vivantes sont blanches
            if current_state[y][x]:
                pygame.draw.rect(screen, ( 250, 250, 250), pygame.Rect(
                                                x * CELL_SIZE, y * CELL_SIZE,
                                                CELL_SIZE, CELL_SIZE))
    pygame.display.flip()