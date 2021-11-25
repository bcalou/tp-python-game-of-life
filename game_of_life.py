import pygame
import constants

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((constants.screen_size))
print(screen)
clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    print("Update !")

    screen.fill((constants.screen_fill))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 100, 100))
    pygame.display.flip()

    clock.tick(1)

    



pygame.quit()