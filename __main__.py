"""main.py"""

import sys
import os
import json
import pygame
from game_of_life.parameters import FRAME_RATE, PRESET_NAME
from game_of_life.screen import Screen
from game_of_life.grid import Grid


def __read_json():
    """Lire les données JSON à partir du fichier spécifié"""
    current_directory = os.path.dirname(__file__)
    json_folder_path = os.path.join(current_directory, 'game_of_life')
    json_file_path = os.path.join(json_folder_path, 'game_of_life.json')

    with open(json_file_path, 'r') as fichier:
        donnees_json = json.load(fichier)
    return donnees_json


def __exit_game():
    """Quitter le jeu"""

    pygame.quit()
    sys.exit()


def __main():
    """Fonction principale"""
    # Charger le preset depuis le fichier JSON

    presets_data = __read_json()
    try:
        preset = presets_data["Presets"][PRESET_NAME]
    except KeyError:
        print(f"Erreur : Le preset '{PRESET_NAME}' n'existe pas.")
        sys.exit(1)

    # Objets

    screen = Screen()
    grid = Grid(preset)

    # Pygame

    clock = pygame.time.Clock()
    close = False

    # Boucle de jeu

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
        clock.tick(FRAME_RATE)

        # Quitter si la grille est vide
        if grid.is_grid_empty():
            __exit_game()


if __name__ == "__main__":
    __main()
