import pygame
from game_of_life.game_manager import Game
from game_of_life.view_manager import View

pygame.init()

def main():
    """Simulate the game of life"""

    View(Game())


main()
