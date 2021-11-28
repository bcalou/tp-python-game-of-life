from wac_render.wac_2DPoint import TwoDPoint
from wac_render.wac_3DPoint import ThreeDPoint

#Two dimensional polygon
class TwoDPolygon():
    points : list[TwoDPoint]

#add point to the list embeded in the twoDPolygon p
def addPoint(poly:TwoDPolygon, p: TwoDPoint):
        poly.points.append(p)