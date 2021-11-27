from pygame import Vector2

class TwoDPoint():
    x: float
    y: float

def set2DPoint(p: TwoDPoint, _x: float, _y: float) -> TwoDPoint:
    p.x = _x
    p.y = _y
    return p

def getNativePoint(p: TwoDPoint)-> Vector2:
    v: Vector2 = Vector2()
    v.x, v.y = p.x, p.y
    return v
