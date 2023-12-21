import pygame
from grid_manager import GridManager, grid_type
from constants import *


class GameController:

    def game_logic(self, initial_grid: grid_type):

        pygame.init()

        grid_manager = GridManager(initial_grid)

        clock = pygame.time.Clock()

        done = False

        # Draw the initial state
        grid_manager.draw_grid()

        # While the game is not over
        while not done:

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    done = True

            # Update the grid
            grid_manager.set_next_grid()

            # Draw the grid
            grid_manager.draw_grid()

            print("Update !")
            clock.tick(1)
        pygame.quit()
