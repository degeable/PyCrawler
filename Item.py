import pygame
from abc import abstractmethod, ABC

class Item(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

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
        self.type = 'pot'

    def onPickup(self,player):
        if self.color == "blue":
            player.health -= self.healthImpact
        elif self.color == "red":
            player.health += self.healthImpact
            #TODO get a player.maxhealth variable and check for that (later for items)
            if player.health >= 10:
                player.health = 10
        self.pickedUp = True
        print("Picked up "+self.color+" Pot with impact: "+str(self.healthImpact))

class Weapon(Item):

    def __init__(self):
        super().__init__()
        self.type = 'weapon'

    def onPickup(self,player):
        self.rect.width = 2
        self.rect.height = 2
        player.hitpoints = self.hitpoints
        player.weapon = self
        self.pickedUp = True
        print("Picked up a Weapon")

class Sword(Weapon):

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

