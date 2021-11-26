import pygame
from copy import deepcopy
from data import *
from game import get_next_state
from display import update_screen

# Init
pygame.init()
current_state: list[list[int]] = deepcopy(initial_state)
screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Loop
playing: bool = False
done: bool = False
while not done:
    for event in pygame.event.get():
        # Close button
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Escape = Quit
            if event.key == pygame.K_ESCAPE:
                done = True
            # Start / Pause simulation
            elif event.key == pygame.K_SPACE:
                playing = not playing

    if playing:
        current_state = get_next_state(current_state)
    update_screen(screen, current_state)
    clock.tick(FRAME_RATE)

pygame.quit()
