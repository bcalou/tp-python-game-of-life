import pygame

# Create own type of matrix
Matrix = list[list[int]]


class Game:
    '''Class to create the game of life'''

    def __init__(self,
                 state: Matrix,
                 display_size_x: int,
                 display_size_y: int,
                 death_cell_color: tuple,
                 alive_cell_color: tuple,
                 fps: int):
        '''constructor to initialize data'''

        # Initialize the first frame matrix
        self._state: Matrix = state

        # Initialize the framerate
        self._fps: int = fps

        # Define colors
        self._death_cell_color: tuple = death_cell_color
        self._alive_cell_color: tuple = alive_cell_color

        # Initialize the game window size
        self._display_size_x: int = display_size_x
        self._display_size_y: int = display_size_y

        # Initialize the cells size
        self._cell_size_x: int = int(display_size_x / len(self._state[0]))
        self._cell_size_y: int = int(display_size_y / len(self._state))

        # Setup pygame stuff
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._done: bool = True
        self._screen: pygame.surface.Surface

    def start(self):
        '''Public function to start the game'''

        print("The game starting.")

        self._done = False

        # Create the game window
        self._screen = pygame.display.set_mode(
            (self._display_size_x, self._display_size_y)
            )
        self._screen.fill(self._death_cell_color)

        pygame.init()
        self._update()

    def _update(self):
        '''Private function which display game for each frame '''

        # While the game is not over
        while not self._done:

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    self._done = True

            # For each iteration
            for index_line in range(len(self._state)):
                for index_column in range(len(self._state[index_line])):
                    if self._state[index_line][index_column] == 1:
                        # draw an alive cell
                        pygame.draw.rect(self._screen, self._alive_cell_color, (
                            index_column * self._cell_size_x,
                            index_line * self._cell_size_y,
                            self._cell_size_x, self._cell_size_y)
                            )
                    else:
                        # draw a death cell
                        pygame.draw.rect(self._screen, self._death_cell_color, (
                            index_column * self._cell_size_x,
                            index_line * self._cell_size_y,
                            self._cell_size_x,
                            self._cell_size_y)
                            )

            # Called at the end of each update. Allows to apply modifications
            pygame.display.flip()

            self._clock.tick(self._fps)
            self._state = self._get_next_state()

        pygame.quit()

    def _get_next_state(self) -> Matrix:
        '''Private function wich return the next state. Called every frame'''

        # Filled matrix with 0
        result_matrix: Matrix = [
            [0]*len(self._state) for i in range(len(self._state[0]))
            ]

        for index_line in range(len(self._state)):
            for index_column in range(len(self._state[index_line])):

                # Get number of alive neighbor cell
                number_neighbor: int = self._get_neighbour(index_line,
                                                           index_column)

                # A dead cell with exactly three living neighboring cells
                # becomes alive
                if number_neighbor == 3:
                    # Cell alive
                    result_matrix[index_line][index_column] = 1

                # A living cell with two or three living neighboring cells
                # remains
                elif number_neighbor == 2:
                    result_matrix[index_line][index_column] =\
                         self._state[index_line][index_column]

                # Otherwise it dies.
                elif number_neighbor < 2 or number_neighbor > 3:
                    # Cell death
                    result_matrix[index_line][index_column] = 0

        return result_matrix

    def _get_neighbour(self, index_line: int, index_column: int) -> int:
        '''Private function which return the number of alive neighbor cell'''

        number_neighbor: int = 0

        # Get neighbors cells by checking every time if they exist
        # top left cell
        if index_line > 0 and index_column > 0:
            if self._state[index_line - 1][index_column - 1] == 1:
                number_neighbor += 1
        # top cell
        if index_line > 0:
            if self._state[index_line - 1][index_column] == 1:
                number_neighbor += 1
        # top right cell
        if index_line > 0 and index_column < len(self._state[index_line]) - 1:
            if self._state[index_line - 1][index_column + 1] == 1:
                number_neighbor += 1

        # left cell
        if index_column > 0:
            if self._state[index_line][index_column - 1] == 1:
                number_neighbor += 1
        # right cell
        if index_column < len(self._state[index_line]) - 1:
            if self._state[index_line][index_column + 1] == 1:
                number_neighbor += 1

        # bottom left cell
        if index_line < len(self._state) - 1 and index_column > 0:
            if self._state[index_line + 1][index_column - 1] == 1:
                number_neighbor += 1
        # bottom cell
        if index_line < len(self._state) - 1:
            if self._state[index_line + 1][index_column] == 1:
                number_neighbor += 1
        # bottom right cell
        if index_line < len(self._state) - 1 and \
                index_column < len(self._state[index_line]) - 1:
            if self._state[index_line + 1][index_column + 1] == 1:
                number_neighbor += 1

        return number_neighbor
