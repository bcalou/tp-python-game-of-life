import pygame
from pygame import Color, color
from pygame.draw import polygon
from wac_render.wac_3DPoint import ThreeDPoint, print3DPoint, set3DPoint, print3DPoint
from wac_render.wac_pointConverter import convertPoint, rotateAxisX, rotateAxisY
from wac_render.wac_var import WIDTH, HEIGHT
from wac_render.wac_3DPolygon import ThreeDPolygon, print3DPolygon, get3Dpoints,get2DPolygon, set3DPolygon,getNativePointList,print2DPolygon

pygame.init()


screen: pygame.surface.Surface = pygame.display.set_mode((HEIGHT, WIDTH))

clock = pygame.time.Clock()

done: bool = False

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

set3DPoint(_left[0], 0, 0, 0)
set3DPoint(_left[1], 100, 0, 0)
set3DPoint(_left[2], 100, 100, 0)
set3DPoint(_left[3], 0, 100, 0)

set3DPoint(_right[0], 0, 0, 100)
set3DPoint(_right[1], 100, 0, 100)
set3DPoint(_right[2], 100, 100, 100)
set3DPoint(_right[3], 0, 100, 100)

set3DPoint(_top[0], 100,  0, 0)
set3DPoint(_top[1], 100, 100, 0)
set3DPoint(_top[2], 100, 100, 100)
set3DPoint(_top[3], 100, 0, 100)

set3DPoint(_bottom[0], 0, 0, 0)
set3DPoint(_bottom[1], 0, 100, 0)
set3DPoint(_bottom[2], 0, 100, 100)
set3DPoint(_bottom[3], 0, 0, 100)

set3DPoint(_front[0], 0, 100, 100)
set3DPoint(_front[1], 100, 100, 100)
set3DPoint(_front[2], 100, 100, 0)
set3DPoint(_front[3], 0, 100, 0)

set3DPoint(_back[0], 0, 100, 100)
set3DPoint(_back[1], 100, 100, 100)
set3DPoint(_back[2], 100, 100, 0)
set3DPoint(_back[3], 0, 100, 0)

set3DPolygon(cube[0], _left)
set3DPolygon(cube[1], _right)
set3DPolygon(cube[2], _top)
set3DPolygon(cube[3], _bottom)
set3DPolygon(cube[4], _front)
#ajouter back !!!

def Rotate_polygon(poly: ThreeDPolygon, timeline: float )-> None:
    for i in range(len(poly.points)):
        #set3DPoint(poly.points[i],rotateAxisY(poly.points[i], timeline).x,rotateAxisY(poly.points[i], timeline).y,rotateAxisY(poly.points[i], timeline).z)
        set3DPoint(poly.points[i],rotateAxisX(poly.points[i], timeline).x,rotateAxisX(poly.points[i], timeline).y,rotateAxisX(poly.points[i], timeline).z)

def GetClosest_polygon(un: ThreeDPolygon, deux: ThreeDPolygon) -> ThreeDPolygon:
    somme_x: float = 0
    for i in range(len(get3Dpoints(un))):
        somme_x = somme_x + get3Dpoints(un)[i].x
    moyenne_x_un: float = somme_x / len(get3Dpoints(un))

    somme_x: float = 0
    for i in range(len(get3Dpoints(deux))):
        somme_x = somme_x + get3Dpoints(deux)[i].x
    moyenne_x_deux: float = somme_x / len(get3Dpoints(deux))

    if(moyenne_x_un > moyenne_x_deux):
        return deux
    return un

def permutate_in_array(l: list[ThreeDPolygon], a: int, b: int)-> list[ThreeDPolygon]:
    tmp: ThreeDPolygon = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l

def Get3DPolygonLayers(layer_list: list[ThreeDPolygon])-> list[ThreeDPolygon]:
    for i in range (len(layer_list)):
        for j in range (i+1, len(layer_list)):
          current: ThreeDPolygon = GetClosest_polygon(layer_list[i], layer_list[j]);
          if (current == layer_list[i]):
            layer_list = permutate_in_array(layer_list, i,j);
    return layer_list

time : float = 0

#enable rotation
for i in range (len(cube)):
    Rotate_polygon(cube[i], 1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    #print3DPolygon(cube[0])

    cube = Get3DPolygonLayers(cube)

    for i in range(len(cube)):
        c: color
        if (i == 0):
            c = (0,255,255)
        if (i == 1):
            c = (255,0,255)
        if (i == 2):
            c = (255,255,0)
        if (i == 3):
            c = (0,255,0)
        if (i == 4):
            c = (0,0,255)
        pygame.draw.polygon(surface=screen, color=c, points=getNativePointList(cube[i]))

    pygame.display.flip()
    #print("time " + str(time))

    time = time + 5

    #print("Update !")
    clock.tick(5)



pygame.quit()