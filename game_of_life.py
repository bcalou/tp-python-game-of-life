import pygame

SCREEN_SIZE:int = 1000
pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:
    screen.fill((255, 255, 255))
    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 0, 0), (100, 200, 100, 100))


    print("Update !")
    pygame.display.flip()

    clock.tick(1)

pygame.quit()
def get_next_state():
    pass
