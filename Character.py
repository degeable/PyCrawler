import DungeonMap
import pygame
import random
from abc import abstractmethod, ABC

keys = 0
counter = 0


class Character(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,vel,map):
        pygame.sprite.Sprite.__init__(self)
        self.vel = vel
        #TODO plazer model based on type
        self.map = map
        self.left = pygame.image.load('src/Character/1.png').convert()
        self.right = pygame.image.load('src/Character/4.png').convert()
        self.up = pygame.image.load('src/Character/2.png').convert()
        self.down = pygame.image.load('src/Character/3.png').convert()
        self.walkCount = 0
        self.walkDirection = 8

    @abstractmethod
    def collision(self,blocksGroup):
        pass

    @abstractmethod
    def walk(self, window):
        pass

class Player(Character):
    def __init__(self,x,y,width,height,vel,map):
        super().__init__(x,y,width,height,vel,map)
        self.image = self.down
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.oldx = x
        self.oldy = y
        self.rect.width = width
        self.rect.height = height
        
    def collision(self,blocksGroup):
        hit_blocks = pygame.sprite.spritecollide(self,blocksGroup,False)
        for block in hit_blocks:
            print(block.getType())
            if block.getType() == "switch":
                print("stepped on switch!")
                block.onEnter()
            if block.blocking == True:
                self.rect.x = self.oldx
                self.rect.y  = self.oldy



    def walk(self, window):
        
        keys = pygame.key.get_pressed()
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
            self.collision(self.map.tiles)
            self.walkDirection = 4
            self.image = self.left
            self.image.set_colorkey((0,0,0))


        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
            self.collision(self.map.tiles)
            self.walkDirection = 6
            self.image = self.right
            self.image.set_colorkey((0,0,0))


        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
            self.collision(self.map.tiles)
            self.walkDirection = 8
            self.image = self.up
            self.image.set_colorkey((0,0,0))

        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel
            self.collision(self.map.tiles)
            self.walkDirection = 2
            self.image = self.down
            self.image.set_colorkey((0,0,0))


        


class WeakNpc(Character):
    def __init__(self,x,y,width,height,vel,map):
        super().__init__(x,y,width,height,vel,map)
        self.image = self.down
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.oldx = x
        self.oldy = y
        self.rect.width = width
        self.rect.height = height

    def collision(self,blocksGroup):
        if pygame.sprite.spritecollide(self,blocksGroup,False):
            self.rect.x = self.oldx
            self.rect.y = self.oldy 

    def walk(self, window):
        
        global counter
        global keys
        counter += 1
        
        if counter > keys+4:
            counter = 0
            keys =  random.randrange(1, 5, 1)
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        if keys == 1:
            self.rect.x -= self.vel
            self.walkDirection = 4
            self.image = self.left
            self.image.set_colorkey((0,0,0))


        if keys == 2:
            self.rect.x += self.vel
            self.walkDirection = 6
            self.image = self.right
            self.image.set_colorkey((0,0,0))

        if keys == 3:
            self.rect.y -= self.vel
            self.walkDirection = 8
            self.image = self.up
            self.image.set_colorkey((0,0,0))

        if keys == 4:
            self.rect.y += self.vel
            self.walkDirection = 2
            self.image = self.down
            self.image.set_colorkey((0,0,0))



