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
    def getType(self):
        pass


class Wall(Tile):

    def __init__(self, x, y, width, height, blocking = True):
        super().__init__(x, y, width, height, blocking)
        self.image = pygame.image.load('src/Textures/Industrial/CROSSCUBE.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def getType(self):
        return "wall"


class Floor(Tile):

    def __init__(self, x, y, width, height, blocking = False):
        super().__init__(x, y, width, height, blocking)
        self.image = pygame.image.load('src/Textures/Wood/CREAKYWOOD.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        

    def getType(self):
        return "floor"


class Active(Tile):
     
    def __init__(self, x, y, width, height, blocking = False):
        super().__init__(x, y, width, height, blocking)
         
    @abstractmethod
    def getType(self):
        pass

class Passive(Tile):
     
    def __init__(self, x, y, width, height, blocking = False):
        super().__init__(x, y, width, height, blocking)
        
    @abstractmethod
    def getType(self):
        pass

class Door(Passive):

    def __init__(self, x, y, width, height, id, blocking = True):
        super().__init__(x, y, width, height, blocking)
        self.id = id
        self.image = pygame.image.load('src/Textures/Doors/CREAKYDOOR.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.master = None
    def getType(self):
        return "door"

    def switch(self,action):
        if action == 'open':
            self.blocking = False
            self.image = pygame.image.load('src/Textures/Urban/PAVEMENT.png').convert()
        elif action == 'close':
            self.blocking = True
            self.image = pygame.image.load('src/Textures/Doors/CREAKYDOOR.png').convert()




class Switch(Active):

    def __init__(self, x, y, width, height, slave,action,blocking = False):
        super().__init__(x, y, width, height, blocking)
        self.image = pygame.image.load('src/Textures/Tech/BIGSQUARES.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.slave = slave
        self.action = action
        self.player = None
        #TODO place player
    def getType(self):
        return "switch"
    
    def onEnter(self):
        self.slave.switch(self.action)
        print("Entered")




