"""
Custom types and type shortcuts
"""

from typing import Literal
import pygame


Screen = pygame.surface.Surface

CellState = Literal[0, 1]
CellsRow = list[CellState]
CellsMatrix = list[CellsRow]

Coordinates = tuple[int, int]
