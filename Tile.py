import pygame
from abc import abstractmethod, ABC



class Tile(ABC):

    def __init__(self,x,y,width,height,blocking= True):
        """
        :param x: x-coord int
        :param y: y-coord int
        :param width: width int
        :param height: height int
        :param blocking: path blocking = True
        :param type: type = "wall"
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blocking = blocking

    @abstractmethod     
    def getType():
        pass

    @abstractmethod
    def draw(self,window):
        pass

class Wall(Tile):

    def __init__(self, x, y, width, height, blocking = True):
        super().__init__(x, y, width, height, blocking)
        self.wall = pygame.image.load('src/Textures/Industrial/CROSSCUBE.png')

    def getType():
        return "wall"

    def draw(self,window):
        window.blit(self.wall,(self.x, self.y, self.width, self.height))
        

class Floor(Tile):

    def __init__(self, x, y, width, height, blocking = False):
        super().__init__(x, y, width, height, blocking)
        self.floor = pygame.image.load('src/Textures/Wood/CREAKYWOOD.png')

    def getType():
        return "floor"

    def draw(self,window):
        window.blit(self.floor,(self.x, self.y, self.width, self.height))


        