import pygame
import game_of_life.global_variables as gv
from game_of_life.game_of_life import Game_of_life

pygame.init()


def main():
    screen = pygame.display.set_mode((gv.WINDOW_WIDTH, gv.WINDOW_HEIGHT))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    done = False

    game_of_life = Game_of_life(gv.INITIAL_STATE2)

    # While the game is not over
    while not done:
        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        screen.fill(gv.WHITE)

        game_of_life.draw(screen)

        # update state
        game_of_life.state_matrix = game_of_life.get_next_state(
            game_of_life.state_matrix)

        pygame.display.flip()
        print("Update !")
        clock.tick(50)

    pygame.quit()


main()
