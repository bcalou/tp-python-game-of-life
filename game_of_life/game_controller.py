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
from game_of_life.save_manager import write_map, grid_to_alives


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

        # Paramètres par défaut
        self.looping: bool = False
        self.paused: bool = False

        # Génération de la grille
        self.grid: list[list[int]] = alives_to_grid(alive_cells, size)

        # Création de l'affichage
        self.displayer = GameDisplayer(self, self.size, self.cell_size)

        # Création du timer
        self.clock = Clock()

    def run(self):
        """Fonction principale du jeu.
        """
        self.looping = True
        while self.looping:
            self.clock.tick(self.speed)
            
            # Gestion des évènements
            self.displayer.handle_events()

            # Gestion de la pause (espace)
            if not self.paused:
                self.grid = logic.get_next_state(self.grid)

            # Affichage
            self.displayer.draw(self.grid)

        # Fermeture de la fenêtre
        self.displayer.quit()

    def toggle_cell(self, x: int, y: int):
        """Modifie la valeur d'une case de la grille.
        """
        self.grid[y][x] = 1 - self.grid[y][x]

    def reset_grid(self):
        """Change la grille du jeu.
        """
        self.grid = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]

    def set_speed(self, speed: int):
        """Change la vitesse du jeu.
        """
        self.speed = speed

    def toggle_paused(self):
        """Change l'état de pause du jeu.
        """
        self.paused = not self.paused

    def quit(self):
        """Ferme le jeu.
        """
        self.looping = False

    def save_grid(self, name: str):
        """Sauvegarde la grille du jeu.
        """
        write_map(name, grid_to_alives(self.grid), self.size)
        