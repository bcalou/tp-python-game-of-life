""" Voici une implémentation du jeu de la vie de Conway.
Le jeu de la vie est un automate cellulaire imaginé par John Horton Conway.

La logique du jeu se trouve dans le dossier game_of_life.
Auteur : Lucas LE DUDAL
"""

from game_of_life.game_controller import GameController
import game_of_life.save_manager as saver


def main():
    """Fonction principale du jeu.
    """
    # Lecture du fichier de sauvegarde (oui, le type de retour est loooooooong)
    map_data: tuple[list[tuple[int, int]], tuple[int, int]]
    map_data = saver.read_map("saves/canon.gol")

    # Récupération des données
    alive_cells: list[tuple[int, int]] = map_data[0]
    size: tuple[int, int] = map_data[1]
    cell_size: int = min([1280 // size[0], 720 // size[1]])

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
