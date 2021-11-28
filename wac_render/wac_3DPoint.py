#two dimensionnal point 
class ThreeDPoint():
    x: float
    y: float
    z: float

#allow to set 3d points with the given point and xyz entries 
def set3DPoint(p: ThreeDPoint, _x: float, _y: float, _z: float) -> ThreeDPoint:
    p.x = _x
    p.y = _y
    p.z = _z
    return p

#a tool for debugging
def print3DPoint(p: ThreeDPoint) -> None:
    print(str(p.x) + " " + str(p.y) + " " + str(p.z))