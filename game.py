import math
import pygame
import copy

screen_size : tuple = (600,600)
screen : pygame.surface.Surface = pygame.display.set_mode(screen_size)

def draw_squares(squares : list[list[int]]) :
    """draw the map

    Args:
        squares (list[list[int]]): a 2d list contains 0 and 1 , if 0 draw purple else draw orange
    """
    square_width = math.floor(screen_size[0]/len(squares))
    square_height = math.floor(screen_size[1]/len(squares[1]))
    square_size : list[int] = [square_width, square_height]
    for i in range(len(squares))  :
        for j in range(len(squares[i])):
            square = j*square_size[0],i*square_size[1],square_size[0], square_size[1]
            if squares[i][j] == 1:
                pygame.draw.rect(screen,(255,124,0),(square))
            else : 
                pygame.draw.rect(screen,(124,102,255),(square))
    pygame.display.flip()


def get_neighbor_amount(x : int, y: int, squares : list[list[int]]) -> int:
    """get the amount of neighbors of the square

    Args:
        x (int): position x of the square
        y (int): position y of the square
        squares (list[list[int]]): sqaure

    Returns:
        int: [description]
    """
    neighbor_amount = 0
    neighbour_cells = [(x-1, y-1), (x-1, y), (x-1, y+1),(x, y-1), (x, y+1),
                       (x+1, y-1), (x+1, y), (x+1, y+1)]
    for ax, ay in neighbour_cells:
        if is_neighbor_valid(ax, ay, squares):
            if squares[ax][ay] == 1:
                neighbor_amount += 1
    return neighbor_amount

def is_neighbor_valid(x : int, y: int, squares : list[list[int]]) -> bool:
    """check if the neighbor of the square is valid or not
    """
    width_squares : int = len(squares) - 1
    height_squares : int = len(squares[1]) - 1
    return True if not any([x<0, y<0, x>width_squares, y > height_squares]) else False

def is_alive(x : int, y : int, squares : list[list[int]]) -> bool:
    """check if the sqare can be alive or not 

    Returns:
        bool: if the sqaure has 3 neighbors => alive else dead
    """
    neighbors_number = get_neighbor_amount(x,y,squares)
    if squares[x][y] == 0:
        return True if neighbors_number == 3 else False
    else:
        return False if any([neighbors_number > 3, neighbors_number < 2]) else True

def get_next_state(state : list[list[int]]) -> list[list[int]]:
    """return the new map based on the map previous

    Args:
        state (list[list[int]]): map previous

    Returns:
        list[list[int]]: next map
    """
    state_copy:  list[list[int]] = copy.deepcopy(state)
    for i in range(len(state_copy)):
        for j in range(len(state_copy[i])):
            if is_alive(i,j,state_copy) :
                state[i][j] = 1 
            else:
                state[i][j] = 0
    return state
