import pygame
from pygame import constants
import screen
import copy
import time
import constant

# run the game.
pygame.init()

done = False
clock = pygame.time.Clock()

initial_state: list[list[int]] = constant.MATRIX

screen.init(initial_state)

def is_extremity(i, j):
        return True if j == 0 or i == 0 or j == len(copied_matrix[0])-1 or i == len(copied_matrix)-1 else False
    

def get_voisin(copied_matrix, i, j):
    voisin: int = 0
    extremity = is_extremity(i,j)

    if not extremity:
        if (copied_matrix[i][j-1] == 1):
            voisin += 1
        if (copied_matrix[i][j+1] == 1):
            voisin += 1
        if (copied_matrix[i-1][j] == 1):
            voisin += 1
        if (copied_matrix[i+1][j] == 1):
            voisin += 1
        if (copied_matrix[i-1][j-1] == 1):
            voisin += 1
        if (copied_matrix[i-1][j+1] == 1):
            voisin += 1
        if (copied_matrix[i+1][j-1] == 1):
            voisin += 1
        if (copied_matrix[i+1][j+1] == 1):
            voisin += 1
    else:
        is_first_line = True if i == 0 else False
        is_first_column = True if j == 0 else False
        is_last_line = True if i == len(copied_matrix)-1 else False
        is_last_column = True if j == len(copied_matrix[0])-1 else False

        if is_first_line and is_first_column:
            if (copied_matrix[i][j+1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j+1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j] == 1):
                voisin += 1
        elif is_first_line and is_last_column:
            if (copied_matrix[i][j-1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j-1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j] == 1):
                voisin += 1
        elif is_first_line:
            if (copied_matrix[i+1][j-1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j] == 1):
                voisin += 1
            if (copied_matrix[i+1][j+1] == 1):
                voisin += 1   
            if (copied_matrix[i][j-1] == 1):
                voisin += 1
            if (copied_matrix[i][j+1] == 1):
                voisin += 1
        elif is_last_line and is_first_column:
            if (copied_matrix[i][j+1] == 1):
                voisin += 1
            if (copied_matrix[i-1][j+1] == 1):
                voisin += 1
            if (copied_matrix[i-1][j] == 1):
                voisin += 1
        elif is_last_line and is_last_column:
            if (copied_matrix[i][j-1] == 1):
                voisin += 1
            if (copied_matrix[i-1][j-1] == 1):
                voisin += 1
            if (copied_matrix[i-1][j] == 1):
                voisin += 1
        elif is_last_line:
            if (copied_matrix[i-1][j-1] == 1):
                voisin += 1
            if (copied_matrix[i-1][j] == 1):
                voisin += 1
            if (copied_matrix[i-1][j+1] == 1):
                voisin += 1   
            if (copied_matrix[i][j-1] == 1):
                voisin += 1
            if (copied_matrix[i][j+1] == 1):
                voisin += 1
        elif is_first_column:
                if (copied_matrix[i-1][j] == 1):
                    voisin += 1
                if (copied_matrix[i-1][j+1] == 1):
                    voisin += 1
                if (copied_matrix[i][j+1] == 1):
                    voisin += 1
                if (copied_matrix[i+1][j] == 1):
                    voisin += 1
                if (copied_matrix[i+1][j+1] == 1):
                    voisin += 1   
        elif is_last_column:
            if (copied_matrix[i-1][j] == 1):
                    voisin += 1
            if (copied_matrix[i-1][j-1] == 1):
                voisin += 1
            if (copied_matrix[i][j-1] == 1):
                voisin += 1
            if (copied_matrix[i+1][j] == 1):
                voisin += 1
            if (copied_matrix[i+1][j-1] == 1):
                voisin += 1  

    return voisin

def get_next_state(copied_matrix):
    new_state: list[list[int]] = copied_matrix
    voisin_matrix: list[list[int]] = [[0 for column in range(len(copied_matrix[0]))]for row in range(len(new_state))]
    for i in range(len(copied_matrix)):
        for j in range(len(copied_matrix[i])):
            voisin_matrix[i][j] = get_voisin(copied_matrix, i, j)
    
    for index_row in range(len(copied_matrix)):
        for index_column in range(len(copied_matrix[index_row])):
            if voisin_matrix[index_row][index_column] > 3 or voisin_matrix[index_row][index_column] < 2:
                if copied_matrix[index_row][index_column] == 1:
                    new_state[index_row][index_column] = 0
            elif voisin_matrix[index_row][index_column] == 3:
                if copied_matrix[index_row][index_column] == 0:
                    new_state[index_row][index_column] = 1
    return new_state
copied_matrix = copy.deepcopy(initial_state)
finish = False
while not finish :
    new_state = get_next_state(copied_matrix)
    copied_matrix = copy.deepcopy(new_state)
    screen.init(new_state)
    time.sleep(1) 

screen.get_lifespan(done, clock)
pygame.quit()
