import pygame
import copy
import world


Matrix = list[list[int]]


class GriddWorld():
    def __init__(self, world_matrix: Matrix) -> None:
        self._world_matrix: Matrix = copy.deepcopy(world_matrix)
        self._world_size_x = len(world_matrix[0])
        self._world_size_y = len(world_matrix)

    def get_cell_value_at(self, pos_x: int, pos_y: int) -> int:
        if not self.check_position_validity(pos_x, pos_y):
            return 0
        return self._world_matrix[pos_x][pos_y]

    def set_cell_value_at(self, value: int, pos_x: int, pos_y: int) -> None:
        if not self.check_position_validity(pos_x, pos_y):
            return
        self._world_matrix[pos_x][pos_y] = value

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
        # Generate an empty matrix template of the size of the current matrix to
        self.empty_matrix = [[0 for i in range(0, self.world.get_world_size_x())] for i in range(
            0, self.world.get_world_size_x())]

    def solve_step(self):
        next_step_world: GriddWorld = GriddWorld(self.empty_matrix)
        print("Begin solve step")
        for current_cell_pos_y in range(self.world.get_world_size_y()):
            for current_cell_pos_x in range(self.world.get_world_size_x()):
                total: int = self.get_number_of_living_neighboring_cells(
                    current_cell_pos_x, current_cell_pos_y)

                if total == 3:
                    next_step_world.set_cell_value_at(
                        1, current_cell_pos_x, current_cell_pos_y)

                if total > 3 or total < 2:
                    next_step_world.set_cell_value_at(
                        0, current_cell_pos_x, current_cell_pos_y)
        print("End solve step")
        self.world = copy.deepcopy(next_step_world)

    def get_number_of_living_neighboring_cells(self, pos_x: int, pos_y: int) -> int:
        total: int = 0
        # Go thru the cells in the range one of the current cells
        for offset_x in range(-1, 2):
            for offset_y in range(-1, 2):
                # Dont add the current cell value, only its neighboring cells values
                if offset_y == 0 and offset_x == 0:
                    continue

                # Current neighbor cell position
                neighbor_pos_x = pos_x + offset_x
                neighbor_pos_y = pos_y + offset_y

                # Check if the neighboring cell exist
                if ((neighbor_pos_x < 0 or neighbor_pos_x >= self.world.get_world_size_x())
                        or (neighbor_pos_y < 0 or neighbor_pos_y >= self.world.get_world_size_y())):
                    continue
                # Add the current neighbour cell value
                total += self.world.get_cell_value_at(neighbor_pos_x,
                                                      neighbor_pos_y)
        return total


def draw_world(world: GriddWorld, screen: pygame.Surface):
    """Function that draw a matrix of black or white rectangles depending on the value of the passed matrix"""
    screen_size_x, screen_size_y = pygame.display.get_window_size()
    cell_size_x = screen_size_x // world.get_world_size_x()
    cell_size_y = screen_size_y // world.get_world_size_y()
    for x in range(world.get_world_size_x()):
        for y in range(world.get_world_size_y()):
            pixel_value = 255 if world.get_cell_value_at(
                y, x) == 1 else 0  # TODO Check if x and y should be swapped
            pygame.draw.rect(screen, (pixel_value, pixel_value, pixel_value), (cell_size_x*y,
                             cell_size_y*x, cell_size_x*(y+1), cell_size_y*(x+1)))


def main():
    pygame.init()
    clock = pygame.time.Clock()

    done: bool = False

    CELL_SIZE = 30

    USE_SIMPLE_MATRIX: bool = False
    current_matrix: Matrix

    if USE_SIMPLE_MATRIX:
        current_matrix = world.simple_matrix_world
    else:
        current_matrix = world.current_matrix_world

    current_world: GriddWorld = GriddWorld(current_matrix)

    solver = WorldSolver(current_world)

    screen: pygame.surface.Surface = pygame.display.set_mode(
        (current_world.get_world_size_x()*CELL_SIZE, current_world.get_world_size_y()*CELL_SIZE))

    print(current_world.get_world_size_x()*CELL_SIZE,
          " X ", current_world.get_world_size_y()*CELL_SIZE,)
    # While the game is not over
    while not done:
        screen.fill((0, 0, 0))
        # Draw the matrix
        draw_world(solver.world, screen)  # type: ignore
        # Solve for the next state
        solver.solve_step()
        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True
        clock.tick(0)
        pygame.display.flip()

    pygame.quit()


    # Using the special variable
    # __name__
if __name__ == "__main__":
    main()
