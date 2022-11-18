import copy


def get_neighbours_cells(cell_position: (int, int)) -> list[(int, int)]:
    """Returns a list of the neighbours position (line, column) of a cell in
     this order in the list:
     [0, 1, 2]
     [3, X, 4]
     [5, 6, 7]
    """

    neighbours: list[(int, int)] = [0, 0] * 4

    neighbours[0] = cell_position[0] - 1, cell_position[1] - 1
    neighbours[1] = cell_position[0] - 1, cell_position[1]
    neighbours[2] = cell_position[0] - 1, cell_position[1] + 1

    neighbours[3] = cell_position[0], cell_position[1] - 1
    neighbours[4] = cell_position[0], cell_position[1] + 1

    neighbours[5] = cell_position[0] + 1, cell_position[1] - 1
    neighbours[6] = cell_position[0] + 1, cell_position[1]
    neighbours[7] = cell_position[0] + 1, cell_position[1] + 1

    return neighbours


def is_neighbour_valid(neighbour_position: (int, int),
                       max_position: int) -> bool:
    """Returns false if the neighbour is at a forbidden position"""

    if neighbour_position[0] <= -1 or neighbour_position[1] <= -1:
        return False

    if neighbour_position[0] >= max_position or \
            neighbour_position[1] >= max_position:
        return False

    return True


def get_number_of_alive_neighbours(cell_position: (int, int),
                                   state: list[list[int]]) -> int:
    """Returns the number of alive cells around a cell"""

    neighbours: list[(int, int)] = get_neighbours_cells(cell_position)
    alive_neighbours: int = 0

    # Look for the number of 1 in the neighbours of our cell
    for neighbour in neighbours:
        # Check if the neighbour exist
        if is_neighbour_valid(neighbour, len(state)):

            if state[neighbour[0]][neighbour[1]] == 1:
                alive_neighbours += 1

    return alive_neighbours


def get_next_state(state: list[list[int]]) -> list[list[int]]:
    """Updates the game state"""

    # Copy the state in our new state
    next_state: list[list[int]] = copy.deepcopy(state)

    # Checking each cell
    for line_index in range(len(state)):
        for column_index in range(len(state[line_index])):

            if state[line_index][column_index] == 1:
                # Check if the cell must die
                cell_position: (int, int) = line_index, column_index
                alive_neighbours: int = get_number_of_alive_neighbours(
                    cell_position, state)
                if alive_neighbours < 2 or alive_neighbours > 3:
                    # Destroy the cell in the next state
                    next_state[line_index][column_index] = 0
            else:
                # Check if a new cell must be born
                cell_position: (int, int) = line_index, column_index
                if get_number_of_alive_neighbours(cell_position, state) == 3:
                    # Create a cell in the next state
                    next_state[line_index][column_index] = 1

    return next_state
