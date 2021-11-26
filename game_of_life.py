import pygame
import copy

# Allows to load, move and draw a texture to represent an object
class Image:
    screen: pygame.surface.Surface
    surface: pygame.surface.Surface
    rect: pygame.rect.Rect

    def __init__(self, texture: str, screen: pygame.surface.Surface):
        self.surface = pygame.image.load(texture)
        self.rect = self.surface.get_rect()
        self.screen = screen

    def set_position(self, x: int, y: int):
        self.rect.topleft = (y, x)

    def paint(self, x: int = 0, y: int = 0):
        self.set_position(x, y)
        self.screen.blit(self.surface, self.rect)

# Go through a state and draw every tile based on its number
def print_state(state: list[list[int]], screen: pygame.surface.Surface):
        screen.fill((0, 0, 0))
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    dead: Image = Image("dead_50.png", screen)
                    dead.paint(i * 50, j * 50)
                else:
                    alive: Image = Image("alive_50.png", screen)
                    alive.paint(i * 50, j * 50)

# Go through a state and make avery number evolve depending on its surroundings
def get_next_state(state: list[list[int]]) -> list[list[int]]:
    next_state: list[list[int]] = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            # Count the number of alive tiles arround the current tile
            alive_tiles: int = 0
            if i > 0:
                if j > 0:
                    if state[i-1][j-1] > 0:
                        alive_tiles += 1
                if state[i-1][j] > 0:
                    alive_tiles += 1
                if j < len(state[i-1]) - 1:
                    if state[i-1][j+1] > 0:
                        alive_tiles += 1
            if j > 0:
                if state[i][j-1] > 0:
                    alive_tiles += 1
            if j < len(state[i]) - 1:
                if state[i][j+1] > 0:
                    alive_tiles += 1
            if i < len(state) - 1:
                if j > 0:
                    if state[i+1][j-1] > 0:
                        alive_tiles += 1
                if state[i+1][j] > 0:
                    alive_tiles += 1
                if j < len(state[i+1]) - 1:
                    if state[i+1][j+1] > 0:
                        alive_tiles += 1
            # The two rules of the game of life
            if(i == 0 and j == 2):
                print("Alive tiles for (" + str(i) + ", " + str(j) + "): " + str(alive_tiles))
            if alive_tiles == 3 and state[i][j] == 0:
                next_state[i][j] = 1
            elif state[i][j] > 0:
                if not (alive_tiles == 2 or alive_tiles == 3):
                    state[i][j] = 0
    return next_state

# The main game function
def game(initial_state: list[list[int]]):
    pygame.init()

    width: int = 1000
    height: int = 1000
    screen: pygame.surface.Surface = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    done: bool = False
    current_state: list[list[int]] = initial_state
    print_state(current_state, screen)
    pygame.display.flip()

    # While the game is not over
    while not done:
        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        # Compute the next state based on the initial state
        current_state = get_next_state(initial_state)

        # Draw the current state
        print_state(current_state, screen)
        pygame.display.flip()
        clock.tick(1)

    # Close the window when the loop is over
    pygame.quit()

# Main thread
initial_state: list[list[int]] = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
game(initial_state)