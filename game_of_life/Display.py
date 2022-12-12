import pygame
import copy
from game_of_life.params import *
from game_of_life.Game import Game


class Display:

    """Class managing the display of the game thanks to the pygame library"""

    def __init__(self, window_size: tuple, current_game: Game):
        self._game: Game = current_game
        self._wanted_window_size: tuple = window_size
        self._window_name: str = "Game of life"
        self._rows_quantity: int = self._game.get_rows_quantity()
        self._columns_quantity: int = self._game.get_columns_quantity()
        self._square_X_size: int = self._wanted_window_size[0] // self._columns_quantity
        self._square_Y_size: int = self._wanted_window_size[1] // self._rows_quantity
        self._real_window_size: tuple = (
            self._square_X_size * self._columns_quantity,
            self._square_Y_size * self._rows_quantity
        )
        self._current_time: int
        self._time_of_last_refresh: int = 0
        self._fps: float = 2
        self._generation: int = 1
        self._current_state: Matrix = copy.deepcopy(self._game.get_initial_state())
        self._is_in_pause: bool = False
        self._done: bool = False

    def init_pygame(self):

        """Pygame library initialization and setting"""

        pygame.init()
        self._screen: pygame.surface.Surface = (
            pygame.display.set_mode(self._real_window_size)
        )
        pygame.display.set_caption(self._window_name)
        self._clock = pygame.time.Clock()
        self._clock.tick(60)
        self._font = pygame.font.SysFont("calibri", 50)

    def display(self):

        """Method managing user events and content refreshing"""

        # While the game is not over
        while not self._done:

            # Listen for all events
            for event in pygame.event.get():

                # Mouse events
                if (
                    event.type == pygame.MOUSEBUTTONDOWN and
                    pygame.mouse.get_pressed()[0]
                ):
                    self._change_state_of_cell()

                # Keyboard events
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self._increase_speed()

                    elif event.key == pygame.K_DOWN:
                        self._decrease_speed()

                    elif event.key == pygame.K_SPACE:
                        self._toggle_pause_mode()

                # Quit the infinite loop when the user presses the close button
                elif event.type == pygame.QUIT:
                    self._done = True

            self._display_current_state()

            # Check if delta time between each frame has elapsed and then
            # compute next state of cells
            self._current_time = pygame.time.get_ticks()

            if (
                self._current_time - self._time_of_last_refresh >= (1 / self._fps) * 1000 and
                not self._is_in_pause
            ):
                self._current_state = self._game.get_next_state(self._current_state)
                self._generation += 1
                self._time_of_last_refresh = pygame.time.get_ticks()

        # Be nice
        print("See you !")
        pygame.quit()

    def _change_state_of_cell(self):

        """Changing the state of the cell when cliked by user"""

        mouse_pos: tuple = pygame.mouse.get_pos()
        cell_coord_X = mouse_pos[0] // self._square_X_size
        cell_coord_Y = mouse_pos[1] // self._square_Y_size
        self._current_state[cell_coord_Y][cell_coord_X] = (
            not self._current_state[cell_coord_Y][cell_coord_X]
        )

    def _increase_speed(self):

        """Increasing the speed of the game by changing the refresh rate"""

        if self._fps < 256:
            self._fps = self._fps * 2
        self._print_FPS()

    def _decrease_speed(self):

        """Decreasing the speed of the game by changing the refresh rate"""

        if self._fps > 0.5:
            self._fps = self._fps / 2
        self._print_FPS()

    def _print_FPS(self):

        """Printing FPS in the console"""

        print(f'{self._fps} FPS')

    def _toggle_pause_mode(self):

        """Toggling the variable managing the pause mode"""

        self._is_in_pause = not self._is_in_pause

    def _display_current_state(self):

        """Waking through the whole matrix to draw each cell one by one"""

        # Drawing squares with the corresponding color
        for row in range(self._rows_quantity):
            for column in range(self._columns_quantity):
                cell_color: tuple = (0, 0, 0) if self._current_state[row][column] == 1 else (255, 255, 255)
                x_coord: int = column * self._square_X_size
                y_coord: int = row * self._square_Y_size
                pygame.draw.rect(
                    self._screen,
                    cell_color,
                    (x_coord, y_coord, self._square_X_size, self._square_Y_size)
                )

        self._draw_grid()

        # Displaying the FPS in the upper left corner
        self._text = self._font.render(f'{self._generation}', True, (255, 0, 0))
        self._screen.blit(self._text, (0, 0))

        # Refreshing the display
        pygame.display.flip()

    def _draw_grid(self):

        """Drawing the grid for a better visibility of the cells and patterns"""

        grid_color: tuple = (200, 200, 200)

        # Drawing columns
        for column in range(self._columns_quantity + 1):
            pygame.draw.line(
                self._screen,
                grid_color,
                (column * self._square_X_size, 0),
                (column * self._square_X_size, self._real_window_size[1])
            )

        # Drawing rows
        for row in range(self._rows_quantity + 1):
            pygame.draw.line(
                self._screen,
                grid_color,
                (0, row * self._square_Y_size),
                (self._real_window_size[0], row * self._square_Y_size)
            )
