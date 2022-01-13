import pygame
from copy import deepcopy
from display import *

def count_neighbors(current_state: list[list[int]], x: int, y: int) -> int:
    return sum([1 for i in (-1, 0, 1) for j in (-1, 0, 1)
                if x+i >= 0 and x+i < len(current_state[0]) and
                y+j >= 0 and y+j < len(current_state) and
                (i != 0 or j != 0) and
                current_state[y+j][x+i] == 1])

def get_next_state(current_state: list[list[int]]) -> list[list[int]]:

    next_state: list[list[int]] = deepcopy(current_state)
    for y in range(len(current_state)):
        for x in range(len(current_state[y])):
            neighborCellsCount: int = count_neighbors(current_state, x, y)

            if neighborCellsCount < 2 or neighborCellsCount > 3:
                next_state[y][x] = 0
            elif neighborCellsCount == 3:
                next_state[y][x] = 1
    return next_state


pygame.init()
current_state: list[list[int]] = deepcopy(initial_state)
screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

playing: bool = False
done: bool = False
while not done:
    if playing:
        current_state = get_next_state(current_state)
    update_screen(screen, current_state)
    clock.tick(FRAME_RATE)

pygame.quit()

