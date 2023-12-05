import pygame
import consts


x_size: float = consts.SCREEN_SIZE[0] / len(consts.INITIAL_STATE)
y_size: float = consts.SCREEN_SIZE[1] / len(consts.INITIAL_STATE[0])
current_state = consts.INITIAL_STATE
new_state = consts.INITIAL_STATE

def init_game_state():
    """init size with the initial state"""


def draw_game_state(screen: pygame.Surface):
    """draw game state on screen"""

    update_game()

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

def update_game():
    """Update state of the game killing or creating cells"""

    # create_cell()
    kill_cell()

    current_state = new_state


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
            if neighbors_count(case, line) > 3:
                new_state[line][case] = 0


def neighbors_count(x: int, y: int) -> int:
    """return how many neihbors a case has"""

    neighbors: int = 0

    if x > 0 :
        if current_state[y][x - 1] == 1:
            neighbors +=1
        if y < len(current_state) - 1:
            if current_state[y + 1][x - 0] == 1:
                neighbors +=1
        if y > 0:
            if current_state[y - 1][x - 0] == 1:
                neighbors += 1

    if x < len(current_state[y]) - 1:
        if current_state[y][x + 1] == 1:
            neighbors += 1
        if y < len(current_state) - 1:
            if current_state[y + 1][x + 1] == 1:
                neighbors +=1
        if y > 0:
            if current_state[y - 1][x + 1] == 1:
                neighbors += 1


    if y < len(current_state) - 1:
        if current_state[y + 1][x] == 1:
            neighbors +=1
    if y > 0:
        if current_state[y - 1][x] == 1:
            neighbors += 1

    return neighbors
