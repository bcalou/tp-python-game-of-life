import pygame

Matrix = list[list[int]]

class Game:

    def __init__(self, state: Matrix, display_size_x : int, display_size_y: int, death_cell_color: tuple, alive_cell_color: tuple, fps: int):
        
        self._state: Matrix = state

        self._fps: int = fps

        self._death_cell_color: tuple = death_cell_color
        self._alive_cell_color: tuple = alive_cell_color

        self._display_size_x: int = display_size_x
        self._display_size_y: int = display_size_y

        self._cell_size_x: int = int(display_size_x / len(self._state[0]))
        self._cell_size_y: int = int(display_size_y / len(self._state))

        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._done: bool = True
        self._screen: pygame.surface.Surface


    def start(self):
        print("The game starting.")
        
        self._done = False
        self._screen = pygame.display.set_mode((self._display_size_x, self._display_size_y))
        self._screen.fill(self._death_cell_color)

        pygame.init()
        self._update()


    def _update(self):

        # While the game is not over
        while not self._done:

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    self._done = True

            '''For each iteration'''
            for index_line in range(len(self._state)):
                for index_column in range(len(self._state[index_line])):
                    if self._state[index_line][index_column] == 1:
                        pygame.draw.rect(self._screen, self._alive_cell_color, (index_column * self._cell_size_x, index_line * self._cell_size_y, self._cell_size_x, self._cell_size_y)) #x, y, largeur, hauteur
                    else:
                        pygame.draw.rect(self._screen, self._death_cell_color, (index_column * self._cell_size_x, index_line * self._cell_size_y, self._cell_size_x, self._cell_size_y))

            '''Called at the end of each update. Allows to apply modifications'''
            pygame.display.flip()
            self._clock.tick(self._fps)
            self._state = self._get_next_state()

        pygame.quit()


    def _get_next_state(self) -> Matrix:

        #Filled matrix with 0
        result_matrix: Matrix = [[0]*len(self._state) for i in range(len(self._state[0]))] 

        for index_line in range(len(self._state)):
            for index_column in range(len(self._state[index_line])):

                number_neighbor: int = self._get_neighbour(index_line, index_column)
                
                #une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît)
                if number_neighbor == 3:
                    #Cell alive
                    result_matrix[index_line][index_column] = 1

                #une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.
                elif number_neighbor == 2:
                    result_matrix[index_line][index_column] = self._state[index_line][index_column]

                elif number_neighbor < 2 or number_neighbor > 3:
                    #Cell death
                    result_matrix[index_line][index_column] = 0
                
        return result_matrix


    def _get_neighbour(self, index_line: int, index_column: int) -> int:

        number_neighbor: int = 0

        '''Filter'''
        #Case en haut à gauche
        if index_line > 0 and index_column > 0:
            if self._state[index_line - 1][index_column - 1] == 1:
                number_neighbor += 1
        #Cause en haut
        if index_line > 0:
            if self._state[index_line - 1][index_column] == 1:
                number_neighbor += 1
        #Case en haut à droite
        if index_line > 0 and index_column < len(self._state[index_line]) - 1:
            if self._state[index_line - 1][index_column + 1] == 1:
                number_neighbor += 1

        #Case à gauche
        if index_column > 0:
            if self._state[index_line][index_column - 1] == 1:
                number_neighbor += 1                
        #Case à droite
        if index_column < len(self._state[index_line]) - 1:
            if self._state[index_line][index_column + 1] == 1:
                number_neighbor += 1
        
        #Case en bas à gauche
        if index_line < len(self._state) - 1 and index_column > 0:
            if self._state[index_line + 1][index_column - 1] == 1:
                number_neighbor += 1
        #Case en bas
        if index_line < len(self._state) - 1:
            if self._state[index_line + 1][index_column] == 1:
                number_neighbor += 1   
        #Case en bas à droite
        if index_line < len(self._state) - 1 and index_column < len(self._state[index_line]) - 1:
            if self._state[index_line + 1][index_column + 1] == 1:
                number_neighbor += 1

        return number_neighbor
