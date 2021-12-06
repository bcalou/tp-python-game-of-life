from wac_render.wac_3DPolygon import ThreeDPolygon, print3DPolygon, get3Dpoints, get2DPolygon, set3DPolygon,getNativePointList,print2DPolygon
from wac_render.wac_3DPoint import ThreeDPoint, print3DPoint, set3DPoint, print3DPoint

#enable creation of 3d cube with x and y offset as inputs
def generate3DCube(offset_x: float, offset_y: float) -> list[ThreeDPolygon] :
    cube: list[ThreeDPolygon] = []

    #instanciate square faces as polygons
    for i in range(0, 5):
        _p: ThreeDPolygon  = ThreeDPolygon()
        cube.append(_p)

    _left: list[ThreeDPoint] = []
    _right: list[ThreeDPoint] = []
    _top: list[ThreeDPoint] = []
    _bottom: list[ThreeDPoint] = []
    _front: list[ThreeDPoint] = []
    _back: list[ThreeDPoint] = []

    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _left.append(point)
    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _right.append(point)
    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _top.append(point)
    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _bottom.append(point)
    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _front.append(point)
    for i in range(0, 4):
        point: ThreeDPoint  = ThreeDPoint()
        _back.append(point)

    scale: int = 100

    set3DPoint(_left[0], -scale/2+offset_x, -scale/2,-scale/2 + offset_y)
    set3DPoint(_left[1], scale/2+offset_x, -scale/2, -scale/2+ offset_y)
    set3DPoint(_left[2], scale/2+offset_x, scale/2, -scale/2+ offset_y)
    set3DPoint(_left[3], -scale/2+offset_x, scale/2,-scale/2+ offset_y)

    set3DPoint(_right[0], -scale/2+offset_x, -scale/2, scale/2+ offset_y)
    set3DPoint(_right[1], scale/2+offset_x, -scale/2, scale/2+ offset_y)
    set3DPoint(_right[2], scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_right[3], -scale/2+offset_x, scale/2, scale/2+ offset_y)

    set3DPoint(_top[0], scale/2+offset_x,  -scale/2, -scale/2 + offset_y)
    set3DPoint(_top[1], scale/2+offset_x, scale/2,  -scale/2 + offset_y)
    set3DPoint(_top[2], scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_top[3], scale/2+offset_x, -scale/2, scale/2+ offset_y)

    set3DPoint(_bottom[0], -scale/2+offset_x, -scale/2, -scale/2+ offset_y)
    set3DPoint(_bottom[1], -scale/2+offset_x, scale/2, -scale/2+ offset_y)
    set3DPoint(_bottom[2], -scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_bottom[3], -scale/2+offset_x, -scale/2, scale/2+ offset_y)

    set3DPoint(_front[0], -scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_front[1], scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_front[2], scale/2+offset_x, scale/2, -scale/2+ offset_y)
    set3DPoint(_front[3], -scale/2+offset_x, scale/2, -scale/2+ offset_y)

    set3DPoint(_back[0], -scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_back[1], scale/2+offset_x, scale/2, scale/2+ offset_y)
    set3DPoint(_back[2], scale/2+offset_x, scale/2, -scale/2+ offset_y)
    set3DPoint(_back[3], -scale/2+offset_x, scale/2, -scale/2+ offset_y)

    set3DPolygon(cube[0], _left)
    set3DPolygon(cube[1], _right)
    set3DPolygon(cube[2], _top)
    set3DPolygon(cube[3], _bottom)
    set3DPolygon(cube[4], _front)
    #ajouter back !!!

    return cube
