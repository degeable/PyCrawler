import DungeonMap
import Item
import pygame
import Character
import healtbar

class Level():

    def __init__(self,file,width,height):
        self.map = self.loadMap(file[0],width,height)
        self.characters = self.loadCharacters(file[1])
        self.healthbars = self.loadHealthbars()
        self.items = self.loadItems(file[2])
        self.fin = False
        self.itemSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.healthSprites = pygame.sprite.Group()
        for it in self.items:
            self.itemSprites.add(it)
        for char in self.characters: 
            self.playerSprites.add(char)
        for bar in self.healthbars:
            self.healthSprites.add(bar)


    def loadMap(self,file,width,height):
        return DungeonMap.DungeonMap(width,height)

    def loadCharacters(self,file):
        characters = []
        inputFile = open(file)
        lines = inputFile.read().split("\n")
        for line in lines:
            chars = str(line).split()
            if chars[0] == 'P':
                characters.append(Character.Player(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6])))
            elif chars[0] == 'A':
                characters.append(Character.AttackNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6])))
            elif chars[0] == 'W':
                characters.append(Character.WeakNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6])))
            elif chars[0] == 'S':
                characters.append(Character.StationaryNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6])))
        return characters

    def loadHealthbars(self):
        bars = []
        for player in self.characters:
            bars.append(healtbar.healthbar(player))
        return bars

    def loadItems(self,file):
        items = []
        inputFile = open(file)
        lines = inputFile.read().split("\n")
        for line in lines:
            chars = str(line).split()
            if chars[0] == 'PB':
                items.append(Item.Pot('blue',int(chars[1]),int(chars[2]),int(chars[3])))
            elif chars[0] == 'PR':
                items.append(Item.Pot('red',int(chars[1]),int(chars[2]),int(chars[3])))
            elif chars[0] == 'S':
                items.append(Item.Sword(int(chars[1]),int(chars[2]),int(chars[3])))
        return items

