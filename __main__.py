import pygame

pygame.init()

def main():
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    done = False

    # While the game is not over
    while not done:
        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        # Update the screen
        # fill screen with white fileld squares and black borders
        for i in range(0, 1000, 100):
            for j in range(0, 1000, 100):
                pygame.draw.rect(screen, (255, 255, 255), (i, j, 100, 100), 0)
                pygame.draw.rect(screen, (0, 0, 0), (i, j, 100, 100), 1)
        
        pygame.display.flip()
        print("Update !")
        clock.tick(1)
    
    pygame.quit()

main()
