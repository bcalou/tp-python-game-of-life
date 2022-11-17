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
from game_of_life.save_manager import read_map, write_map, grid_to_alives


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
        self.paused: bool = True
        self.template: list[list[int]] = []
        self.template_rota: int = 0

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
        if self.template:
            self.place_template(x, y)
        else:
            self.grid[y][x] = 1 - self.grid[y][x]

    def reset_grid(self):
        """Change la grille du jeu.
        """
        self.grid = [
            [0 for _ in range(self.size[0])] for _ in range(self.size[1])
        ]

    def lower_speed(self):
        """Baisse la vitesse du jeu.
        """
        if self.speed > 2:
            self.speed -= 2

    def raise_speed(self):
        """Augmente la vitesse du jeu.
        """
        if self.speed < 60:
            self.speed += 2

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
    
    def load_template(self, id: int):
        """Permet d'afficher un template
        """
        
        template: tuple[list[tuple[int, int]], tuple[int, int]]
        template = read_map(f"templates/{id}")
        self.template = alives_to_grid(template[0], template[1])

    def place_template(self, place_x: int, place_y: int):
        """Permet de placer un template
        """
        # On tourne le template
        self.template = logic.rotate_grid(self.template, self.template_rota)
        
        for y in range(len(self.template)):
            for x in range(len(self.template[0])):
                self.grid[place_y + y][place_x + x] = self.template[y][x]

        self.template = []
        self.template_rota = 0

    def rotate_template(self, rotation: int):
        """Permet de tourner un template
        """
        self.template_rota = rotation
