import pygame
from abc import abstractmethod, ABC



class Tile(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,blocking= True):
        """
        :param x: x-coord int
        :param y: y-coord int
        :param width: width int
        :param height: height int
        :param blocking: path blocking = True
        :param type: type = "wall"
        """
        pygame.sprite.Sprite.__init__(self)
        self.blocking = blocking

    @abstractmethod     
    def getType():
        pass

 #   @abstractmethod
  #  def draw(self,window):
  #      pass

class Wall(Tile):

    def __init__(self, x, y, width, height, blocking = True):
        super().__init__(x, y, width, height, blocking)
        self.image = pygame.image.load('src/Textures/Industrial/CROSSCUBE.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def getType():
        return "wall"

#    def draw(self,window):
 #       self.image.draw(window)       

class Floor(Tile):

    def __init__(self, x, y, width, height, blocking = False):
        super().__init__(x, y, width, height, blocking)
        self.image = pygame.image.load('src/Textures/Wood/CREAKYWOOD.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        

    def getType():
        return "floor"

  #  def draw(self,window):
   #
   #      self.image.draw(window)
        

        