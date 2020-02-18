import DungeonMap
import pygame
import random
from abc import abstractmethod, ABC

keys = 0
counter = 0


class Character(ABC):

    def __init__(self,x,y,width,height,vel,_map):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self._map = _map
        #TODO plazer model based on type
        self.left = pygame.image.load('src/Character/1.png')
        self.right = pygame.image.load('src/Character/4.png')
        self.up = pygame.image.load('src/Character/2.png')
        self.down = pygame.image.load('src/Character/3.png')
        self.walkCount = 0
        self.walkDirection = 8


    @abstractmethod
    def walk(self, window):
        pass

class Player(Character):
    def __init__(self,x,y,width,height,vel,_map):
        super().__init__(x,y,width,height,vel,_map)

    def walk(self, window):
        
        oldX = self.x
        oldY = self.y
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.walkDirection = 4


        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.walkDirection = 6


        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.walkDirection = 8

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.walkDirection = 2

        newPosition = (self.x,self.y)
        #print(newPosition)
        for var in range(0,self.width):
                if (newPosition[0]+var,newPosition[1]+var) in self._map.block_list:
                    self.x = oldX
                    self.y = oldY
        if self.walkDirection == 4: 
            window.blit(self.left, (self.x, self.y, self.width, self.height))
                      
        elif self.walkDirection == 6:
            window.blit(self.right, (self.x, self.y, self.width, self.height))

        elif self.walkDirection == 8:
            window.blit(self.up, (self.x, self.y, self.width, self.height))

        elif self.walkDirection == 2:
            window.blit(self.down, (self.x, self.y, self.width, self.height))

        


class WeakNpc(Character):
    def __init__(self,x,y,width,height,vel,_map):
        super().__init__(x,y,width,height,vel,_map)

    def walk(self, window):
        
        global counter
        global keys
        counter += 1
        
        if counter > keys+4:
            counter = 0
            keys =  random.randrange(1, 5, 1)

        if keys == 1:
            self.x -= self.vel
            self.walkDirection = 4


        if keys == 2:
            self.x += self.vel
            self.walkDirection = 6


        if keys == 3:
            self.y -= self.vel
            self.walkDirection = 8

        if keys == 4:
            self.y += self.vel
            self.walkDirection = 2


        if self.walkDirection == 4: 
            window.blit(self.left, (self.x, self.y, self.width, self.height))           
                
        elif self.walkDirection == 6:
            window.blit(self.right, (self.x, self.y, self.width, self.height))

        elif self.walkDirection == 8:
            window.blit(self.up, (self.x, self.y, self.width, self.height))

        elif self.walkDirection == 2:
            window.blit(self.down, (self.x, self.y, self.width, self.height))



