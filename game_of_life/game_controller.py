"""Cette classe est le controlleur principal du jeu.
Elle gère les interactions générales entre les éléments du jeu.

Je choisis le format alive_cells plutôt que grid, afin de faciliter l'écriture
à la main de la grille de départ. Les outils pour passer d'un format à l'autre
sont dans le fichier save_manager.py.
"""
# Public libs
from pygame.time import Clock

# Local imports
from game_of_life.game_displayer import GameDisplayer
from game_of_life.save_manager import alives_to_grid
import game_of_life.game_logic as logic


class GameController:
    """Classe qui gère les interactions entre les éléments du jeu.
    """

    def __init__(
        self,
        size: tuple[int, int],
        alive_cells: list[tuple[int, int]] = [],
        cell_size: int = 10,
        speed: int = 2
    ):
        """Initialise le controlleur du jeu.
        """
        # Stockage des valeurs
        self.size: tuple[int, int] = size
        self.cell_size: int = cell_size
        self.speed: int = speed

        # Génération de la grille
        self.grid: list[list[int]] = alives_to_grid(alive_cells, size)

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

            # Editer au clic
            clic = self.displayer.get_clicked()
            if clic != (-1, -1):
                # Toogle de la case cliquée
                self.grid[clic[1]][clic[0]] = 1 - self.grid[clic[1]][clic[0]]

            # Gestion de la pause (espace)
            if self.displayer.is_running():
                # Calcul de la nouvelle grille
                self.grid = logic.get_next_state(self.grid)

            # Affichage
            self.displayer.draw(self.grid)

        # Fermeture de la fenêtre
        self.displayer.quit()
