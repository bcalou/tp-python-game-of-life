import pygame

SCREEN_SIZE: int = 1000
SQUARE_COLOR: (int,int,int) = (0, 0, 0)
pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

clock = pygame.time.Clock()

done: bool = False
initial_state: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
screen_state = initial_state
row_len: int = len(initial_state)
column_len: int = len(initial_state[1])
block_size: int = SCREEN_SIZE // len(initial_state)



def events_check():
    """check if there is any event"""
    global done
    # Listen for all events
    for event in pygame.event.get():
        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True


def update_screen_state_from_matrix(matrix_state: list[list[int]]):
    """Go through a given matrix, and renders it on the screen"""
    global screen
    for row_index in range(0, row_len):
        for column_index in range(0, column_len):
            if matrix_state[row_index][column_index] == 1:
                x_position:int = column_index * block_size
                y_position:int = row_index * block_size
                pygame.draw.rect(screen, SQUARE_COLOR,
                                 (x_position, y_position, block_size, block_size))

# While the game is not over
while not done:
    screen.fill((255, 255, 255))

    events_check()
    update_screen_state_from_matrix(screen_state)

    print("Update !")
    pygame.display.flip()
    clock.tick(1)

pygame.quit()


def get_next_state():
    pass


