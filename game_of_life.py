import pygame

'''Constants'''
DISPLAY_SIZE_X: int = 600
DISPLAY_SIZE_Y: int = 600
FPS: int = 1

BLACK_COLOR: tuple = (0,0,0)
WHITE_COLOR: tuple = (255,255,255)

GRID_SIZE_X = 10
GRID_SIZE_Y = 10
#Vérifier que c'est égale à la taille de la matrice

pygame.init()


def get_next_state():   
    screen: pygame.surface.Surface = pygame.display.set_mode((DISPLAY_SIZE_X, DISPLAY_SIZE_Y))
    
    clock = pygame.time.Clock()

    done: bool = False

    '''Matrix initialisation'''
    initial_state: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

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



        case_size_x = int(DISPLAY_SIZE_X / GRID_SIZE_X)
        case_size_y = int(DISPLAY_SIZE_Y / GRID_SIZE_Y)

        for index_y in range(len(initial_state)):
            for index_x in range(len(initial_state[index_y])):
                if initial_state[index_y][index_x] == 1:
                    pygame.draw.rect(screen, WHITE_COLOR, (index_x * case_size_x, index_y * case_size_y, case_size_x, case_size_y)) #x, y, largeur, hauteur

        '''Called at the end of each update. Allows to apply modifications'''
        pygame.display.flip()
        #####
        clock.tick(FPS)

    pygame.quit()

get_next_state()