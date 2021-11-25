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
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def check_alive_neighbour(grid : List[List[Cell]], x : int, y : int):
    alive_count = 0
    neighbour_pos = [
        (x-1, y-1),
        (x-1 ,y),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
    ]
    for n in neighbour_pos:
        if n[0] >= 0 and n[0] < len(grid) and n[1] >= 0 and n[1] < len(grid[1]):
            alive_count += 1 if grid[n[0]][n[1]].isAlive else 0
    return alive_count
    


w = gc.WINDOW_WIDTH
h = gc.WINDOW_HEIGHT
s = gc.SIZE_OF_CELL

#True if rd.randint(0,100) <= 20 else False
grid_game = [[Cell((i*s, j*s, s, s), True if rd.randint(0,100) <= 30 else False) for j in range(w//s)] for i in range(h//s)]

# While the game is not over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((0, 0, 0))

    for column in range(len(grid_game)):
        for row in range(len(grid_game[0])):
            pygame.draw.rect(screen, grid_game[row][column].color, grid_game[row][column].rect)
            alive_nb = check_alive_neighbour(grid_game, row, column)
            grid_game[row][column].testSurvivability(alive_nb)
    pygame.display.flip()

    clock.tick(1)

pygame.quit()



                      

                
    
