import DungeonMap
import pygame
import random
from abc import abstractmethod, ABC
import time
keys = 0
counter = 0


class Character(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,vel,health,hitpoints):
        pygame.sprite.Sprite.__init__(self)
        self.vel = vel
        #TODO player model based on type
        self.baseImage = pygame.image.load('src/Character/Char.png').convert()
        self.deadImage = pygame.image.load('src/Character/CharDead.png').convert()
        self.left = pygame.transform.rotate(self.baseImage,270)
        self.right = pygame.transform.rotate(self.baseImage,90)
        self.up = pygame.transform.rotate(self.baseImage,180)
        self.health = health
        self.isAlive = True
        self.weapon = None
        self.hitpoints = hitpoints
        self.strafeUpRight = pygame.transform.rotate(self.baseImage,135)
        self.strafeUpLeft = pygame.transform.rotate(self.baseImage,225)
        self.strafeDownRight = pygame.transform.rotate(self.baseImage,45)
        self.strafeDownLeft = pygame.transform.rotate(self.baseImage,315)
        
        self.down = self.baseImage
        #TODO FIGHT animation...
        #self.fightImage = pygame.image.load('src/Character/Char_attack.png').convert()
        self.walkCount = 0
        self.walkDirection = 8


    def attack(self,player):
        player.health -= self.hitpoints

    @abstractmethod
    def collision(self,blocksGroup):
        pass

    @abstractmethod
    def walk(self):
        pass

class Player(Character):
    def __init__(self,x,y,width,height,vel,health,hitpoints):
        super().__init__(x,y,width,height,vel,health,hitpoints)
        self.image = self.down
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.oldx = 0
        self.oldy = 0
        self.rect.width = width
        self.rect.height = height
        

    def collision(self,blocksGroup,playerGroup,itemSprites):
        hit_blocks = pygame.sprite.spritecollide(self,blocksGroup,False)
        for block in hit_blocks:
            if block.getType() == "switch":
                block.onEnter()
            if block.blocking == True:
                self.rect.x = self.oldx
                self.rect.y = self.oldy
        hit_players = pygame.sprite.spritecollide(self,playerGroup,False)
        hit_players.remove(self)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for player in hit_players:
                if player.__class__.__name__ is not 'healthbar':
                    self.attack(player)
                    print("Hit: "+str(self.hitpoints))
        hit_items = pygame.sprite.spritecollide(self,itemSprites,False)
        for item in hit_items:
            item.onPickup(self)
        0


    def walk(self,enemy,map,playerSprites,itemSprites):
        
        if self.health <= 0:
            self.isAlive = False


        keys = pygame.key.get_pressed()
        self.oldx = self.rect.x
        self.oldy = self.rect.y

        if keys[pygame.K_LEFT]:
            self.rect.center  = [self.rect.center[0] - self.vel,self.rect.center[1]]
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 4


        if keys[pygame.K_x]:
            print("Health: "+str(self.health))
            print("Hitpoints: "+str(self.hitpoints)) 

        if keys[pygame.K_RIGHT]:
            self.rect.center  = [self.rect.center[0] + self.vel,self.rect.center[1]]
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 6



        if keys[pygame.K_UP]:
            self.rect.center  = [self.rect.center[0] ,self.rect.center[1]- self.vel]
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 8


        if keys[pygame.K_DOWN]:
            self.rect.center  = [self.rect.center[0] ,self.rect.center[1] + self.vel]
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 2    

        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.walkDirection = 1
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.walkDirection = 3
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.walkDirection = 7
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.walkDirection = 9

        
        if self.walkDirection == 1:
            self.image = self.strafeDownLeft
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==2:
            self.image = self.down
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==3:
            self.image = self.strafeDownRight
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==4:
            self.image = self.left
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==6:
            self.image = self.right
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==7:
            self.image = self.strafeUpLeft
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==8:
            self.image = self.up
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==9:
            self.image = self.strafeUpRight
            self.image.set_colorkey((0,0,0)) 
            
        if self.weapon is not None:
             self.weapon.rect.x = self.rect.x-4
             self.weapon.rect.y = self.rect.y-8
             
 

class WeakNpc(Character):
    def __init__(self,x,y,width,height,vel,health,hitpoints):
        super().__init__(x,y,width,height,vel,health,hitpoints)
        self.image = self.down
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.oldx = x
        self.oldy = y
        self.vel = 1
        self.rect.width = width
        self.rect.height = height

    def collision(self,blocksGroup,playerGroup,itemSprites):
        hit_blocks = pygame.sprite.spritecollide(self,blocksGroup,False)
        for block in hit_blocks:
            if block.getType() == "switch":
                block.onEnter()
            if block.blocking == True:
                self.rect.x = self.oldx
                self.rect.y = self.oldy

    def walk(self,enemy,map,playerSprites,itemSprites):
        
        if self.health <= 0:
            self.isAlive = False


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
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 4
            self.image = self.left
            self.image.set_colorkey((0,0,0))


        if keys == 2:
            self.rect.x += self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 6
            self.image = self.right
            self.image.set_colorkey((0,0,0))

        if keys == 3:
            self.rect.y -= self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 8
            self.image = self.up
            self.image.set_colorkey((0,0,0))

        if keys == 4:
            self.rect.y += self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 2
            self.image = self.down
            self.image.set_colorkey((0,0,0))


class AttackNpc(Character):
    def __init__(self,x,y,width,height,vel,health,hitpoints):
        super().__init__(x,y,width,height,vel,health,hitpoints)
        self.image = self.down
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.oldx = x
        self.oldy = y
        self.vel = 1
        self.rect.width = width
        self.rect.height = height

    def collision(self,blocksGroup,playerGroup,itemSprites):
        hit_blocks = pygame.sprite.spritecollide(self,blocksGroup,False)
        for block in hit_blocks:
            if block.getType() == "switch":
                block.onEnter()
            if block.blocking == True:
                self.rect.x = self.oldx
                self.rect.y = self.oldy
        
        hit_players = pygame.sprite.spritecollide(self,playerGroup,False)
        hit_players.remove(self)
        for player in hit_players:
            if player.__class__.__name__ is not 'healthbar':
                self.attack(player)
                print("Hit: "+str(self.hitpoints))
                #TODO timed attacks!
        hit_items = pygame.sprite.spritecollide(self,itemSprites,False)
        for item in hit_items:
            item.onPickup(self)


    def roundMe(self, number):
        off = number % 32
        if off < 16:
            return number - off
        else:
            return number + (32 - off)

    def walk(self,enemy,map,playerSprites,itemSprites):
        if self.health <= 0:
            self.isAlive = False
        #TODO set an enemy and not just take player[0]
        toPathX = self.roundMe(enemy.rect.x)
        toPathY = self.roundMe(enemy.rect.y)
        fromPathX = self.roundMe(self.rect.x)
        fromPathY = self.roundMe(self.rect.y)

        path = map.getPathTo([fromPathX,fromPathY],[toPathX,toPathY])
        path.sort()

        self.oldx = self.rect.x
        self.oldy = self.rect.y

        if path[0][1] < self.rect.y:
            self.rect.y -= self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 8
    
        if path[0][1] > self.rect.y:
            self.rect.y += self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 2

        if path[0][0] < self.rect.x:
            self.rect.x -= self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 4

        if path[0][0] > self.rect.x:
            self.rect.x += self.vel
            self.collision(map.tiles,playerSprites,itemSprites)
            self.walkDirection = 6
        
        if path[0][0] < self.rect.x and path[0][1] > self.rect.y:
            self.walkDirection = 1
        if path[0][0] > self.rect.x and path[0][1] > self.rect.y:
            self.walkDirection = 3
        if path[0][0] < self.rect.x and path[0][1] < self.rect.y:
            self.walkDirection = 7
        if path[0][0] > self.rect.x and path[0][1] < self.rect.y:
            self.walkDirection = 9
        
        if self.walkDirection == 1:
            self.image = self.strafeDownLeft
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==2:
            self.image = self.down
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==3:
            self.image = self.strafeDownRight
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==4:
            self.image = self.left
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==6:
            self.image = self.right
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==7:
            self.image = self.strafeUpLeft
            self.image.set_colorkey((0,0,0)) 
        elif self.walkDirection ==8:
            self.image = self.up
            self.image.set_colorkey((0,0,0))
        elif self.walkDirection ==9:
            self.image = self.strafeUpRight
            self.image.set_colorkey((0,0,0)) 
            
        

