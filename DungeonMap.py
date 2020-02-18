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
        self.level = self.loadLevel(level)
        self.tiles = pygame.sprite.Group()
        self.blockingSprites = pygame.sprite.Group()
        for block in self.level:
            self.tiles.add(block)
            if block.blocking == True:
                self.blockingSprites.add(block)
                


    def drawMap(self):
        #self.window.blit(self.background,(0,0))
        self.tiles.update()
        self.tiles.draw(self.window)


    def loadLevel(self,level):
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


