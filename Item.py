import pygame
from abc import abstractmethod, ABC

class Item(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None

    @abstractmethod
    def onPickup(self,player):
        pass

      
class Pot(Item):

    def __init__(self,color,x,y, impact):
        super().__init__()
        self.image = pygame.image.load('src/Textures/Items/'+color+'Pot.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 16
        self.rect.height = 16
        self.color = color
        self.healthImpact = impact
        self.pickedUp = False

    def onPickup(self,player):
        player.health += self.healthImpact
        self.pickedUp = True
        print("Picked up "+self.color+" Pot")

class Sword(Item):

    def __init__(self,x,y,impact):
        super().__init__()
        self.image = pygame.image.load('src/Textures/Items/sword.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 16
        self.rect.height = 16
        self.hitpoints = 5
        self.pickedUp = False

    def onPickup(self,player):
        player.hitpoints = self.hitpoints
        self.pickedUp = True
        print("Picked up Sword")

    
