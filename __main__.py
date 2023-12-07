import pygame
from pygame.time import Clock

from game_of_life.grid_manager import GridManager
from game_of_life.screen_manager import ScreenManager


def main() -> None:
    clock: Clock = pygame.time.Clock()

    done: bool = False

    grid_manager: GridManager = GridManager()
    screen_manager: ScreenManager = ScreenManager()

    # While the game is not over
    while not done:
        # Listen for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen_manager.draw_grid(grid_manager.get_grid())
        clock.tick(30)
        grid_manager.update_grid()

    pygame.quit()


main()
