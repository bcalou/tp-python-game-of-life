from pygame.event import clear
from wac_render.wac_2DPoint import TwoDPoint, getNativePoint
from wac_render.wac_3DPoint import ThreeDPoint
from wac_render.wac_2DPolygon import TwoDPolygon, addPoint
from wac_render.wac_pointConverter import convertPoint
from wac_render.wac_var import WIDTH, HEIGHT
from pygame import Vector2

#three dimensional point
class ThreeDPolygon():
    points : list[ThreeDPoint] = []

#enable to set a three dimensional polygon as a list of three dimensional points
def set3DPolygon(poly: ThreeDPolygon, l: list[ThreeDPoint])-> ThreeDPolygon:
    clear3Dpoints(poly)
    poly.points = l
    return poly

#get a transformed three dimensional polygon as two dimensional polygon
def get2DPolygon(poly: ThreeDPolygon) -> TwoDPolygon:
    plain_poly : TwoDPolygon = TwoDPolygon()
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        addPoint(plain_poly, p)
    return plain_poly

#get a transformed three dimensional polygon as pygame native Vector 2 point list
def getNativePointList(poly: ThreeDPolygon) -> list[Vector2]:
    v2list: list[Vector2] = []
    print("len" + str(len(poly.points)))
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        v2list.append(getNativePoint(p))
    return v2list

#clear all the point associated with the given polygon
def clear3Dpoints(poly: ThreeDPolygon):
    poly.points.clear()

#tool for debugging
def  print2DPolygon(poly: ThreeDPolygon):
    print("----polygon :")
    for i in range(0, len(poly.points)):
        p: TwoDPoint = convertPoint(WIDTH, HEIGHT,poly.points[i])
        print("{" + str(p.x) + " - " + str(p.y) + " }")
        
#tool for debugging
def  print3DPolygon(poly: ThreeDPolygon):
    print("----polygon :")
    for i in range(0, len(poly.points)):
        p: ThreeDPoint = poly.points[i]
        print("{" + str(p.x) + " - " + str(p.y) + " - " + str(p.z) +" }")

#get all the 3d point from polygon
def get3Dpoints(poly: ThreeDPolygon)-> list[ThreeDPoint]:
    return poly.points
