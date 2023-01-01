import pygame
import copy

Matrix = list[list[int]]


simple_matrix_world: Matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]
# TODO CREATE MATRIX CLASS


class GriddWorld():
    def __init__(self, world_matrix: Matrix) -> None:
        self._world_matrix: Matrix = copy.deepcopy(world_matrix)
        self._world_size_x = len(world_matrix[0])
        self._world_size_y = len(world_matrix)

    def get_cell_value_at(self, pos_x: int, pos_y: int) -> int:
        if not self.check_position_validity(pos_x, pos_y):
            return 0
        return self._world_matrix[pos_y][pos_x]

    def set_cell_value_at(self, value: int, pos_x: int, pos_y: int):
        if not self.check_position_validity(pos_x, pos_y):
            return
        self._world_matrix[pos_y][pos_x] = value

    def check_position_validity(self, pos_x: int, pos_y: int) -> bool:
        is_pos_x_valid: bool = (pos_x >= 0 and pos_x < self._world_size_x)
        is_pos_y_valid: bool = (pos_y >= 0 and pos_y < self._world_size_y)
        return is_pos_x_valid and is_pos_y_valid

    def get_world_size_x(self):
        return self._world_size_x

    def get_world_size_y(self):
        return self._world_size_y


class WorldSolver():
    def __init__(self, world: GriddWorld) -> None:
        self.world: GriddWorld = world
