from pygame import Vector2

#two dimensionnal point 
class TwoDPoint():
    x: float
    y: float

#allow to set 2d points with the given point and xy entries 
def set2DPoint(p: TwoDPoint, _x: float, _y: float) -> TwoDPoint:
    p.x = _x
    p.y = _y
    return p

#get Pygame Native Point
def getNativePoint(p: TwoDPoint)-> Vector2:
    v: Vector2 = Vector2()
    v.x, v.y = p.x, p.y
    return v
