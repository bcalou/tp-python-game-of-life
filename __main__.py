import pygame

from game_of_life.initial_state import INITIAL_STATE
from game_of_life.game import Game
from game_of_life.board import Board
from game_of_life.state import State

FRAMES_PER_SECOND = 30


def main():
    """Instantiate the classes and start the game"""

    state = State(INITIAL_STATE)
    board = Board(state)
    game = Game(board, state)

    start(game)


def start(game: Game):
    """Start the game loop"""

    clock = pygame.time.Clock()

    done = False

    # Game loops until it's over
    while not done:

        # Listen for all events
        for event in pygame.event.get():

            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        clock.tick(FRAMES_PER_SECOND)
        game.update()

    pygame.quit()


main()
