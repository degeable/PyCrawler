import DungeonMap
import Item
import pygame
import Character
import healtbar
import json
class Level():

    def __init__(self,file):
        with open(file) as json_file:
            data = json.load(json_file)
        self.map = self.loadMap(data["map"]["src"],data["doors"].items(),data["switches"].items(),int(data["map"]["width"]),int(data["map"]["height"]))
        self.characters = self.loadCharacters(data["player"].items())
        self.healthbars = self.loadHealthbars()
        self.items = self.loadItems(data["items"].items())
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


    def loadMap(self,file,doors,switches,width,height):
        return DungeonMap.DungeonMap(width,height,file,doors,switches)

    def loadCharacters(self,player):
        characters = []
        for p in player:
            chars = str(p[1]).split()
            print(chars)
            if chars[0] == 'P':
                characters.append(Character.Player(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6]), int (chars[7])))
            elif chars[0] == 'A':
                characters.append(Character.AttackNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6]), int (chars[7])))
            elif chars[0] == 'W':
                characters.append(Character.WeakNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6]), int (chars[7])))
            elif chars[0] == 'S':
                characters.append(Character.StationaryNpc(int(chars[1]),int(chars[2]),int(chars[3]),int(chars[4]),int(chars[5]),int(chars[6]), int (chars[7])))
        return characters

    def loadHealthbars(self):
        bars = []
        for player in self.characters:
            bars.append(healtbar.healthbar(player))
        return bars

    def loadItems(self,item):
        items = []
        for i in item:
            chars = str(i[1]).split()
            if chars[0] == 'PB':
                items.append(Item.Pot('blue',int(chars[1]),int(chars[2]),int(chars[3])))
            elif chars[0] == 'PR':
                items.append(Item.Pot('red',int(chars[1]),int(chars[2]),int(chars[3])))
            elif chars[0] == 'S':
                items.append(Item.Sword(int(chars[1]),int(chars[2]),int(chars[3])))
        return items

