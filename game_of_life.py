import pygame

from const import SCREEN_SIZE, FRAME_RATE, INITIAL_STATE, CUBE_SIZE
from game_of_life.game import get_next_state

pygame.init()
screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
done: bool = False

# Matrix to represent our game
state: list[list[int]] = INITIAL_STATE

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    # ============ Game logic here =================

    # Drawing state
    for line_index in range(len(state)):
        for column_index in range(len(state[line_index])):

            # Draw a cube each time there is a 1 in the matrix
            if state[column_index][line_index] == 1:
                # A cube position depends on its line/column index multiplied
                # by its size because the screen is exactly the size of a
                # line of cubes
                pygame.draw.rect(screen, (255, 255, 255), (
                    CUBE_SIZE * line_index, CUBE_SIZE * column_index, CUBE_SIZE,
                    CUBE_SIZE))

    # Get the next state
    state = get_next_state(state)

    # =============================================

    pygame.display.flip()

    # print("Update !")
    clock.tick(FRAME_RATE)

pygame.quit()
