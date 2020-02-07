import pygame
import Tile

tilesize = 32

class DungeonMap():
    """
    Represents the game map
    """

    def __init__(self,width=200, height=200):

        self.window = pygame.display.set_mode((width, height))
        #self.background = pygame.image.load('src/bg.jpg')
        self.walls = self.loadWalls()

    def drawMap(self):
        #self.window.blit(self.background,(0,0))
        for wall in self.walls:
            #print(wall.type)
            wall.draw(self.window)

    def loadWalls(self):
        tiles = []
        x = 0
        y = 0
        file = open("level.txt")
        #header = file.readline()
        lines = file.read().split()
        for line in lines:
            chars = list(line)
            for char in chars:
                if char == '#':
                    tiles.append(Tile.Tile(x,y,32,32,type='wall'))
                elif char == '.':
                    tiles.append(Tile.Tile(x,y,32,32,type='floor'))
                print(char)
                x += 32
            y += 32
            x = 0
        #print(header.split(" "))
        return tiles#[ (Tile.Tile(250,250,40,40)),(Tile.Tile(350,350,40,40)),(Tile.Tile(450,450,40,40)) ]


