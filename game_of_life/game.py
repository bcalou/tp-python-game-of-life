import copy

def count_neighbors(current_state: list[list[int]], x: int, y: int) -> int:
    count : int = 0
    for i in (-1, 0, 1): 
        for j in (-1, 0, 1):
            if x+i >= 0 and x+i < len(current_state[0]) and y+j >= 0 and y+j < len(current_state) and (i != 0 or j != 0) and current_state[y+j][x+i] == 1 :
                count += 1
    return count

def get_next_state(current_state: list[list[int]]) -> list[list[int]]:
    next_state: list[list[int]] = copy.deepcopy(current_state)
    for y in range(len(current_state)):
        for x in range(len(current_state[y])):
            cellsCount: int = count_neighbors(current_state, x, y)
            if cellsCount < 2 or cellsCount > 3:
                next_state[y][x] = 0
            elif cellsCount == 3:
                next_state[y][x] = 1
    return next_state