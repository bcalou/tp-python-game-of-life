"""Fichier de paramètres du jeu"""

from typing import List

# Alias de types

Array2 = List[List[int]]

# Couleurs

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'gray': (128, 128, 128),
    'pink': (255, 153, 153),
}

# Paramètres : preset

PRESET_NAME: str = "Canon"  # ex: Glider, Blinker, Toad, Pulsar, Canon
PRESET_COLOR: tuple = COLORS['white']

# Paramètres : écran

SCREEN_SIZE: tuple[int, int] = (1200, 700)
CELL_SIZE: int = 5
FRAME_RATE: int = 50
