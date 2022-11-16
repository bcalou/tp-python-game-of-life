import pygame

'''Constants'''
DISPLAY_SIZE_X = 700
DISPLAY_SIZE_Y = 700
FPS = 1

BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)

pygame.init()


def get_next_state():   
    screen: pygame.surface.Surface = pygame.display.set_mode((DISPLAY_SIZE_X, DISPLAY_SIZE_Y))
    
    clock = pygame.time.Clock()

    done: bool = False

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        #####
        '''For each iteration'''
        screen.fill(BLACK_COLOR)
        pygame.draw.rect(screen, WHITE_COLOR, (0, 0, 100, 100))#x, y, largeur, hauteur
        pygame.draw.rect(screen, WHITE_COLOR, (100, 100, 200, 200))


        '''Called at the end of each update. Allows to apply modifications'''
        pygame.display.flip()
        #####
        clock.tick(FPS)

    pygame.quit()

get_next_state()