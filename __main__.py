import pygame

def main():
    print("Hello world")
    pygame.init()
    screen = pygame.display.set_mode((1120, 600))

    clock = pygame.time.Clock()

    done = False

    initial_state: list[list[int]] = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
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
            
            # Effacer l'écran
            screen.fill((0, 0, 0))

            # Déssine l'etat initial_state
            print_state(screen, initial_state)
            
            # Applique les déssins sur l'écran
            pygame.display.flip()

        # print("Update !")
        clock.tick(30)

    pygame.quit()

pixel_size = 25
def print_state(screen, state: list[list[int]]) -> None:
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*pixel_size, y*pixel_size, x+pixel_size, y+pixel_size))
            else:
                pygame.draw.rect(screen, (50, 50, 50), (x*pixel_size, y*pixel_size, x+pixel_size, y+pixel_size))



main()
