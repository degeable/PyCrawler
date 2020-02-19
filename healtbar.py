import Character
import pygame

class healthbar(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.h10 =   pygame.image.load('src/Character/health10.png').convert()
        self.h9 =   pygame.image.load('src/Character/health9.png').convert()
        self.h8 =  pygame.image.load('src/Character/health8.png').convert()
        self.h7 =  pygame.image.load('src/Character/health7.png').convert()
        self.h6 =  pygame.image.load('src/Character/health6.png').convert()
        self.h5 =  pygame.image.load('src/Character/health5.png').convert()
        self.h4 =  pygame.image.load('src/Character/health4.png').convert()
        self.h3 =  pygame.image.load('src/Character/health3.png').convert()
        self.h2 =   pygame.image.load('src/Character/health2.png').convert()
        self.h1 =  pygame.image.load('src/Character/health1.png').convert()
        self.h0 =  pygame.image.load('src/Character/health0.png').convert()
        self.image = self.h10
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def update(self):
        if self.player.health == 10:
            self.image = self.h10
        if self.player.health == 9:
            self.image = self.h9
        if self.player.health == 8:
            self.image = self.h8
        if self.player.health == 9:
            self.image = self.h9
        if self.player.health == 8:
            self.image = self.h8
        if self.player.health == 7:
            self.image = self.h7
        if self.player.health == 6:
            self.image = self.h6
        if self.player.health == 5:
            self.image = self.h5
        if self.player.health == 4:
            self.image = self.h4
        if self.player.health == 3:
            self.image = self.h3
        if self.player.health == 2:
            self.image = self.h2
        if self.player.health == 1:
            self.image = self.h1
        if self.player.health == 0:
            self.image = self.h0
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y