CELL_SIZE: int = 20
BLACK_COLOR: tuple[int, int, int] = (0, 0, 0)
WHITE_COLOR: tuple[int, int, int] = (255, 255, 255)

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 800

NEIGHBORS: list[tuple[int, int]] = [
    # (height, width)
    (-1, -1),  # Top left
    (-1, 0),  # Top
    (-1, 1),  # Top right
    (0, -1),  # Left
    (0, 1),  # Right
    (1, -1),  # Bottom left
    (1, 0),  # Bottom
    (1, 1),  # Bottom right
]
