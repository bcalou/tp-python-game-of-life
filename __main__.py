from grid_manager import grid_type

initial_grid: grid_type = [
    # 0 1  2  3  4  5  6  7  8  9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # 3
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # 4
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 9
]

if __name__ == '__main__':
    from game_controller import GameController

    game_controller = GameController()
    game_controller.game_logic(initial_grid)
