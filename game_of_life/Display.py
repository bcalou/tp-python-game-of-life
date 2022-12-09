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
        self._real_window_size: tuple = (self._square_X_size * self._columns_quantity, self._square_Y_size * self._rows_quantity)
        self._time_between_frames: int = 160  # in ms
        self._current_time: int
        self._time_of_last_refresh: int = 0
        self._frequency: int = 1
        self._generation: int = 1
        self._current_state: Matrix = copy.deepcopy(self._game.get_initial_state())
        self._is_in_pause: bool = False
        self._done: bool = False
        self._init_pygame()
        self._main_loop()

    def _init_pygame(self):

        """Pygame library initialization and setting"""

        pygame.init()
        self._screen: pygame.surface.Surface = (
            pygame.display.set_mode(self._real_window_size)
        )
        pygame.display.set_caption(self._window_name)
        self._clock = pygame.time.Clock()
        self._clock.tick(60)
        self._font = pygame.font.SysFont("calibri", 50)
        # self._draw_grid()

    def _main_loop(self):

        """Method managing user events and content refreshing"""

        # While the game is not over
        while not self._done:

            # Listen for all events
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    # print(f"click {pygame.time.get_ticks()}")
                    self._change_state_of_cell()

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
            
            self._current_time =  pygame.time.get_ticks()

            if (self._current_time - self._time_of_last_refresh >= self._time_between_frames and
                not self._is_in_pause
            ):
                self._current_state = self._game.get_next_state(self._current_state)
                self._generation += 1
                self._time_of_last_refresh = pygame.time.get_ticks()

        print("See you !")
        pygame.quit()
    
    def _change_state_of_cell(self):
        mouse_pos: tuple = pygame.mouse.get_pos()
        cell_coord_X = mouse_pos[0] // self._square_X_size
        cell_coord_Y = mouse_pos[1] // self._square_Y_size
        self._current_state[cell_coord_Y][cell_coord_X] = not self._current_state[cell_coord_Y][cell_coord_X]

    def _increase_speed(self):

        """Increasing the speed of the game by changing the refresh rate"""

        if self._time_between_frames > 16:
            self._time_between_frames = self._time_between_frames // 2
        self._print_FPS()

    def _decrease_speed(self):

        """Decreasing the speed of the game by changing the refresh rate"""

        if self._time_between_frames < 1024:
            self._time_between_frames = self._time_between_frames * 2
        self._print_FPS()
    
    def _print_FPS(self):
        print(f'{1 / (self._time_between_frames / 1000)} FPS')

    def _toggle_pause_mode(self):
        self._is_in_pause = not self._is_in_pause

    def _display_current_state(self):

        """Waking through the whole matrix to draw each cell one by one"""
        
        for row in range(self._rows_quantity):
            for column in range(self._columns_quantity):
                if self._current_state[row][column] == 1:
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255)

                pygame.draw.rect(self._screen, color, (column * self._square_X_size, row * self._square_Y_size, self._square_X_size, self._square_Y_size))

        self._draw_grid()
        
        self._text = self._font.render(f'{self._generation}', True, (255, 0, 0))
        self._screen.blit(self._text, (0, 0))
        pygame.display.flip()
    
    def _draw_grid(self):
        color: tuple = (200, 200, 200)

        for row in range(self._game.get_rows_quantity() + 1):
            pygame.draw.line(self._screen, color, (0, row * self._square_X_size), (self._rows_quantity * self._square_X_size, row * self._square_X_size))
        
        for column in range(self._game.get_columns_quantity() + 1):
            pygame.draw.line(self._screen, color, (column * self._square_Y_size, 0), (column * self._square_Y_size, self._columns_quantity * self._square_Y_size))
