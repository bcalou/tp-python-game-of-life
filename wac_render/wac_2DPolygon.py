from wac_render.wac_2DPoint import TwoDPoint
from wac_render.wac_3DPoint import ThreeDPoint

class TwoDPolygon():
    points : list[TwoDPoint]


def addPoint(poly:TwoDPolygon, p: TwoDPoint):
        poly.points.append(p)