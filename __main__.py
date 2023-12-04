import pygame

def main():
    print("Hello world")
    pygame.init()
    screen = pygame.display.set_mode((1120, 600))

    clock = pygame.time.Clock()

    done = False

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True
            
            # Effacer l'écran
            screen.fill((0, 0, 0))

            # Déssine un carrée blanc (ecran, couleur, (x,y,x2,y2))
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 100, 100))
            
            # Applique les déssins sur l'écran
            pygame.display.flip()

        print("Update !")
        clock.tick(30)

    pygame.quit()


main()
