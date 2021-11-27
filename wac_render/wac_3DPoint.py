class ThreeDPoint():
    x: float
    y: float
    z: float

def set3DPoint(p: ThreeDPoint, _x: float, _y: float, _z: float) -> ThreeDPoint:
    p.x = _x
    p.y = _y
    p.z = _z
    return p

def print3DPoint(p: ThreeDPoint) -> None:
    print(str(p.x) + " " + str(p.y) + " " + str(p.z))