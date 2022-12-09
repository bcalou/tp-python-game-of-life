from game_of_life.params import *
from game_of_life.Game import Game
from game_of_life.Display import Display


new_game = Game(INITIAL_STATE)
display = Display(WINDOW_SIZE, new_game)
