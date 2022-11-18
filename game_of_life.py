import pygame

from const import SCREEN_SIZE, FRAME_RATE, INITIAL_STATE, CUBE_SIZE, ALIVE, \
    Coordinates
from game_of_life.game import GameState

pygame.init()
screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
done: bool = False

# create our game state class with our initial state
game: GameState = GameState(INITIAL_STATE)

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # Check every cell of the game
    for line_index in range(len(game.get_state())):
        for column_index in range(len(game.get_state()[line_index])):

            cell_position: Coordinates = (column_index, line_index)

            if game.get_state()[column_index][line_index] == ALIVE:
                # Draw a cube each time there is a 1 in the matrix
                pygame.draw.rect(screen, (0, 0, 0), (
                    CUBE_SIZE * line_index, CUBE_SIZE * column_index, CUBE_SIZE,
                    CUBE_SIZE))

                # Update the cell status for the next state
                game.update_alive_cell_status(cell_position)
            else:
                # Update the cell status for the next state
                game.update_dead_cell_status(cell_position)

    # Update state for next render
    game.update_state()

    pygame.display.flip()
    clock.tick(FRAME_RATE)

pygame.quit()
