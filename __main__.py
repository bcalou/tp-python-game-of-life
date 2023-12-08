import pygame
import random

screen = pygame.display.set_mode((1000, 1000))
screen.fill((0, 0, 0))

pygame.init()

clock = pygame.time.Clock()

done = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (255, 255, 255), (random.randint(0, 100), random.randint(0, 100), 100, 100))
    pygame.display.flip()
    clock.tick(1)
initial_state: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

pygame.quit()