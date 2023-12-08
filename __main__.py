import game_of_life.const as Const
from game_of_life.Matrix_State import Matrix_State
from game_of_life.Display import Display

DEFAULT_TICK: int = 60
COLOR_BLACK: tuple[int, int, int] = (0, 0, 0)


class Main:

    __matrix: Matrix_State
    __window: Display

    def __init__(self, clock_tick: int = DEFAULT_TICK):
        """You can set the number of frames to refresh the game"""
        self.__clock_tick = clock_tick
        self.upgrade_pygame()

    def upgrade_pygame(self) -> None:
        """We use pygame for create and modify a window"""

        # We initiate all variable we need
        Const.pygame.init()
        clock = Const.pygame.time.Clock()
        done = False
        self.__window = Display()
        self.__matrix = Matrix_State()

        # While the game is not over
        while not done:

            # We choose the state of the grid
            self.__matrix.state_choose()

            # We change visual of game
            self.change_visual()

            # We modify the matrix every tick
            clock.tick(self.__clock_tick)

            # Listen for all events
            for event in Const.pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == Const.pygame.QUIT:
                    done = True

        Const.pygame.quit()

    def change_visual(self) -> None:
        """We clear screen and draw a new screen"""

        # We clear and we draw
        Const.screen.fill(COLOR_BLACK)
        self.__window.draw_on_screen(self.__matrix.get_state())

        # We need to flip pygame for making change effective
        Const.pygame.display.flip()


Main()
