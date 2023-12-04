import pygame

SQUARE_SIZE: int = 20
SQUARE_COLOR: tuple[int, int, int] = (0, 0, 0)
SQUARE_BORDER_COLOR: tuple[int, int, int] = (100, 100, 100)
SCREEN_SIZE: tuple[int, int] = (1000, 1000)
GRID_SIZE: tuple[int, int] = (SCREEN_SIZE[0] // SQUARE_SIZE,
                              SCREEN_SIZE[1] // SQUARE_SIZE)

NEIGHBORS: list[tuple[int, int]] = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

SCREEN_SQUARE_SIZE: tuple[int, int] = (
    SCREEN_SIZE[0] // SQUARE_SIZE, SCREEN_SIZE[1] // SQUARE_SIZE)

initial_state: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

first_square_pos: tuple[int, int] = (
    SCREEN_SQUARE_SIZE[0] // 2 - len(initial_state[0]) // 2 - 1,
    SCREEN_SQUARE_SIZE[1] // 2 - len(initial_state) // 2 - 1)


def main():
    grid: list[list[int]] = init_grid()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    done = False

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(2)
        grid = update_grid(grid)

    pygame.quit()


def init_grid():
    grid: list[list[int]] = [
        [0 for _ in range(SCREEN_SQUARE_SIZE[0])]
        for _ in range(SCREEN_SQUARE_SIZE[1])
    ]

    for init_y in range(len(initial_state)):
        for init_x in range(len(initial_state[init_y])):
            grid[init_y + first_square_pos[1]][init_x + first_square_pos[0]] = \
                initial_state[init_y][init_x]
    return grid


def update_grid(grid: list[list[int]]) -> list[list[int]]:
    temp_grid: list[list[int]] = [[0 for _ in range(GRID_SIZE[0])] for
                                  _ in range(GRID_SIZE[1])]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            temp_grid[y][x] = get_next_state(x, y, grid)

    return temp_grid


def count_neighbors(x, y, grid):
    count = 0
    for neighbor in NEIGHBORS:
        if 0 <= x + neighbor[0] < GRID_SIZE[0] and \
                0 <= y + neighbor[1] < GRID_SIZE[1]:
            count += grid[y + neighbor[1]][x + neighbor[0]]
    return count


def get_next_state(x, y, grid):
    neighbors = count_neighbors(x, y, grid)
    if neighbors == 3:
        return 1

    if neighbors < 2 or neighbors > 3:
        return 0

    return grid[y][x]


def draw_grid(screen, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                draw_void(screen, x, y)
            else:
                draw_square(screen, x, y)


def draw_square(screen, x: int, y: int):
    pos_x = x * SQUARE_SIZE
    pos_y = y * SQUARE_SIZE
    pygame.draw.rect(screen, SQUARE_BORDER_COLOR,
                     (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, SQUARE_COLOR,
                     (pos_x + 1, pos_y + 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2))


def draw_void(screen, x: int, y: int):
    pos_x = x * SQUARE_SIZE
    pos_y = y * SQUARE_SIZE
    pygame.draw.rect(screen, (255, 255, 255),
                     (pos_x, pos_y, SQUARE_SIZE, SQUARE_SIZE))


main()
