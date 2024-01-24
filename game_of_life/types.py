from typing import Literal

CellState = Literal[0, 1]
CellsRow = list[CellState]
CellsMatrix = list[CellsRow]

Coordinates = tuple[int, int]
