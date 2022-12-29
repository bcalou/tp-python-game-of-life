from game_of_life.params import *
from game_of_life.Game import *
from game_of_life.Display import *


new_game = Game(INITIAL_STATE)
display = Display(WINDOW_SIZE, new_game)

display.init_pygame()
display.display()
