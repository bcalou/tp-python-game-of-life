""" Voici une implémentation du jeu de la vie de Conway.
    Le jeu de la vie est un automate cellulaire imaginé par John Horton Conway en 1970.

    La logique du jeu se trouve dans le dossier game_of_life.
    Auteur : Lucas LE DUDAL
"""

from game_of_life.game_controller import GameController

def main():
    """Fonction principale du jeu.
    """
    # Lancement du jeu
    controller = GameController((10, 10), [(2, 2), (3, 2), (4, 2)], 50)
    controller.run()

if __name__ == "__main__":
    main()