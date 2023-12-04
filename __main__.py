import pygame

def main():
    
    initial_state: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
    
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 700, 700))
    pygame.draw.rect(screen, (0, 0, 0), (130, 70, 40, 40))
    pygame.draw.rect(screen, (0, 0, 0), (530, 90, 40, 40))
    pygame.display.flip()
    
    clock = pygame.time.Clock()

    done = False

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        print("Update !")
        clock.tick(1)

    pygame.quit()

main()
