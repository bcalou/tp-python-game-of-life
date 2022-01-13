import copy


def count_neighbors(current_state: list[list[int]], x: int, y: int) -> int:
    count: int = 0
    for col in (-1, 0, 1):
        for line in (-1, 0, 1):
            if x+col >= 0 and x+col < len(current_state[0]) and y+line >= 0 and y+line < len(current_state) and (col != 0 or line != 0) and current_state[y+line][x+col] == 1:
                count += 1
    return count


def get_next_state(current_state: list[list[int]]) -> list[list[int]]:
    next_state: list[list[int]] = copy.deepcopy(current_state)
    for i in range(len(current_state)):
        for y in range(len(current_state[i])):
            cellsCount: int = count_neighbors(current_state, y, i)
            if cellsCount < 2 or cellsCount > 3:
                next_state[i][y] = 0
            elif cellsCount == 3:
                next_state[i][y] = 1
    return next_state
