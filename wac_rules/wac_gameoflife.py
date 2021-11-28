from random import randint

#return if cube is alive in function of its neighbours
def behaviour_cell(alive, neighbours):
    return neighbours == 3 or (alive and neighbours == 2)

#count neighbours around a cube
def count_neighbours(grid, position):
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
def behaviour(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if behaviour_cell(cell, neighbours) else 0
    return new_grid
