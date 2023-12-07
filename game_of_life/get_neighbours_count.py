def get_neighbours_count(state: list[list[int]], x: int, y: int) -> int:
    """
    Count the number of neighbour of a cell
    """

    count: int = 0

    heigh: int = len(state)
    width: int = len(state[0])

    x_coords: list[int] = [x-1, x,  x+1]
    y_coords: list[int] = [y-1, y, y+1]

    for neighbour_x in x_coords:
        for neighbour_y in y_coords:
            if neighbour_x is not x or neighbour_y is not y:
                if (neighbour_x >= 0 and neighbour_x < width
                   and neighbour_y >= 0 and neighbour_y < heigh):
                    # print(f"{x}/{y} : {neighbour_x}/{neighbour_y} \
                    # ({state[neighbour_x][neighbour_y]})")
                    count += state[neighbour_y][neighbour_x]

    return count
