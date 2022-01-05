import pygame
import constant

def draw_square(screen):
    pygame.draw.rect(screen, constant.WHITE, (0, 0, constant.SQUARE_SIZE, constant.SQUARE_SIZE))
    pygame.display.flip()

def get_lifespan(screen):
    # Lifespan
    clock = pygame.time.Clock()
    done: bool = False

    # While the game is not over.
    while not done:
        # Listen for all events.
        for event in pygame.event.get():
            # Quit the infinite loop when the user press the close button.
            if event.type == pygame.QUIT:
                done = True
        # Update frequency.
        clock.tick(constant.UPDATE_FREQUENCY)

def init():
    screen: pygame.surface.Surface = pygame.display.set_mode(constant.SCREEN_SIZE)
    screen.fill(constant.BLACK)

    draw_square(screen)
    get_lifespan(screen)