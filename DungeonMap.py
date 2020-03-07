import pygame
import Tile
from pygame.locals import *
tilesize = 32

class DungeonMap():
    """
    Represents the game map
    """

    def __init__(self,width, height, level, doors, switches):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height),RESIZABLE|HWSURFACE|DOUBLEBUF)#|FULLSCREEN)
        #self.background = pygame.image.load('src/bg.jpg')
        self.level = self.loadLevel(level,doors,switches)
        self.tiles = pygame.sprite.Group()
        for block in self.level:
            self.tiles.add(block)

    def getPathTo(self,fromPos,toPos):
        if fromPos == toPos:
            return [[0,0]]
        result = []
        Qset = []
        Q2set = []
        prevDict = { }
        distDict = { }
        for x in range(0,self.width,32):
            for y in range(0,self.height,32):
                Qset.append([x,y])
                distDict[x,y] = 1000000
                prevDict[x,y] = [-1,-1]

        Q2set = Qset
        distDict[fromPos[0],fromPos[1]] = 0

        while (len(Qset)!= 0):
            u = Qset[0]
            for elem in Qset:
                if distDict[elem[0],elem[1]] < distDict[u[0],u[1]]:
                    u = elem
            Qset.remove(u)
            for i in range(-32,128,32):
                for j in range(-32,128,32):
                    newPos = [u[0]+i,u[1]+j]
                    newItPos = newPos
                    newDist = distDict[u[0],u[1]] + 1
                    if newPos[0] in range(0,576) and newPos[1] in range(0,288):
                        if newDist < distDict[newPos[0],newPos[1]] and newItPos[0] <= 576 and newItPos[1] <= 288:

                            distDict[newPos[0],newPos[1]] = newDist
                            prevDict[newPos[0],newPos[1]] = u
            
        currentPos = toPos
        while(currentPos != fromPos):
            result.append(currentPos)
            currentPos = prevDict[currentPos[0],currentPos[1]]

        result.reverse()

        return result
        

    def findTile(self,pos): 
        for tile in self.level:
            if tile.rect.x == pos[0] and tile.rect.y == pos[1]:
                return tile
        print("Failed searchpos: ", pos)
        return None

    def drawMap(self):
        self.tiles.update()
        self.tiles.draw(self.window)

    

    def loadLevel(self,level,doors,switches):
        tiles = []
        x = 0
        y = 0
        print(level)
        file = open(level)
        lines = file.read().split()
        for line in lines:
            chars = list(line)
            for char in chars:
                if char == '#':
                    tiles.append(Tile.Wall(x,y,32,32))
                elif char == '.':
                    tiles.append(Tile.Floor(x,y,32,32))
                x += 32
            y += 32
            x = 0
        doors_list = []
        for d in doors:
            chars = str(d[1]).split()
            door = Tile.Door(int(chars[0]),int(chars[1]),int(chars[2]),int(chars[3]),chars[4])
            tiles.append(door)
            doors_list.append(door)
        for s in switches:
            chars = str(s[1]).split()
            for do in doors_list:
                if do.id == chars[4]:
                    tiles.append(Tile.Switch(int(chars[0]),int(chars[1]),int(chars[2]),int(chars[3]),do, chars[5]))
            
        return tiles