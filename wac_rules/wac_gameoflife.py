from random import randint

#return if cube is alive in function of its neighbours
def behaviour_cell(alive, neighbours) -> bool:
    return neighbours == 3 or (alive and neighbours == 2)

#count neighbours around a cube
def count_neighbours(grid: list[list[int]], position) -> int:
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count

#make grid empty
def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

#make a random grid
def make_random_grid(x, y):
        grid = []
        for r in range(x):
            row = []
            for c in range(y):
                row.append(randint(0,1))
            grid.append(row)
        return grid


#return a new grid in function of the current situation
def get_next_state(grid : list[list[int]]) -> list[list[int]]:
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for rows in range(x):
        for col in range(y):
            cell = grid[rows][col]
            neighbours = count_neighbours(grid, (rows, col))
            new_grid[rows][col] = 1 if behaviour_cell(cell, neighbours) else 0
    return new_grid
