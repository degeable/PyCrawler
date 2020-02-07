import DungeonMap
import pygame

class Character():

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = pygame.image.load('src/Character/1.png')
        self.right = pygame.image.load('src/Character/4.png')
        self.up = pygame.image.load('src/Character/2.png')
        self.down = pygame.image.load('src/Character/3.png')
        self.walkCount = 0
        self.walkDirection = 8



    def walk(self, window):

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
            window.blit(self.up, (self.x, self.y, self.width, self.height))

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.walkDirection = 2
            window.blit(self.down, (self.x, self.y, self.width, self.height))

        if self.walkDirection == 4:
            window.blit(self.left, (self.x, self.y, self.width, self.height))
        elif self.walkDirection == 6:
            window.blit(self.right, (self.x, self.y, self.width, self.height))
        elif self.walkDirection == 8:
            window.blit(self.up, (self.x, self.y, self.width, self.height))
        elif self.walkDirection == 2:
            window.blit(self.down, (self.x, self.y, self.width, self.height))





