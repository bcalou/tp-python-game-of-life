import pygame

'''Constants'''
DISPLAY_SIZE_X: int = 600
DISPLAY_SIZE_Y: int = 600
FPS: int = 1

BLACK_COLOR: tuple = (0,0,0)
WHITE_COLOR: tuple = (255,255,255)

GRID_SIZE_X = 3
GRID_SIZE_Y = 3
#Vérifier que c'est égale à la taille de la matrice

pygame.init()


def main():
    screen: pygame.surface.Surface = pygame.display.set_mode((DISPLAY_SIZE_X, DISPLAY_SIZE_Y))
    
    clock = pygame.time.Clock()

    done: bool = False

    '''Matrix initialisation'''
    initial_state: list[list[int]] = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    state = initial_state

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        #####
        '''For each iteration'''
        
        state = get_next_state(state)


        screen.fill(BLACK_COLOR)



        case_size_x = int(DISPLAY_SIZE_X / GRID_SIZE_X)
        case_size_y = int(DISPLAY_SIZE_Y / GRID_SIZE_Y)

        for index_y in range(len(state)):
            for index_x in range(len(state[index_y])):
                if state[index_y][index_x] == 1:
                    pygame.draw.rect(screen, WHITE_COLOR, (index_x * case_size_x, index_y * case_size_y, case_size_x, case_size_y)) #x, y, largeur, hauteur

        '''Called at the end of each update. Allows to apply modifications'''
        pygame.display.flip()
        #####
        clock.tick(FPS)

    pygame.quit()

def get_next_state(state_matrix):
    

    for index_y in range(len(state_matrix)):
        for index_x in range(len(state_matrix[index_y])):
            number_neighbor: int = 0
            '''Filter'''
            
            
            #Case en haut à gauche
            if state_matrix[index_y - 1][index_x - 1] == 1:
                number_neighbor += 1
            #Cause en haut
            if state_matrix[index_y - 1][index_x] == 1:
                number_neighbor += 1
            #Case en haut à droite
            if state_matrix[index_y - 1][index_x + 1] == 1:
                number_neighbor += 1


            #Case à gauche
            if state_matrix[index_y][index_x - 1] == 1:
                number_neighbor += 1                
            #Case à droite
            if state_matrix[index_y][index_x + 1] == 1:
                number_neighbor += 1
            #Case en bas à gauche
            if state_matrix[index_y + 1][index_x - 1] == 1:
                number_neighbor += 1
            #Case en bas
            if state_matrix[index_y + 1][index_x] == 1:
                number_neighbor += 1   
            #Case en bas à droite
            if state_matrix[index_y + 1][index_x + 1] == 1:
                number_neighbor += 1

            print(number_neighbor)
            
            #une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît)
            if state_matrix[index_y][index_x] == 0 and number_neighbor == 3:
                #Cell alive
                state_matrix[index_y][index_x] = 1

            #une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.
            if not state_matrix[index_y][index_x] == 1 and not (number_neighbor == 2 or number_neighbor == 3):
                #Cell death
                state_matrix[index_y][index_x] = 0

    return state_matrix

main()