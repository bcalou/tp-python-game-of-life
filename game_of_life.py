import pygame
from pygame import Color, color
from pygame.draw import polygon
from wac_render.wac_3DPoint import ThreeDPoint, print3DPoint, set3DPoint, print3DPoint
from wac_render.wac_pointConverter import convertPoint, rotateAxisX, rotateAxisY
from wac_render.wac_var import WIDTH, HEIGHT
from wac_render.wac_3DPolygon import ThreeDPolygon, print3DPolygon, get3Dpoints,get2DPolygon, set3DPolygon,getNativePointList,print2DPolygon
from wac_cube.wac_3DCube import generate3DCube
pygame.init()


screen: pygame.surface.Surface = pygame.display.set_mode((HEIGHT, WIDTH))

clock = pygame.time.Clock()

done: bool = False

cubes: list[list[ThreeDPolygon]] = []

for i in range(100):
    for j in range(100):
        cubes.append(generate3DCube(i * 100,j * 100))

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
for i in range (len(cubes)):
    for j in range(len(cubes[i])):
        Rotate_polygon(cubes[i][j], 1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    #reajust layers 
    for i in range (len(cubes)):
        for j in range(len(cubes[i])):
            cubes[i] = Get3DPolygonLayers(cubes[i])

    for i in range (len(cubes)):
        for j in range(len(cubes[i])):
            c: color
            if (j == 0):
                c = (0,255,255)
            if (j == 1):
                c = (255,0,255)
            if (j == 2):
                c = (255,255,0)
            if (j == 3):
                c = (0,255,0)
            if (j == 4):
                c = (0,0,255)
            pygame.draw.polygon(surface=screen, color=c, points=getNativePointList(cubes[i][j]))

    pygame.display.flip()
    #print("time " + str(time))

    time = time + 5

    #print("Update !")
    clock.tick(5)



pygame.quit()