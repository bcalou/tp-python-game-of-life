import pygame
from pygame.surface import Surface
from data import *


def update_screen(screen: Surface, current_state: list[list[int]]):
    # Clear screen
    screen.fill((255, 255, 255))

    # Display state
    for y in range(len(current_state)):
        for x in range(len(current_state[y])):
            # Living cells are drawn in black
            if current_state[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                                                x * CELL_SIZE, y * CELL_SIZE,
                                                CELL_SIZE, CELL_SIZE))

        # Display grid ((de)activable in data.py)
            if DISPLAY_GRID and y == 0:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                                                x * CELL_SIZE, 0,
                                                1, SCREEN_SIZE[1]))
        if DISPLAY_GRID:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                                                0, y * CELL_SIZE,
                                                SCREEN_SIZE[0], 1))
    pygame.display.flip()
