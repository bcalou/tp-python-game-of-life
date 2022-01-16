import pygame
from map import map_start
from game import draw_squares, get_next_state

pygame.init()
timer = pygame.time.Clock()
game_stop: bool = False
while not game_stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stop = True
    draw_squares(map_start)
    get_next_state(map_start)
    timer.tick(10)
pygame.quit()