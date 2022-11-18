from typing import TypedDict


class Coords(TypedDict):
    y: int
    x: int


GameState: list[list[int]]
