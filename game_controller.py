import pygame
from grid_manager import GridManager, grid_type
from constants import *


class GameController:
    def __init__(self, initial_grid: grid_type):
        self.paused = False
        self.generation = 0
        self.done = False
        self.initial_grid = initial_grid
        pygame.init()
        self.grid_manager = GridManager(initial_grid)

    def game_routine(self):

        clock = pygame.time.Clock()

        # Draw the initial state
        self.grid_manager.draw_grid(self.generation)

        # While the game is not over
        while not self.done:
            self.__input_handler()

            self.grid_manager.draw_grid(self.generation)

            clock.tick(30)

            if self.paused:
                continue

            # Update the grid
            self.grid_manager.set_next_grid()

            self.generation += 1

        pygame.quit()

    def __input_handler(self):
        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                self.done = True

            # Check if buttons are clicked
            for button in self.grid_manager.buttons:
                if button.hovered:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        match button.text:
                            case "Pause":
                                button.text = "Play"
                                self.paused = True
                                button.update_icon("icons/play_button.png")
                            case "Play":
                                button.text = "Pause"
                                self.paused = False
                                button.update_icon("icons/pause_button.png")
                            case "Reset":
                                self.grid_manager.grid = self.initial_grid
                                self.generation = 0
                            case "Step forward":
                                self.grid_manager.set_next_grid()
                                self.generation += 1
                                self.grid_manager.draw_grid(self.generation)
                            case "Step back":
                                if self.generation > 0:
                                    self.generation -= 1
                                    self.grid_manager.step_back()
                                    self.grid_manager.draw_grid(self.generation)
