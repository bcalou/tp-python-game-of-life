import pygame
from game_of_life import const, array2d
from game_of_life.rendering import Renderer


class Game():
    """Represents an instance of the game of life"""
    state: array2d
    renderer: Renderer
    clock: pygame.time.Clock
    paused: bool = False

    def __init__(self, state: array2d) -> None:
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
                self.perform_game_tick()
            self.clock.tick(const.FPS)

        pygame.quit()

    def perform_game_tick(self) -> None:
        """
        Performs a game tick and renders it.
        """
        # Initialize the new state var
        new_state: array2d = [[] for row in self.state]

        self.renderer.clear()

        # Loop through all and calculate the new states
        for row_index in range(0, len(self.state)):
            for column_index in range(0, len(self.state[0])):
                new_cell_state: int = self.__update_cell_state(
                    (row_index, column_index), self.state
                )

                new_state[row_index].append(new_cell_state)
                if (new_cell_state == 1):
                    self.renderer.draw_cell(column_index, row_index)

        self.renderer.update()
        self.state = new_state

    def __update_cell_state(self, cell_id: tuple, grid: array2d) -> int:
        """
        Updates the next state of a cell given its neighbours
        A live cell remains alive if it has 2-3 neighbours and dies otherwise.
        A dead cell becomes alive if it has exactly 3 neighbours.
        """
        neighbours: int = self.__get_neighbour_count(cell_id, grid)

        # If cell is alive
        if grid[cell_id[0]][cell_id[1]] == 1:
            return 0 if neighbours < 2 or neighbours > 3 else 1
        else:
            return 0 if neighbours != 3 else 1

    def __get_neighbour_count(self, cell_id: tuple, grid: array2d) -> int:
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
