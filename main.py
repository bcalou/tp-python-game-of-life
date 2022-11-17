#!/bin/python3
""" Voici une implémentation du jeu de la vie de Conway.
La logique du jeu se trouve dans le dossier game_of_life.

Pour utiliser un fichier, il faut le placer dans le dossier saves et passer son
nom en argument de la ligne de commande. La ligne de commande est utilisable de
plusieurs manières :

    - python main.py                        # Lance le jeu avec une grille de 50x50 cases vides.
    - python main.py 100 100                # Lance le jeu avec une grille de 100x100 cases vides.
    - python main.py nom_de_sauvegarde      # Lance le jeu avec une grille enregistrée.


Sauvegardes fournies :

    - example                               # Petit spinner sur une grille de 5x5 cases.
    - canon                                 # Canon à glider vers le bas droite.
    - canon_inverse                         # Canon à glider vers le haut droite.


Commandes :
    
    - Echap                                 # Ferme le jeu.
    - Espace                                # Met en pause le jeu.
    - Clic gauche                           # Active ou désactive une cellule.
    - S                                     # Sauvegarde la grille dans un fichier.
    - R                                     # Remet la grille à zéro.
    - ↑                                     # Augmente la vitesse du jeu. (2 fps)
    - ↓                                     # Diminue la vitesse du jeu. (2 fps)


Auteur : Lucas LE DUDAL
"""

import sys

from game_of_life.game_controller import GameController
import game_of_life.save_manager as saver


def main():
    """Fonction principale du jeu.
    """
    # Valeurs à set :
    alive_cells: list[tuple[int, int]]
    size: tuple[int, int]
    cell_size: int

    # Récupération des arguments de ligne de commande
    if len(sys.argv) == 2:
        # Lecture du fichier de sauvegarde (le type de retour est looooooooong)

        map_data: tuple[list[tuple[int, int]], tuple[int, int]]
        map_data = saver.read_map(sys.argv[1])

        # Set des données
        alive_cells = map_data[0]
        size = map_data[1]

    elif len(sys.argv) == 3:
        # Set des données
        alive_cells = []
        size = (int(sys.argv[1]), int(sys.argv[2]))

    else:
        # Set des données
        alive_cells = []
        size = (50, 50)

    # Valeurs par défaut

    cell_size = min([1280 // size[0], 720 // size[1]])
    speed: int = 60  # fps

    # Lancement du jeu
    controller = GameController(
        size,
        alive_cells=alive_cells,
        cell_size=cell_size,
        speed=speed
    )
    controller.run()


if __name__ == "__main__":
    main()
