from wac_render.wac_3DPolygon import ThreeDPolygon, print3DPolygon, get3Dpoints, get2DPolygon, set3DPolygon,getNativePointList,print2DPolygon
from wac_render.wac_3DPoint import ThreeDPoint, print3DPoint, set3DPoint, print3DPoint


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

    set3DPoint(_left[0], 0+offset_x, 0, 0 + offset_y)
    set3DPoint(_left[1], 100+offset_x, 0, 0+ offset_y)
    set3DPoint(_left[2], 100+offset_x, 100, 0+ offset_y)
    set3DPoint(_left[3], 0+offset_x, 100, 0+ offset_y)

    set3DPoint(_right[0], 0+offset_x, 0, 100+ offset_y)
    set3DPoint(_right[1], 100+offset_x, 0, 100+ offset_y)
    set3DPoint(_right[2], 100+offset_x, 100, 100+ offset_y)
    set3DPoint(_right[3], 0+offset_x, 100, 100+ offset_y)

    set3DPoint(_top[0], 100+offset_x,  0, 0+ offset_y)
    set3DPoint(_top[1], 100+offset_x, 100, 0+ offset_y)
    set3DPoint(_top[2], 100+offset_x, 100, 100+ offset_y)
    set3DPoint(_top[3], 100+offset_x, 0, 100+ offset_y)

    set3DPoint(_bottom[0], 0+offset_x, 0, 0+ offset_y)
    set3DPoint(_bottom[1], 0+offset_x, 100, 0+ offset_y)
    set3DPoint(_bottom[2], 0+offset_x, 100, 100+ offset_y)
    set3DPoint(_bottom[3], 0+offset_x, 0, 100+ offset_y)

    set3DPoint(_front[0], 0+offset_x, 100, 100+ offset_y)
    set3DPoint(_front[1], 100+offset_x, 100, 100+ offset_y)
    set3DPoint(_front[2], 100+offset_x, 100, 0+ offset_y)
    set3DPoint(_front[3], 0+offset_x, 100, 0+ offset_y)

    set3DPoint(_back[0], 0+offset_x, 100, 100+ offset_y)
    set3DPoint(_back[1], 100+offset_x, 100, 100+ offset_y)
    set3DPoint(_back[2], 100+offset_x, 100, 0+ offset_y)
    set3DPoint(_back[3], 0+offset_x, 100, 0+ offset_y)

    set3DPolygon(cube[0], _left)
    set3DPolygon(cube[1], _right)
    set3DPolygon(cube[2], _top)
    set3DPolygon(cube[3], _bottom)
    set3DPolygon(cube[4], _front)
    #ajouter back !!!

    return cube