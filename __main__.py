from constants import GLIDER_GUN, grid_type

initial_grid: grid_type = GLIDER_GUN

if __name__ == '__main__':
    from game_controller import GameController

    game_controller = GameController(initial_grid)
    game_controller.game_routine()
