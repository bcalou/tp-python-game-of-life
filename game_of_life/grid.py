from game_of_life.parameters import CELL_SIZE, SCREEN_SIZE

width, height = SCREEN_SIZE

class Grid:

    def __init__(self, preset) -> None:
        """Constructeur"""
        # Créer la grille vide (matrice de 0)
        self.matrix: list[list[int]] = [[0] * (width // CELL_SIZE) for _ in range(height // CELL_SIZE)]

        preset_len_row = len(preset)
        preset_len_col = len(preset[0])

        grid_len_row = len(self.matrix)
        grid_len_col = len(self.matrix[0])

        # Centre de la matrice
        row_center = (height // CELL_SIZE - len(preset)) // 2
        col_center = (width // CELL_SIZE - len(preset[0])) // 2

        # Ajouter le preset au centre
        if 0 <= preset_len_row < grid_len_row and 0 <= preset_len_col < grid_len_col:
            for row_offset, row in enumerate(preset):
                for col_offset, element in enumerate(row):
                    self.matrix[row_center + row_offset][col_center + col_offset] = element
        else:
            print("Indices invalides : ({}, {})".format(preset_len_row, preset_len_col))
            print("Taille écran : ")
            print("Taille cellule : ")

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
        # Créer une copie de la matrice actuelle
        next_state = [[0] * cols for _ in range(rows)]

        for row_id in range(rows):
            for col_id in range(cols):
                # Compter le nombre de voisins vivants
                living_neighbors = self.count_living_neighbors(row_id, col_id)

                # Appliquer les règles du jeu de la vie
                if self.matrix[row_id][col_id] == 1:  # Cellule vivante
                    if living_neighbors < 2 or living_neighbors > 3:
                        next_state[row_id][col_id] = 0  # Mort par sous-population ou surpopulation
                    else:
                        next_state[row_id][col_id] = 1  # Survie
                else:  # Cellule morte
                    if living_neighbors == 3:
                        next_state[row_id][col_id] = 1  # Naissance
                    else:
                        next_state[row_id][col_id] = 0  # Reste morte

        self.matrix = next_state

    def count_living_neighbors(self, row_id, col_id):
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
            # +1 voisin si dans la matrice
            if 0 <= row_neighbor < rows_len and 0 <= col_neighbor < cols_len:
                living_neighbors += self.matrix[row_neighbor][col_neighbor]

        return living_neighbors

    def __iter__(self):
        # Permet d'itérer sur les lignes de la grille
        return iter(self.matrix)
