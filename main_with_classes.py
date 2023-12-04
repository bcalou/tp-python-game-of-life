import pygame
from game_of_life.GameOfLife import GameOfLife, generate_random_state


WIDTH = 2200
HEIGHT = 1300
pixel_size = 20

def main_with_classes():
    print("Hello world")
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    done = False

    print(f"SIMULATION SIZE: {(WIDTH//pixel_size, HEIGHT//pixel_size)}")
    game_of_life: GameOfLife = GameOfLife(generate_random_state(WIDTH//pixel_size, HEIGHT//pixel_size))

    # for y in range(0, 3):
    #         print(f"{get_neighbours_count(state, 0, y)} {get_neighbours_count(state, 1, y)} {get_neighbours_count(state, 2, y)}")

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
        print_state(screen, game_of_life)

        # Applique les déssins sur l'écran
        pygame.display.flip()

        # Calcule l'etat suivant
        game_of_life.next_state()
        
        # print("Update !")
        clock.tick(30)

    pygame.quit()


def print_state(screen, game_of_life: GameOfLife) -> None:
    for y in range(game_of_life.get_height()):
        for x in range(game_of_life.get_width()):
            color: int = game_of_life.get_cell(x, y)*220 + 35
            pygame.draw.rect(screen, (color, color, color), 
                            (x*pixel_size, y*pixel_size, pixel_size-1, pixel_size-1))

main_with_classes()
