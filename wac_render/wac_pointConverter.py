from wac_render.wac_2DPoint import TwoDPoint, set2DPoint
from wac_render.wac_3DPoint import ThreeDPoint, print3DPoint, set3DPoint
import math 
def convertPoint(height_screen:int, width_screen:int, _p: ThreeDPoint):
    x2D: int = (int) (height_screen / 2 +_p.y)
    y2D: int = (int) (width_screen / 2 +_p.z)
    p: TwoDPoint = TwoDPoint()
    p = set2DPoint(p, x2D, y2D)
    return p

def rotateAxisX(_point: ThreeDPoint, degres: float)-> ThreeDPoint:
    radius: float = math.sqrt(_point.y*_point.y + _point.z*_point.z )
    theta: float = math.atan2(_point.y, _point.z)
    theta += 2*math.pi/360*degres
    new_point : ThreeDPoint = ThreeDPoint()
    set3DPoint(new_point, radius * math.sin(theta),_point.x + 50 ,radius * math.cos(theta))
    return new_point

def rotateAxisY(_point: ThreeDPoint, degres: float)-> ThreeDPoint:
    radius: float = math.sqrt(_point.x*_point.x + _point.z*_point.z )
    theta: float = math.atan2(_point.x, _point.z)
    theta += 2*math.pi/360*degres
    new_point : ThreeDPoint = ThreeDPoint()
    set3DPoint(new_point, radius * math.sin(theta),_point.y  ,radius * math.cos(theta))
    return new_point
