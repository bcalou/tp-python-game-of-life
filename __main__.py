# main.py

import sys
import os
import json
import pygame
from game_of_life.parameters import FRAME_RATE
from game_of_life.screen import Screen
from game_of_life.grid import Grid

pygame.init()

def main():
    """Magie..."""

    # Charger les presets depuis le fichier JSON

    current_directory = os.path.dirname(__file__)
    json_folder_path = os.path.join(current_directory, 'game_of_life')
    json_file_path = os.path.join(json_folder_path, 'game_of_life.json')

    with open(json_file_path, 'r') as file:
        presets_data = json.load(file)

    # Presets disponibles : Glider, Blinker, Toad, Pulsar, Canon
    preset = presets_data["Presets"]["Pulsar"]

    # Pygame

    clock = pygame.time.Clock()
    close = False

    # Constructeurs

    screen = Screen()
    grid = Grid(preset)

    pygame.display.set_caption("Game of Life")

    # Jeu

    while not close:
        # Evènements de jeu
        for event in pygame.event.get():
            # Quitter le jeu
            if event.type == pygame.QUIT:
                close = True

        # Afficher la grille
        screen.draw_grid(grid)

        # Mettre à jour la grille
        grid.update_grid()
        print("Update !")
        clock.tick(FRAME_RATE)

        # Quitter si la grille est vide
        if grid.is_grid_empty():
            close = True

    pygame.quit()
    sys.exit()

main()
