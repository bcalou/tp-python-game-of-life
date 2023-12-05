from copy import deepcopy
import pygame
import consts


x_size: float = consts.SCREEN_SIZE[0] / len(consts.INITIAL_STATE)
y_size: float = consts.SCREEN_SIZE[1] / len(consts.INITIAL_STATE[0])
current_state = deepcopy(consts.INITIAL_STATE)
new_state = deepcopy(consts.INITIAL_STATE)

def init_game_state():
    """init size with the initial state"""


def draw_game_state(screen: pygame.Surface):
    """draw game state on screen"""

    global current_state

    current_state = deepcopy(get_next_state())

    x_position: float = 0
    y_position: float = 0

    for line in current_state:
        for case in line:
            if case == 1:
                pygame.draw.rect(screen, (255, 255, 255),
                                (x_position, y_position, x_size, y_size))
            x_position += x_size
        x_position = 0
        y_position += y_size


def get_next_state() -> list[list[int]]:
    """Update state of the game killing or creating cells"""

    create_cell()
    kill_cell()

    return new_state


def create_cell():
    """create cell when 3 cells are around a case"""

    for line in range(len(current_state)):
        for case in range(len(current_state[line])):
            if neighbors_count(case, line) == 3:
                new_state[line][case] = 1


def kill_cell():
    """kill cell when more than 3 cells are around"""

    for line in range(len(current_state)):
        for case in range(len(current_state[line])):
            if neighbors_count(case, line) > 3 \
                or neighbors_count(case, line) <= 1:
                new_state[line][case] = 0


def neighbors_count(position_x: int, position_y: int) -> int:
    """return how many neihbors a case has"""

    neighbors: int = 0

    x: int = position_x - 1
    y: int = position_y - 1

    for i in range(3):
        for j in range(3):
            if (x + j != position_x or y + i != position_y) \
                and x + j >= 0 and y + i >= 0 \
                    and x + j < len(current_state[position_y]) \
                        and y + i < len(current_state) \
                            and current_state[y + i][x + j] == 1:
                neighbors += 1

    return neighbors
