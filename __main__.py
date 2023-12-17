import pygame
from game_of_life.game_manager import Game, GameState
from game_of_life.view_manager import View

pygame.init()


def main():
    """Simulate the game of life"""

    view: View = View()
    game_manager: Game = Game()
    done: bool = False
    clock = pygame.time.Clock()

    # While the game is not over
    while not done:

        # Draw the current state of the game
        new_state: GameState = game_manager.get_next_state()
        view.draw_current_state(new_state)

        # Check if user closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Redraw the game 30 times per second
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


main()
