import random

def rlint(size: int) -> list[int]:
    return [random.randint(0, 1) for _ in range(size)]

def generate_random_state(width: int, height: int) -> list[list[int]]:
    return [rlint(width) for _ in range(height)]

class GameOfLife:

    def __init__(self, initial_state: list[list[int]]) -> None:
        self.__width: int = len(initial_state[0])
        self.__height: int = len(initial_state)
        self.__state: list[list[int]] = initial_state

    
    def next_state(self) -> None:

        next_state: list[list[int]] = []
        for y, row in enumerate(self.__state):
            new_row: list[int] = []
            for x, cell in enumerate(row):
                neighbour_count: int = self.__get_neighbours_count(x, y)
                if neighbour_count == 3:
                    new_row.append(1)
                elif neighbour_count == 2:
                    new_row.append(self.__state[y][x])
                else:
                    new_row.append(0)
            next_state.append(new_row)

        self.__state = next_state

    def __get_neighbours_count(self, x: int, y: int) -> int:
        count: int = 0

        x_coords: list[int] = [x-1, x,  x+1]
        y_coords: list[int] = [y-1, y, y+1]

        for neighbour_x in x_coords:
            for neighbour_y in y_coords:
                if neighbour_x is not x or neighbour_y is not y:
                    if (neighbour_x >= 0 and neighbour_x < self.__width
                    and neighbour_y >= 0 and neighbour_y < self.__height):
                        # print(f"{x}/{y} : {neighbour_x}/{neighbour_y} ({state[neighbour_x][neighbour_y]})")
                        count += self.__state[neighbour_y][neighbour_x]

        return count

    def get_cell(self, x: int, y: int) -> int:
        return self.__state[y][x]
    
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height