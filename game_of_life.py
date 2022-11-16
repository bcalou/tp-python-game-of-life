import pygame

from const import SCREEN_SIZE, FRAME_RATE, INITIAL_STATE, CUBE_SIZE

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

    # Drawing initial state
    for line_index in range(len(INITIAL_STATE)):
        for column_index in range(len(INITIAL_STATE[line_index])):

            # Draw a cube each time there is a 1 in the matrix
            if INITIAL_STATE[column_index][line_index] == 1:
                # A cube position depends on its line/column index multiplied
                # by its size because the screen is exactly the size of a
                # line of cubes
                pygame.draw.rect(screen, (255, 255, 255), (
                    CUBE_SIZE * line_index, CUBE_SIZE * column_index, CUBE_SIZE,
                    CUBE_SIZE))

    # =============================================

    pygame.display.flip()

    # print("Update !")
    clock.tick(FRAME_RATE)

pygame.quit()


def get_next_state():
    pass
