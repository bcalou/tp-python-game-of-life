import pygame
from game_of_life.Matrix_State import Matrix_State, MINIMUM_CELL_LENGTH, \
    SCREEN_WIDTH, SCREEN_HEIGHT

COLOR: int = 255
BORDER_COUNT: int = 4
DEFAULT_TICK: int = 60
COLOR_BLACK: tuple[int, int, int] = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Display:

    __matrix: Matrix_State

    def __init__(self, clock_tick: int = DEFAULT_TICK):
        """You can set the number of frames to refresh the game"""
        self.__clock_tick = clock_tick
        self.update()

    def update(self) -> None:
        """We use pygame for create and modify a window"""

        # We initiate all variable we need
        pygame.init()
        clock = pygame.time.Clock()
        done = False
        self.__matrix = Matrix_State()

        # While the game is not over
        while not done:

            # We choose the state of the grid
            self.__matrix.state_choose()

            # We change visual of game
            self.change_visual()

            # We modify the matrix every tick
            clock.tick(self.__clock_tick)

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    done = True

        pygame.quit()

    def change_visual(self) -> None:
        """We clear screen and draw a new screen"""

        # We clear and we draw
        screen.fill(COLOR_BLACK)
        self.draw_on_screen(self.__matrix.get_state())

        # We need to flip pygame for making change effective
        pygame.display.flip()

    def draw_on_screen(self, state: list[list[int]]) -> None:
        """We draw screen cell by cell"""

        # We draw every cell in state with two loop
        for tab_index, tab in enumerate(state):
            for element_index, element in enumerate(tab):

                # We draw cell color
                self.draw_cell(element * COLOR,
                               element_index * MINIMUM_CELL_LENGTH + 1,
                               tab_index * MINIMUM_CELL_LENGTH + 1,
                               MINIMUM_CELL_LENGTH - 2,
                               MINIMUM_CELL_LENGTH - 2)

                # We define borders of cell
                self.draw_border(element, element_index, tab_index)

    def draw_border(self, element: int, element_index: int, tab_index: int):
        """We  draw all border of cell and
        we define for all border each parameter"""

        # First Color is opposed of color cell
        color = ((element+1) % 2) * COLOR

        # Position of border will be in two case on four
        # the up left corner drawing go right or down
        position_x = element_index * MINIMUM_CELL_LENGTH
        position_y = tab_index * MINIMUM_CELL_LENGTH

        # We make a loop for draw each border of cell
        for increment in range(BORDER_COUNT):

            # We decide if border is made in height or width
            # by define the size of area draw
            size_x, size_y = MINIMUM_CELL_LENGTH if increment % 2 == 0\
                else 1, MINIMUM_CELL_LENGTH if increment % 2 == 1 else 1

            # In the two other case we define it at up right corner to go down
            # or at down left corner to go right
            if (increment == 2):
                position_y = (tab_index + 1) \
                    * MINIMUM_CELL_LENGTH - 1
            if (increment == 3):
                position_x = (element_index + 1) \
                    * MINIMUM_CELL_LENGTH - 12

            # Then we call draw_cell function with all modification
            self.draw_cell(color, position_x, position_y,
                           size_x, size_y)

    def draw_cell(self, color: int, position_x: int, position_y: int,
                  size_x: int, size_y: int) -> None:
        """We draw a rect  with color, place and size of rect"""

        pygame.draw.rect(screen, (color, color, color),
                         (position_x, position_y, size_x, size_y))
