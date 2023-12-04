from game_of_life.get_neighbours_count import get_neighbours_count


def get_next_state(current_state: list[list[int]]) -> list[list[int]]:

    next_state: list[list[int]] = []
    for y, row in enumerate(current_state):
        new_row: list[int] = []
        for x, cell in enumerate(row):
            neighbour_count: int = get_neighbours_count(current_state, x, y)
            if neighbour_count == 3:
                new_row.append(1)
            elif neighbour_count == 2:
                new_row.append(current_state[y][x])
            else:
                new_row.append(0)
        next_state.append(new_row)

    return next_state