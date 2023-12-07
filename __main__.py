import pygame
from game_of_life.get_next_state import get_next_state
from game_of_life.default import GLIDER_GUN


WIDTH = 980
HEIGHT = 980
PIXEL_SIZE = 20


def main():
    print("Hello world")
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    done = False

    state: list[list[int]] = GLIDER_GUN

    # for y in range(0, 3):
    #         print(f"{get_neighbours_count(state, 0, y)} \
    #                 {get_neighbours_count(state, 1, y)} \
    #                 {get_neighbours_count(state, 2, y)}")

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        # debug
        # print("\n\n\n\n\n\n")
        # for y in range(len(state)):
        #     for x in range(len(state[0])):
        #         print(state[y][x], end="")
        #     print("")

        # Effacer l'écran
        screen.fill((0, 0, 0))

        # Déssine l'etat initial_state
        print_state(screen, state)

        # Applique les déssins sur l'écran
        pygame.display.flip()

        # Calcule l'etat suivant
        state = get_next_state(state)

        # print("Update !")
        clock.tick(120)

    pygame.quit()


def print_state(screen, state: list[list[int]]) -> None:
    """Print cell to the screen according to the state"""
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            color: int = cell*220 + 35
            pygame.draw.rect(screen, (color, color, color), (
                             x*PIXEL_SIZE, y*PIXEL_SIZE,
                             PIXEL_SIZE-1, PIXEL_SIZE-1))


main()
