import pygame
from game_of_life_manager import Game
from view_manager import View

pygame.init()

def main():
    """Simulate the game of life"""

    View(Game())


main()
