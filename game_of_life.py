import pygame

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

done: bool = False

# While the game is not over
while not done:
    screen.fill((0, 0, 0))
    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True
    initial_state: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
    line = 0
    #mettre une image quadrier en fond 
    for i in initial_state:
        line +=1 
        col = 0
        for y in i:
            col +=1
            if(y == 1):
                print(line,col)
                pygame.draw.rect(screen, (255, 255, 255), (200*(col-1), 200*(line-1), 200, 200))
    
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
