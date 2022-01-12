import pygame
import constant

def draw_square(screen, initial_state):
    x = 0
    for i in initial_state:
        y = 0
        for j in i:
            if j == 1:
                pygame.draw.rect(screen, constant.WHITE, (y, x, constant.SCREEN_SIZE[0] / len(initial_state), constant.SCREEN_SIZE[1] / len(i)))
            else:
                pygame.draw.rect(screen, constant.BLACK, (y, x, constant.SCREEN_SIZE[0] / len(initial_state), constant.SCREEN_SIZE[1] / len(i)))

            y += constant.SCREEN_SIZE[0] / len(initial_state)
            
        x += constant.SCREEN_SIZE[1] / len(i)

    pygame.display.flip()

def get_lifespan(done, clock):
    # While the game is not over.
    while not done:
        # Listen for all events.
        for event in pygame.event.get():
            # Quit the infinite loop when the user press the close button.
            if event.type == pygame.QUIT:
                done = True
        # Update frequency.
        clock.tick(constant.UPDATE_FREQUENCY)

def init(initial_state):
    screen: pygame.surface.Surface = pygame.display.set_mode(constant.SCREEN_SIZE)
    screen.fill(constant.BLACK)

    draw_square(screen, initial_state)
    #get_lifespan(screen)