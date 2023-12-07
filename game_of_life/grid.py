"""Fichier de la classe Grid en python"""

from game_of_life.parameters import CELL_SIZE, SCREEN_SIZE
from game_of_life.parameters import Array2

width, height = SCREEN_SIZE

class Grid:
    """Classe représantant la grille de cellules"""
    def __init__(self, preset: Array2) -> None:
        """Constructeur"""
        # Créer la grille vide (matrice de 0)
        self.matrix: Array2 = \
            [[0] * (width // CELL_SIZE) for _ in range(height // CELL_SIZE)]
        # Ajouter le preset (ajout de 1)
        self.__add_preset(preset)

    def is_grid_empty(self) -> bool:
        """Vérifie si la matrice (2D) est vide"""
        for row in self.matrix:
            for element in row:
                if element != 0:
                    return False
        return True

    def update_grid(self):
        """Donne le prochain état de la matrice donnée"""

        rows = len(self.matrix)
        cols = len(self.matrix[0])

        # Grille de l'état suivant
        next_state = [[0] * cols for _ in range(rows)]

        for row_id in range(rows):
            for col_id in range(cols):
                # Compter le nombre de voisins vivants
                living_neighbors = self.__count_living_neighbors(row_id, col_id)

                # Appliquer les règles du jeu de la vie
                if self.matrix[row_id][col_id] == 1:  # Si cellule vivante
                    if living_neighbors < 2 or living_neighbors > 3:
                        next_state[row_id][col_id] = 0  # Mort par sous-population ou surpopulation
                    else:
                        next_state[row_id][col_id] = 1  # Survie
                else:                                  # Si cellule morte
                    if living_neighbors == 3:
                        next_state[row_id][col_id] = 1  # Naissance
                    else:
                        next_state[row_id][col_id] = 0  # Reste morte

        self.matrix = next_state

    def __count_living_neighbors(self, row_id: int, col_id: int) -> int:
        """Donne le nombre de voisins d'une cellule"""

        rows_len = len(self.matrix)
        cols_len = len(self.matrix[0])
        living_neighbors = 0

        # Coordonnées relatives des voisins autour de la cellule
        neighbors_coordinates = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for x_neighbor, y_neighbor in neighbors_coordinates:
            row_neighbor, col_neighbor = row_id + x_neighbor, col_id + y_neighbor
            # +1 voisin si dans la grille
            if 0 <= row_neighbor < rows_len and 0 <= col_neighbor < cols_len:
                living_neighbors += self.matrix[row_neighbor][col_neighbor]

        return living_neighbors

    def __add_preset(self, preset: Array2):
        """Ajouter le preset au centre de la grille"""
        grid_len_row = len(self.matrix)
        grid_len_col = len(self.matrix[0])

        preset_len_row = len(preset)
        preset_len_col = len(preset[0])

        # Centre de la matrice
        row_center = (height // CELL_SIZE - len(preset)) // 2
        col_center = (width // CELL_SIZE - len(preset[0])) // 2

        # Calculer la taille maximale de la cellule affichable
        max_cell_size: int = min(width // preset_len_row, height // preset_len_col)
        sugg_cell_size: int = max_cell_size // 10 + 4

        print("preset:")
        print(preset_len_row)
        print(preset_len_col)
        print("grille:")
        print(grid_len_row)
        print(grid_len_col)

        # Ajouter le preset au centre
        if 0 <= preset_len_row <= grid_len_row and \
            0 <= preset_len_col <= grid_len_col:
            for row_offset, row in enumerate(preset):
                for col_offset, cell in enumerate(row):
                    self.matrix[row_center + row_offset][col_center + col_offset] = cell
        else:
            print("Taille d'écran ou de cellule invalide")
            print(f"Écran : ({width}, {height}) px")
            print(f"Cellule : ({CELL_SIZE}) px")
            print(f"Taille de cellule suggérée : ({sugg_cell_size}) px")
