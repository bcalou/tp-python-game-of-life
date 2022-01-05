from const import INITIAL_STATE, NUMBER_OF_SQUARE, SCREEN_SIZE, SIZE_OF_SQUARE
import pygame
import copy

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((0, 0, 0))

def newMatrice(matrice: list[list[int]]):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), 
                (j*SIZE_OF_SQUARE, i*SIZE_OF_SQUARE, SIZE_OF_SQUARE, SIZE_OF_SQUARE))
                pygame.display.flip()
            if matrice[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), 
                (j*SIZE_OF_SQUARE, i*SIZE_OF_SQUARE, SIZE_OF_SQUARE, SIZE_OF_SQUARE))
                pygame.display.flip()

def nextStep(matrice: list[list[int]]) -> list[list[int]]:
    editable_copy = copy.deepcopy(matrice)
    for i in range(0, len(INITIAL_STATE)):
        for j in range(0, len(INITIAL_STATE[0])):
            number_of_neighbours_cells: int = 0

            if i == 0:
              if matrice[i+1][j] == 1:
                  number_of_neighbours_cells += 1
              if j == 0:
                  if matrice[i][j+1] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i+1][j+1] == 1:
                      number_of_neighbours_cells += 1
              if j == len(INITIAL_STATE[0])-1:
                  if matrice[i][j-1] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i+1][j-1] == 1:
                      number_of_neighbours_cells += 1
              else:
                if matrice[i][j-1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i][j+1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j-1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j+1] == 1:
                    number_of_neighbours_cells += 1

            elif i == len(INITIAL_STATE)-1:
              if matrice[i-1][j] == 1:
                  number_of_neighbours_cells += 1
              if j == 0:
                  if matrice[i][j+1] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i-1][j+1] == 1:
                      number_of_neighbours_cells += 1
              if j == len(INITIAL_STATE[0])-1:
                  if matrice[i][j-1] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i-1][j-1] == 1:
                      number_of_neighbours_cells += 1
              else:
                if matrice[i][j-1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i][j+1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i-1][j-1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i-1][j+1] == 1:
                    number_of_neighbours_cells += 1

            elif j == 0:
              if matrice[i][j+1] == 1:
                  number_of_neighbours_cells += 1
              if i == 0:
                  if matrice[i+1][j] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i+1][j+1] == 1:
                      number_of_neighbours_cells += 1
              if i == len(INITIAL_STATE)-1:
                  if matrice[i-1][j] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i-1][j+1] == 1:
                      number_of_neighbours_cells += 1
              else:
                if matrice[i-1][j] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i-1][j+1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j+1] == 1:
                    number_of_neighbours_cells += 1

            elif j == len(INITIAL_STATE[0])-1:
              if matrice[i][j-1] == 1:
                  number_of_neighbours_cells += 1
              if i == 0:
                  if matrice[i-1][j] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i-1][j-1] == 1:
                      number_of_neighbours_cells += 1
              if i == len(INITIAL_STATE)-1:
                  if matrice[i-1][j] == 1:
                      number_of_neighbours_cells += 1
                  if matrice[i-1][j-1] == 1:
                      number_of_neighbours_cells += 1
              else:
                if matrice[i-1][j] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i-1][j-1] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j] == 1:
                    number_of_neighbours_cells += 1
                if matrice[i+1][j-1] == 1:
                    number_of_neighbours_cells += 1
            
            else:
              if matrice[i-1][j-1] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i-1][j] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i-1][j+1] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i][j-1] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i][j+1] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i+1][j-1] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i+1][j] == 1:
                  number_of_neighbours_cells += 1
              if matrice[i+1][j+1] == 1:
                  number_of_neighbours_cells += 1
                
            if number_of_neighbours_cells == 3:
                editable_copy[i][j] = 1
            elif number_of_neighbours_cells == 2:
                editable_copy[i][j] = matrice[i][j]
            else:
              editable_copy[i][j] = 0

    return editable_copy

clock = pygame.time.Clock()
done: bool = False

matrice = INITIAL_STATE
# newMatrice(matrice)

# While the game is not over
while not done:

    newMatrice(matrice)
    matrice = nextStep(matrice)

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60)

pygame.quit()
