import pygame
import consts
from game import draw_game_state

pygame.init()

def main():
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    clock = pygame.time.Clock()

    done = False

    # While the game is not over
    while not done:

        # clean the screen at the begining and draw state
        screen.fill((0, 0, 0))
        draw_game_state(screen)

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


main()
