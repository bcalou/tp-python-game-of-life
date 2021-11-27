from pygame.event import clear
from wac_render.wac_2DPoint import TwoDPoint, getNativePoint
from wac_render.wac_3DPoint import ThreeDPoint
from wac_render.wac_2DPolygon import TwoDPolygon, addPoint
from wac_render.wac_pointConverter import convertPoint
from wac_render.wac_var import WIDTH, HEIGHT
from pygame import Vector2


class ThreeDPolygon():
    points : list[ThreeDPoint] = []

def set3DPolygon(poly: ThreeDPolygon, l: list[ThreeDPoint])-> ThreeDPolygon:
    clear3Dpoints(poly)
    poly.points = l
    return poly

def get2DPolygon(poly: ThreeDPolygon) -> TwoDPolygon:
    plain_poly : TwoDPolygon = TwoDPolygon()
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        addPoint(plain_poly, p)
    return plain_poly

def getNativePointList(poly: ThreeDPolygon) -> list[Vector2]:
    v2list: list[Vector2] = []
    print("len" + str(len(poly.points)))
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        v2list.append(getNativePoint(p))
    return v2list

def clear3Dpoints(poly: ThreeDPolygon):
    poly.points.clear()

def  print2DPolygon(poly: ThreeDPolygon):
    print("----polygon :")
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        print("{" + str(p.x) + " - " + str(p.y) + " }")
        

def  print3DPolygon(poly: ThreeDPolygon):
    print("----polygon :")
    for i in range(0, len(poly.points)):
        p: ThreeDPoint = poly.points[i]
        print("{" + str(p.x) + " - " + str(p.y) + " - " + str(p.z) +" }")
        
def get3Dpoints(poly: ThreeDPolygon)-> list[ThreeDPoint]:
    return poly.points
