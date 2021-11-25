from typing import List
import pygame
import random as rd
from src.cell import Cell
from src.constantes import GameConstants as gc

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((gc.WINDOW_WIDTH, gc.WINDOW_HEIGHT))

clock = pygame.time.Clock()

done: bool = False

init_pattern = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
]

def check_alive_neighbour(grid : List[List[Cell]], row : int, column : int):
    alive_count = 0
    neighbour_pos = [
        (row-1 ,column-1),
        (row-1 ,column  ),
        (row-1 ,column+1),

        (row, column-1),
        (row ,column+1),

        (row+1 ,column-1),
        (row+1 ,column  ),
        (row+1 ,column+1),
    ]
    for n in neighbour_pos:
        if n[0] >= 0 and n[0] < len(grid) and n[1] >= 0 and n[1] < len(grid[0]):
            alive_count += 1 if grid[n[0]][n[1]].isAlive else 0
    return alive_count
    


w = gc.WINDOW_WIDTH
h = gc.WINDOW_HEIGHT
s = gc.SIZE_OF_CELL

grid_game = [[Cell((j*s, i*s, s, s)) for j in range(w//s)] for i in range(h//s)]


for row in range(len(init_pattern)):
    row_offset = len(init_pattern) // 2
    for column in range(len(init_pattern[row])):
        column_offset = len(init_pattern[row]) // 2
        if init_pattern[row][column] == 1:
            grid_game[row][column].setState(True)
            #grid_game[row + w//s//2][column + h//s//2].setState(True)


# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((0, 0, 0))
    ch = ""
    for row in range(len(init_pattern)):
        for column in range(len(init_pattern[row])):

            pygame.draw.rect(screen, grid_game[row][column].color, grid_game[row][column].rect)
            alive_nb = check_alive_neighbour(grid_game, row, column)
            ## TODO change state too early
            ch += str(alive_nb) 
            future_grid[row][column].testSurvivability(alive_nb)
        ch += "\n"
    print(ch)
    grid_game = future_grid
    pygame.display.flip()

    clock.tick(1)

pygame.quit()



                      

                
    
