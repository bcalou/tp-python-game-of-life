import copy

import pygame
from constants import *
from typing import TypedDict


class Position(TypedDict):
    x: int
    y: int


class Button:
    def __init__(self, text, position: Position, icon_path: str = None):
        self.text = text
        self.position = position
        self.rect = pygame.Rect(position['x'] - BUTTON_WIDTH // 2, position['y'] - BUTTON_HEIGHT // 2, BUTTON_WIDTH,
                                BUTTON_HEIGHT)
        self.icon_path = icon_path

        self.color = WHITE_COLOR

        # Load the icon image
        if self.icon_path:
            self.icon = pygame.image.load(icon_path)
            self.icon_rect = self.icon.get_rect(center=self.rect.center)

        self.hovered = False

    def is_hovered(self, mouse_position_x, mouse_position_y) -> bool:
        """
        Returns True if the mouse is hovering the button.

        :return: True if the mouse is hovering the button, False otherwise
        """
        return self.rect.collidepoint(mouse_position_x, mouse_position_y)

    def write_text_above_button(self, surface) -> None:
        """
        Writes the button text above the button.

        :param surface:
        :return: None
        """
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, WHITE_COLOR)
        text_rect = text_surface.get_rect(
            center=(self.rect.center[0], self.rect.center[1] - BUTTON_HEIGHT // 2 - 15))
        surface.blit(text_surface, text_rect)

    def update_icon(self, new_icon_path: str) -> None:
        """
        Updates the icon of the button.

        :return: None
        """
        self.icon = pygame.image.load(new_icon_path)
        self.icon_rect = self.icon.get_rect(center=self.rect.center)


class GridManager:
    def __init__(self, initial_grid: grid_type):
        self.grid = initial_grid
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 48)
        self.history = [copy.deepcopy(initial_grid)]

        pygame.display.set_caption("Game of Life")

        self.pause_button = Button("Pause", Position(x=PAUSE_BUTTON_POSITION_WIDTH, y=BUTTON_POSITION_HEIGHT),
                                   "icons/pause_button.png")

        self.step_forward_button = Button("Step forward", Position(x=self.pause_button.position['x'] + BUTTON_WIDTH,
                                                                   y=BUTTON_POSITION_HEIGHT),
                                          "icons/step_forward_button.png")

        self.step_back_button = Button("Step back", Position(x=self.pause_button.position['x'] - BUTTON_WIDTH,
                                                             y=BUTTON_POSITION_HEIGHT),
                                       "icons/step_backward_button.png")

        self.reset_button = Button("Reset", Position(x=self.step_back_button.position['x'] - BUTTON_WIDTH,
                                                     y=BUTTON_POSITION_HEIGHT),
                                   "icons/reset_button.png")

        self.buttons = [self.pause_button, self.step_forward_button, self.step_back_button,
                        self.reset_button]

    def set_next_grid(self) -> None:
        """
        Sets the next grid according to the rules of John Conway's Game of Life.

        - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        - Any live cell with two or three live neighbours lives on to the next generation.
        - Any live cell with more than three live neighbours dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


        :return: None
        """
        self.history.append(copy.deepcopy(self.grid))
        next_grid = copy.deepcopy(self.grid)

        for row_index, row in enumerate(self.grid):
            for cell_index in range(len(row)):
                next_grid[row_index][cell_index] = self.__get_next_cell_state(row_index, cell_index)

        if len(self.history) > MAX_HISTORY_SIZE:
            del self.history[0]

        self.grid = next_grid

    def step_back(self) -> None:
        """
        Sets the grid to the previous state.

        :return: None
        """
        if len(self.history) > 0:
            self.grid = self.history.pop()

    def __get_next_cell_state(self, row_index: int, cell_index: int) -> int:
        """
        Returns the next state of the given cell according to the rules of John Conway's Game of Life :

        :param row_index: Height index of the cell
        :param cell_index: Width index of the cell
        :return: The next state of the cell (0 : dead or 1 : alive)
        """
        cell = self.grid[row_index][cell_index]
        neighbors = self.__get_neighbors(row_index, cell_index)

        if cell is ALIVE and (neighbors < 2 or neighbors > 3):
            return DEAD
        elif cell is DEAD and neighbors == 3:
            return ALIVE

        return cell

    def __get_neighbors(self, row_index: int, cell_index: int) -> int:
        """
        Returns the number of neighbors of the given cell.

        :param row_index: Height index of the cell
        :param cell_index: Width index of the cell
        :return:
        """
        neighbors = 0

        for neighbor in NEIGHBORS:
            try:
                if self.grid[row_index + neighbor[0]][cell_index + neighbor[1]] == 1:
                    neighbors += 1
            except IndexError:
                pass

        return neighbors

    def draw_grid(self, generation: int) -> None:
        """
        Draws the current grid.

        :return: None
        """

        # Fill the screen with black
        self.screen.fill(BLACK_COLOR)

        # Draw the generation number
        generation_text = self.font.render(f"Generation : {generation}", True, WHITE_COLOR)
        self.screen.blit(generation_text, (10, 10))

        for button in self.buttons:
            if button.is_hovered(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                button.color = GREY_COLOR
                button.write_text_above_button(self.screen)
                button.hovered = True
            else:
                button.color = WHITE_COLOR
                button.hovered = False

            self.__draw_button(button)

        # Calculate the starting position of the grid
        starting_position = (SCREEN_WIDTH // 2 - len(self.grid[0]) * CELL_SIZE // 2,
                             SCREEN_HEIGHT // 2 - len(self.grid) * CELL_SIZE // 2)

        # Draw the grid in the center of the screen
        for row_index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell is ALIVE:
                    pygame.draw.rect(self.screen, WHITE_COLOR,
                                     (starting_position[0] + cell_index * CELL_SIZE,
                                      starting_position[1] + row_index * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

    def __draw_button(self, button: Button) -> None:
        """
        Draws the given button.

        :param button: The button to draw
        :return: None
        """
        # Draw the button background
        pygame.draw.rect(self.screen, button.color, button.rect)

        # Draw the button icon
        if button.icon_path:
            self.screen.blit(button.icon, button.icon_rect)

        else:
            text = self.font.render(button.text, True, BLACK_COLOR)
            self.screen.blit(text, (button.position['x'] - text.get_width() // 2,
                                    button.position['y'] - text.get_height() // 2))

    def get_grid(self) -> grid_type:
        """
        Returns the current grid.

        :return: The current grid
        """
        return self.grid

    def set_grid(self, grid: grid_type) -> None:
        """
        Sets the current grid.

        :param grid: The new grid
        :return: None
        """
        self.grid = grid
