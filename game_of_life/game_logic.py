"""Ce fichier contient les fonctions qui gèrent la logique du jeu de la vie.
"""


def get_next_state(grid: list[list[int]]) -> list[list[int]]:
    """Fonction qui calcule la génération suivante du jeu.
    """
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            new_grid[y][x] = is_alive(grid, x, y)

    return new_grid


def is_alive(grid: list[list[int]], x: int, y: int) -> int:
    """Fonction qui vérifie si une cellule sera vivante ou non.
    """
    neighbours = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if y + i < 0 or y + i >= len(grid):
                continue

            if x + j < 0 or x + j >= len(grid[0]):
                continue

            neighbours += grid[y + i][x + j]

    if grid[y][x] == 1:
        if neighbours < 2 or neighbours > 3:
            return 0  # Décès par solitude ou surpopulation

        return 1  # Survie

    elif neighbours == 3:
        return 1  # Naissance

    return 0  # Reste morte
