class MatrixManager():

    def __init__(self, width, height) -> None:
        '''
            Create an empty matrix.
        '''

        self.__width: int = width
        self.__height: int = height

        self.__matrix: list[list[int]] = []

        for i in range(height):
            self.__matrix.append([])

    def replace_matrix(self, matrix: list[list[int]]) -> None:
        '''
            Create a matrix filled from imbricated arrays (basically a copy).
        '''

        self.__width: int = len(matrix[0])
        self.__height: int = len(matrix)

        self.__matrix: list[list[int]] = matrix

    def get_cell(self, row: int, column: int) -> int:
        '''
            Fetch the element at given coordinates.
        '''

        return self.matrix[row][column]

    def get_matrix(self) -> list[list[int]]:
        '''
            Give the matrix stored.
        '''

        return self.__matrix

    def update_matrix(self) -> None:
        '''
            Update the stored matrix according to the game_of_life rules.
        '''

        new_matrix: list[list[int]] = []

        for i in range(len(self.__matrix)):
            # Browse through rows to generate copies with updated values

            row: list[int] = []

            for j in range(len(self.__matrix[i])):
                # Browse through columns and calculate rows updated values

                life_indicator: int = self.calculate_life_indicator(i, j)

                row.append(self.determine_fate(self.__matrix[i][j],
                                               life_indicator))

            new_matrix.append(row)

        self.__matrix = new_matrix

    def calculate_life_indicator(self, row: int, column: int) -> int:
        '''
            Will be useful to know if cell will live, spawn or die.
        '''

        life_indicator: int = 0

        for i in range(row - 1, row + 2):
            # Browse thrue row neighbours

            if (i < 0 or i >= self.__height):
                # except if they doesn't exists
                continue

            for j in range(column - 1, column + 2):
                # Browse thrue column neighbours

                if ((j == column and i == row) or j < 0 or j >= self.__width):
                    # except if they doesn't exists or
                    # the cell is browsing herself
                    continue

                life_indicator += self.__matrix[i][j]

        return life_indicator

    def determine_fate(self, cell_value: int, life_indicator: int) -> int:
        '''
            Kill, Spawn or let the cell in place
        '''

        if cell_value == 1:
            # if alive
            if life_indicator < 2 or life_indicator > 3:

                cell_value = 0

        else:
            # if ded
            if life_indicator == 3:

                cell_value = 1

        return cell_value
