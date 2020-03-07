import pygame
import pygame.freetype
import DungeonMap
import Character
import Tile
import healtbar
import Item
import Level
import itertools

pygame.init()
pygame.display.set_caption("PyCrawler1.0")


largeText = pygame.font.Font('freesansbold.ttf',40)
clock = pygame.time.Clock()

level = Level.Level("level.json")

def redrawGameWindow():
    level.map.drawMap()

    for character in level.characters:
        if character.isAlive:
            character.walk(level.characters[0],level.map,level.playerSprites,level.itemSprites)
        else:
            character.image = character.deadImage
            character.image.set_colorkey((0,0,0)) 
    for bar in level.healthbars:
        bar.update()
    for item in level.items:
        if item.pickedUp == True and item.type is not 'weapon':
            level.itemSprites.remove(item)
        if item.pickedUp == True and item.type is 'weapon':
            #img = level.item.image
            item.image  = pygame.transform.scale(item.image,(12,12))
  
    level.itemSprites.update()
    level.itemSprites.draw(level.map.window)
    level.playerSprites.update()
    level.playerSprites.draw(level.map.window)
    level.healthSprites.update()
    level.healthSprites.draw(level.map.window)
    pygame.display.update()

def text_objects(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()

def game_menu():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            intro = False
        level.map.window.fill((255,255,255))
        TextSurf,TextRect = text_objects("Hello! Welcome to PyCrawler!",largeText)
        #TODO get map width and height right here
        TextRect.center = ((576/2),(288/2))
        level.map.window.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(15)
    


def run():
     game_menu()
     
     run = True
     
     while run:
         clock.tick(27)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
         redrawGameWindow()
         


