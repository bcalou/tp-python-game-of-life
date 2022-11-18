import pygame
# import random
import copy
import game_of_life.params as params


Matrix = list[list[int]]


LINES: int = len(params.INITIAL_STATE)
COLUMNS: int = len(params.INITIAL_STATE[0])
SQUARE_X_SIZE: int = params.WINDOW_SIZE[0] // COLUMNS
SQUARE_Y_SIZE: int = params.WINDOW_SIZE[1] // LINES


def increase_speed():
    if params.frequency < 128: params.frequency = params.frequency * 2
    print(f'Frequency : {params.frequency} Hz')


def decrease_speed():
    if params.frequency > 1: params.frequency = params.frequency // 2
    print(f'Frequency : {params.frequency} Hz')


def main():
    pygame.init()
    screen: pygame.surface.Surface = pygame.display.set_mode(params.WINDOW_SIZE)
    pygame.display.set_caption("Game of life")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri", 50)
    done: bool = False
    current_state: Matrix = copy.deepcopy(params.INITIAL_STATE)
    generation: int = 1
    

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    increase_speed()
                elif event.key == pygame.K_DOWN:
                    decrease_speed()
        
        for y in range(LINES):
            for x in range(COLUMNS):
                if current_state[y][x] == 1:
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255)
                
                pygame.draw.rect(screen, color, (x * SQUARE_X_SIZE, y * SQUARE_Y_SIZE, SQUARE_X_SIZE, SQUARE_Y_SIZE))
        
        text = font.render(f'{generation}', True, (255, 0, 0))
        screen.blit(text, (0, 0))
        pygame.display.flip()

        current_state = get_next_state(current_state)
        generation += 1
        clock.tick(params.frequency)

    pygame.quit()


"""def generate_random_coordinates() -> tuple:
    coordinates: tuple = (random.randint(0, 600), random.randint(0, 600))
    return coordinates"""


def get_next_state(current_state: Matrix) -> Matrix:
    # print("Getting next_state")
    next_state: Matrix = create_empty_matrix(LINES, COLUMNS)

    for y in range(LINES):
            for x in range(COLUMNS):
                # print(f'Checking cell [{x}][{y}]')
                if will_the_cell_live(current_state, current_state[y][x], x, y):
                    next_state[y][x] = 1
                else:
                    next_state[y][x] = 0
    
    return next_state


def create_empty_matrix(lines: int, columns: int) -> Matrix:
    matrix: Matrix = []

    for y in range(lines):
        matrix.append([])
        for x in range(columns):
            matrix[y].append(0)
    
    return matrix


def will_the_cell_live(current_state_matrix: Matrix, current_state_of_cell: int, x: int, y: int) -> bool:
    # print(f'Checking if cell [{x}][{y}] will live')
    living_cells_around: int = 0

    for surrounding_cell_Y in range(y -1, y + 2):
        for surrounding_cell_X in range(x - 1, x + 2):
            if 0 <= surrounding_cell_X <= (COLUMNS - 1) and 0 <= surrounding_cell_Y <= (LINES - 1):
                # print(f'Checking cell [{surrounding_cell_X}][{surrounding_cell_Y}]')
                living_cells_around += current_state_matrix[surrounding_cell_Y][surrounding_cell_X]
            
    living_cells_around -= current_state_matrix[y][x]
    # print(f'Living cells around : {living_cells_around}')
    
    if current_state_of_cell == 0 and living_cells_around == 3:
        # print(f'Cell [{x}][{y}] will be born')
        return True
    elif current_state_of_cell == 1 and 2 <= living_cells_around <= 3:
        # print(f'Cell [{x}][{y}] will keep living')
        return True
    else:
        # print(f'Cell [{x}][{y}] will die')
        return False


main()


# print(create_empty_matrix(LINES, COLUMNS))

# print(will_the_cell_live(params.INITIAL_STATE, params.INITIAL_STATE[y][x], x, y))
