"""Cette classe est le controlleur principal du jeu.
Elle gère les interactions générales entre les éléments du jeu.
"""

from game_of_life.game_displayer import GameDisplayer
import game_of_life.game_logic as logic 

from pygame.time import Clock
class GameController:
    """Classe qui gère les interactions entre les éléments du jeu.
    """

    def __init__(self, size: tuple[int, int], alive_cells: list[tuple[int, int]], cell_size: int, speed: int = 2):
        """Initialise le controlleur du jeu.
        """
        # Stockage des valeurs
        self.size: tuple[int, int] = size
        self.cell_size: int = cell_size
        self.speed: int = speed

        # Génération de la grille
        self.grid: list[list[int]] = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]
        for cell in alive_cells:
            self.grid[cell[1]][cell[0]] = 1

        # Création de l'affichage
        self.displayer = GameDisplayer(self.size, self.cell_size)

        # Création du timer
        self.clock = Clock()

    def run(self):
        """Fonction principale du jeu.
        """
        while True:
            self.clock.tick(self.speed)
            # Vérification de la fermeture de la fenêtre
            if self.displayer.is_closing():
                break
            # Gestion de la pause (espace)
            if self.displayer.is_running():
                # Calcul de la nouvelle grille
                self.grid = logic.get_next_state(self.grid)

            # Affichage
            self.displayer.draw(self.grid)

        # Fermeture de la fenêtre
        self.displayer.quit()