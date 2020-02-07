import pygame

floor = pygame.image.load('src/Textures/Wood/CREAKYWOOD.png')
wall = pygame.image.load('src/Textures/Industrial/CROSSCUBE.png')

class Tile():

    def __init__(self,x,y,width,height,blocking= True,type = "Wall"):
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
        self.type = type


    def draw(self,window):
        if self.type == 'wall':
            window.blit(wall,(self.x, self.y, self.width, self.height))

        elif self.type == 'floor':
            window.blit(floor, (self.x, self.y, self.width, self.height))