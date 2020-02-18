import pygame
import Tile

tilesize = 32

class DungeonMap():
    """
    Represents the game map
    """

    def __init__(self,width=200, height=200, level="level.txt"):

        self.window = pygame.display.set_mode((width, height))
        #self.background = pygame.image.load('src/bg.jpg')
        self.walls = self.loadWalls(level)
        self.block_list = []
        for wall in self.walls:
            if wall.blocking == True:
                for i in range(0,32):
                    for j in range(0,32):
                        self.block_list.append((wall.x+i-8,wall.y+j-16))



    def drawMap(self):
        #self.window.blit(self.background,(0,0))
        for wall in self.walls:
            #print(wall.type)
            wall.draw(self.window)


    def loadWalls(self,level):
        tiles = []
        x = -64
        y = -64
        file = open(level)
        #header = file.readline()
        lines = file.read().split()
        for line in lines:
            chars = list(line)
            for char in chars:
                if char == '#':
                    tiles.append(Tile.Wall(x,y,32,32))
                elif char == '.':
                    tiles.append(Tile.Floor(x,y,32,32))
                print(char)
                x += 32
            y += 32
            x = 0
        #print(header.split(" "))
        return tiles#[ (Tile.Tile(250,250,40,40)),(Tile.Tile(350,350,40,40)),(Tile.Tile(450,450,40,40)) ]


