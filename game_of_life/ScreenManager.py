import pygame
from game_of_life.Consts import Enums


class ScreenManager():

    def __init__(self, width: int, height: int, fps: int = 10) -> None:
        '''
            Create a new window for the game to run and launch it
        '''

        pygame.init()

        self.__screen: pygame.Surface = pygame.display.set_mode(
            (width, height))
        self.__clock: pygame.time.Clock = pygame.time.Clock()
        self.__FPS: int = fps

    def wants_to_quit(self) -> bool:
        '''
            Check if the user want to quit the game.
        '''

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return True

        return False

    def refresh_view(self, matrix: list[list[int]]) -> None:
        '''
            Update the game view for each frame.
        '''

        self.__screen.fill((0, 0, 0))

        self.draw_cells(matrix)

        pygame.display.flip()

        self.__clock.tick(self.__FPS)

    def draw_cells(self, matrix: list[list[int]]) -> None:
        '''
            Draw each cells of the matrix given in the right size at the 
            right posisition
        '''
        x_size: int = self.__screen.get_width() / len(matrix[0])
        y_size: int = self.__screen.get_width() / len(matrix)

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                color = 255 if matrix[i][j] == 1 else 0

                x_pos: int = j * x_size
                y_pos: int = i * y_size

                pygame.draw.rect(
                    self.__screen,
                    (color, color, color),
                    (x_pos + 0.5, y_pos + 0.5, x_size - 1, y_size - 1))

    def quit(self) -> None:
        '''
            Just quit the game.
        '''

        pygame.quit()
