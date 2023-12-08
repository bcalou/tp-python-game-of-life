"""Fichier de la classe Grid en python"""

from game_of_life.parameters import CELL_SIZE, SCREEN_SIZE
from game_of_life.parameters import Array2

# Paramètres

WIDTH, HEIGHT = SCREEN_SIZE

NEIGHBORS_COORDINATES = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0), (1, 1)
]


class Grid:
    """Classe représantant la grille de cellules"""

    def __init__(self, preset: Array2) -> None:
        """Constructeur"""

        # Créer une grille vide (matrice de 0)
        self.matrix: Array2 = \
            [[0] * (WIDTH // CELL_SIZE) for _ in range(HEIGHT // CELL_SIZE)]
        # Ajouter le preset (ajout de 1)
        self.__add_preset(preset)

    def is_grid_empty(self) -> bool:
        """Vérifie si la matrice (2D) est vide"""

        return not any(any(cell != 0 for cell in row) for row in self.matrix)

    def update_grid(self):
        """Donne le prochain état de la matrice donnée
        en utilisant les règles du jeu de la vie"""

        _grid_len_row = len(self.matrix)
        _grid_len_col = len(self.matrix[0])

        # Grille de l'état suivant, par défaut les cellules sont à 0 (morte)
        _next_state = [[0] * _grid_len_col for _ in range(_grid_len_row)]

        for row_id in range(_grid_len_row):
            for col_id in range(_grid_len_col):
                # Compter le nombre de voisins vivants
                live_neighbors = self.__count_living_neighbors(row_id, col_id)
                # Appliquer les règles du jeu de la vie
                if self.matrix[row_id][col_id] == 1:  # Si cellule vivante
                    if live_neighbors in (2, 3):
                        # Survie
                        _next_state[row_id][col_id] = 1
                else:  # Si cellule morte
                    if live_neighbors == 3:
                        # Naissance
                        _next_state[row_id][col_id] = 1

        self.matrix = _next_state

    def __count_living_neighbors(self, row_id: int, col_id: int) -> int:
        """Donne le nombre de voisins vivants d'une cellule spécifique"""

        _rows_len = len(self.matrix)
        _cols_len = len(self.matrix[0])

        # Parcourir les cellules voisines et compter celles vivantes
        _live_neighbors = sum(
            self.matrix[row_id + x][col_id + y]
            for x, y in NEIGHBORS_COORDINATES
            if 0 <= row_id + x < _rows_len and 0 <= col_id + y < _cols_len)

        return _live_neighbors

    def __add_preset(self, preset: Array2):
        """Ajouter un motif prédéfini (preset) au centre de la grille"""

        _preset_len_row = len(preset)
        _preset_len_col = len(preset[0])

        # Centre de la matrice
        _row_center = (HEIGHT // CELL_SIZE - _preset_len_col) // 2
        _col_center = (WIDTH // CELL_SIZE - len(preset[0])) // 2

        # Calculer la taille maximale de la cellule affichable
        _max_cell_size: int = min(WIDTH // _preset_len_row, HEIGHT // _preset_len_col)
        _sugg_cell_size: int = _max_cell_size // 10 + 4

        try:
            # Ajouter le preset au centre
            for row_offset, row in enumerate(preset):
                for col_offset, cell in enumerate(row):
                    self.matrix[_row_center + row_offset][_col_center + col_offset] = cell
        except IndexError:
            print("Taille d'écran ou de cellule invalide")
            print(f"Écran : ({WIDTH}, {HEIGHT}) px")
            print(f"Cellule : ({CELL_SIZE}) px")
            print(f"Taille de cellule suggérée : ({_sugg_cell_size}) px")
