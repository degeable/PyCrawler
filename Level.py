import DungeonMap
import Item
import pygame
import Character

class Level():

    def __init__(self,file,width,height):
        self.map = loadMap(file[0],width,height)
        self.characters = loadCharacters(file[1])
        self.items = loadItems(file[2])
        self.fin = False
        self.itemSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        for (it,char) in zip(self.items, self.characters):
            self.itemSprites.add(it)
            self.playerSprites.add(char)


    def loadMap(file,width,height)
        return DungeonMap.DungeonMap(map_width,map_height)

    def loadCharacters(file):
        characters = []
        inputFile = open(file)
        lines = inputFile.read().split()
        for line in lines:
            chars = list(line)
            if chars[0] == 'P':
                characters.append(Character.Player(chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7]))
            elif chars[0] == 'A':
                characters.append(Character.AttackNpc(chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7]))
            elif chars[0] == 'D':
                characters.append(Character.WeakNpc(chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7]))
            elif chars[0] == 'S':
                characters.append(Character.StationaryNpc(chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7]))
        return characters

    def loadItems(file):
        items = []
        inputFile = open(file)
        lines = inputFile.read().split()
        for line in lines:
            chars = list(line)
            if chars[0] = 'PB'
                items.append(Item.Pot('blue',chars[1],cjars[2],chars[3]))
            if chars[0] = 'PR'
                items.append(Item.Pot('red',chars[1],chars[2],chars[3]))
            if chars[0] = 'S'
                items.append(Item.Sword(chars[1],chars[2],chars[3]))
        return items