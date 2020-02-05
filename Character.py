import DungeonMap
import pygame

class Character():

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        #self.isJump = False
        #self.left = False
        #self.right = False
        self.walkCount = 0
        #self.jumpCount = 10
        #self.standing = True


    def walk(self, window):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))
