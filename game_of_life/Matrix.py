from game_of_life.Consts import maTrix


class MatrixManager():

    def __init__(self, matrix: maTrix) -> None:
        '''
            Create a matrix filled from imbricated arrays (basically a copy).
        '''

        self.__width: int = len(matrix[0])
        self.__height: int = len(matrix)

        self.__matrix: maTrix = matrix

    def replace_matrix(self, matrix: maTrix) -> None:
        '''
            Create a matrix filled from imbricated arrays (basically a copy).
        '''

        self.__width: int = len(matrix[0])
        self.__height: int = len(matrix)

        self.__matrix: maTrix = matrix

    def get_cell(self, row: int, column: int) -> int:
        '''
            Fetch the element at given coordinates.
        '''

        return self.matrix[row][column]

    def get_matrix(self) -> maTrix:
        '''
            Give the matrix stored.
        '''

        return self.__matrix

    def update_matrix(self) -> None:
        '''
            Update the stored matrix according to the game_of_life rules.
        '''

        new_matrix: maTrix = []

        for i in range(len(self.__matrix)):
            # Browse through rows to generate copies with updated values

            updated_row: list[int] = []

            for j in range(len(self.__matrix[i])):
                # Browse through columns and calculate rows updated values

                alive_neighbours: int = self.get_alive_neighbours(i, j)

                updated_value: int = self.determine_fate(self.__matrix[i][j],
                                                         alive_neighbours)
                updated_row.append(updated_value)

            new_matrix.append(updated_row)

        self.__matrix = new_matrix

    def get_alive_neighbours(self, row: int, column: int) -> int:
        '''
            Get alive neighbours to determine the fate of the cell.
        '''

        alive_neighbours_count: int = 0

        for i in range(row - 1, row + 2):
            # Browse through row neighbours

            if (i < 0 or i >= self.__height):
                # except if they doesn't exists
                continue

            for j in range(column - 1, column + 2):
                # Browse through column neighbours

                if ((j == column and i == row) or j < 0 or j >= self.__width):
                    # except if they doesn't exists or
                    # the cell is browsing itself
                    continue

                alive_neighbours_count += self.__matrix[i][j]

        return alive_neighbours_count

    def determine_fate(self, cell_value: int, alive_neighbours: int) -> int:
        '''
            Kill, Spawn or let the cell in place
        '''

        if cell_value == 1:
            # if alive
            if alive_neighbours < 2 or alive_neighbours > 3:

                return 0

        else:
            # if ded
            if alive_neighbours == 3:

                return 1

        return cell_value
