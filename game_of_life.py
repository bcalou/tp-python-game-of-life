import pygame
from pygame import constants
import constant

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((constant.window_size, constant.window_size))
clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 10, 10))
        pygame.display.flip()
        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    print("Update !")
    clock.tick(1)

pygame.quit()