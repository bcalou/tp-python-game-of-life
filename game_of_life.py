import pygame
from pygame import Vector2, color
from wac_render.wac_3DPoint import ThreeDPoint, set3DPoint
from wac_render.wac_pointConverter import rotateAxisX, rotateAxisY, rotateAxisZ
from wac_render.wac_var import WIDTH, HEIGHT, SIZE_X, SIZE_Y
from wac_render.wac_3DPolygon import ThreeDPolygon, get3Dpoints,getNativePointList, print3DPolygon
from wac_cube.wac_3DCube import generate3DCube
from wac_rules.wac_basicgrid import initial_state, IndexCube, setIndexCube
from wac_rules.wac_gameoflife import get_next_state

#init pygame framework
pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((HEIGHT, WIDTH))

clock = pygame.time.Clock()

animated: bool = False

done: bool = False

cubes: list[list[ThreeDPolygon]] = []

#generate cube grid
for i in range(SIZE_X):
    for j in range(SIZE_Y):
        cubes.append(generate3DCube(i * 100,j * 100))

#enalbel rotation
def Rotate_polygon(poly: ThreeDPolygon, timeline: float )-> None:
    for i in range(len(poly.points)):
        _p: ThreeDPoint = rotateAxisX(poly.points[i], timeline)
        set3DPoint(poly.points[i],_p.x,_p.y,_p.z)

#get closest polygon from a couple a polygons
# -> a very simple ray caster !
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

#permutate two polygons in a list with indexes
def permutate_in_array(l: list[ThreeDPolygon], a: int, b: int)-> list[ThreeDPolygon]:
    tmp: ThreeDPolygon = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l

#return list of three d polygons with layers
def Get3DPolygonLayers(layer_list: list[ThreeDPolygon])-> list[ThreeDPolygon]:
    for i in range (len(layer_list)):
        for j in range (i+1, len(layer_list)):
          current: ThreeDPolygon = GetClosest_polygon(layer_list[i], layer_list[j]);
          if (current == layer_list[i]):
            layer_list = permutate_in_array(layer_list, i,j);
    return layer_list

time: float = 20


#enable rotation
for i in range (len(cubes)):
    for j in range(len(cubes[i])):
        Rotate_polygon(cubes[i][j], time)

world: list[list[int]] = initial_state

#the real time loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    if(animated):
        #enable rotation
        for i in range (len(cubes)):
            for j in range(len(cubes[i])):
                Rotate_polygon(cubes[i][j], time)
        time = time + 0.5

    #reajust layers
    for i in range (len(cubes)):
        for j in range(len(cubes[i])):
            cubes[i] = Get3DPolygonLayers(cubes[i])

    x: int = 0
    y: int = 0
    for i in range (len(cubes)):
        if(x == SIZE_X):
            y = y + 1
            x = 0
        if(world[x][y] == 1):
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
        x = x + 1


    pygame.display.flip()

    #launch the world evolution
    world = get_next_state(world)

    clock.tick(1)



pygame.quit()
