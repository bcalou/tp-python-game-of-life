import pygame

from const import SCREEN_SIZE, FRAME_RATE

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    # ============ Game logic here =================

    for i in range(10):
        pygame.draw.rect(screen, (255, 255, 255), (i*50, i*50, 100, 100))

    # =============================================

    pygame.display.flip()

    # print("Update !")
    clock.tick(FRAME_RATE)

pygame.quit()


def get_next_state():
    pass
