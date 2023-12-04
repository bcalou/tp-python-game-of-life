import pygame
from game_of_life import const
from game_of_life.rendering import Renderer


class Game():
    """Represents an instance of the game of life"""
    state: list[list[int]]
    renderer: Renderer
    clock: pygame.time.Clock
    paused: bool = False

    def __init__(self, state: list[list[int]]) -> None:
        self.state = state
        self.clock = pygame.time.Clock()

        screen = pygame.display.set_mode(const.SCREEN_DIMENSIONS)
        self.renderer = Renderer(screen)

    def start(self) -> None:
        """Opens the game window and starts the game"""
        pygame.init()
        done: bool = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if not self.paused:
                self.state = self.__get_next_state(self.state)
                self.renderer.draw_game(self.state)
            self.clock.tick(const.FPS)

        pygame.quit()

    def __get_next_state(self, state: list[list[int]]) -> list[list[int]]:
        """Calculates the next state of the game"""
        # Initialize the new state var
        new_state: list[list[int]] = [[] for row in state]

        # Loop through all and calculate the new states
        for row_index in range(0, len(state)):
            for column_index in range(0, len(state[0])):
                new_state[row_index].append(self.__calc_cell_state(
                    (row_index, column_index), state
                ))

        return new_state

    def __calc_cell_state(self, cell_id: tuple, grid: list[list[int]]) -> int:
        """Calculates the next state of a cell given its neighbours"""
        neighbours: int = self.__calc_neighbours(cell_id, grid)

        # If cell is alive
        if grid[cell_id[0]][cell_id[1]] == 1:
            return 0 if neighbours < 2 or neighbours > 3 else 1
        else:
            return 0 if neighbours != 3 else 1

    def __calc_neighbours(self, cell_id: tuple, grid: list[list[int]]) -> int:
        """Calculates the number of alive neighbours of a cell"""
        neighbours: int = 0
        for direction in const.DIRECTIONS:
            # Coordinates of the neighbouring cell
            new_coordinates: tuple = (
                cell_id[0] + direction[0],
                cell_id[1] + direction[1]
            )

            # Check for out of bounds X
            if new_coordinates[0] < 0 or new_coordinates[0] >= len(grid[0]):
                continue

            # Check for out of bounds Y
            if new_coordinates[1] < 0 or new_coordinates[1] >= len(grid):
                continue

            neighbours += grid[new_coordinates[0]][new_coordinates[1]]

        return neighbours
