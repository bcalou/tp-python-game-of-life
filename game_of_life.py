import pygame
from copy import deepcopy
from pygame import constants
from matrice import *
from affichage import update_screen
from jeu import get_next_state
import constant

pygame.init()
current_state: list[list[int]] = deepcopy(initial_state)
screen: pygame.surface.Surface = pygame.display.set_mode((constant.window_size, constant.window_size))
clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():
        current_state = get_next_state(current_state)
        update_screen(screen, current_state)
        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    print("Update !")
    clock.tick(FRAME_RATE)

pygame.quit()