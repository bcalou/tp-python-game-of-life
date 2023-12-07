def get_next_state(current_state: list[list[int]]) -> list[list[int]]:
    """Donne le prochain état de la matrice donnée"""

    rows = len(current_state)
    cols = len(current_state[0])

    # Créer une copie de la matrice actuelle
    next_state = [[0] * cols for _ in range(rows)]

    for row_id in range(rows):
        for col_id in range(cols):
            # Compter le nombre de voisins vivants
            living_neighbors = __count_living_neighbors(current_state, row_id, col_id)

            # Appliquer les règles du jeu de la vie
            if current_state[row_id][col_id] == 1:  # Cellule vivante
                if living_neighbors < 2 or living_neighbors > 3:
                    next_state[row_id][col_id] = 0  # Mort par sous-population ou surpopulation
                else:
                    next_state[row_id][col_id] = 1  # Survie
            else:  # Cellule morte
                if living_neighbors == 3:
                    next_state[row_id][col_id] = 1  # Naissance
                else:
                    next_state[row_id][col_id] = 0  # Reste morte

    return next_state

def __count_living_neighbors(current_state, row_id, col_id):
    """Donne le nombre de voisins d'une cellule"""

    rows_len = len(current_state)
    cols_len = len(current_state[0])
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
            living_neighbors += current_state[row_neighbor][col_neighbor]

    return living_neighbors
