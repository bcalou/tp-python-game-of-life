import pygame

from const import SCREEN_SIZE, FRAME_RATE, INITIAL_STATE, CUBE_SIZE
from game_of_life.game import GameState

pygame.init()
screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
done: bool = False

# The game class containing our game state
game: GameState = GameState(INITIAL_STATE)

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # Draw the state
    for line_index in range(len(game.get_state())):
        for column_index in range(len(game.get_state()[line_index])):

            # Draw a cube each time there is a 1 in the matrix
            if game.get_state()[column_index][line_index] == 1:
                # A cube position depends on its line/column index multiplied
                # by its size because the screen is exactly the size of a
                # line of cubes
                pygame.draw.rect(screen, (0, 0, 0), (
                    CUBE_SIZE * line_index, CUBE_SIZE * column_index, CUBE_SIZE,
                    CUBE_SIZE))

    # Update state for next render
    game.update_state()

    pygame.display.flip()
    clock.tick(FRAME_RATE)

pygame.quit()
