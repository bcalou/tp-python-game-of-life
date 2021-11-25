import pygame
import constants

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((constants.screen_size))
clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    #print("Update !")

    screen.fill((constants.screen_fill))

    initial_state: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    cell_size_x : float = constants.screen_size[0] / len(initial_state)
    cell_size_y : float = constants.screen_size[1] / len(initial_state)

    for y in range(len(initial_state)):
        for x in range(len(initial_state)):
            if initial_state[y][x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*cell_size_x, y*cell_size_y, cell_size_x, cell_size_y))
    pygame.display.flip()

    clock.tick(1)

    



pygame.quit()