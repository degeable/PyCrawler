import pygame
import pygame.freetype
import DungeonMap
import Character
import Tile
import healtbar

pygame.init()
pygame.display.set_caption("PyCrawler1.0")


largeText = pygame.font.Font('freesansbold.ttf',40)
map_width = 610
map_height = 320
clock = pygame.time.Clock()

dungeon_map = DungeonMap.DungeonMap(map_width,map_height)
player1 = Character.Player(120,120,20,20,5,dungeon_map)
npc = Character.WeakNpc(320,250,20,20,5,dungeon_map)
healthPlayer1 = healtbar.healthbar(player1)
healthNpc = healtbar.healthbar(npc)
playerSprites = pygame.sprite.Group()
playerSprites.add(player1)
playerSprites.add(healthPlayer1)
playerSprites.add(healthNpc)
playerSprites.add(npc)

def redrawGameWindow():
    dungeon_map.drawMap()
    if player1.isAlive:
        player1.walk(dungeon_map.window,playerSprites)
        healthPlayer1.update()
    if npc.isAlive:
        npc.walk(dungeon_map.window)
        healthNpc.update()

    playerSprites.update()
    playerSprites.draw(dungeon_map.window)
    pygame.display.update()

def text_objects(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            intro = False
        dungeon_map.window.fill((255,255,255))
        TextSurf,TextRect = text_objects("Hello! Welcome to PyCrawler!",largeText)
        TextRect.center = ((map_width/2),(map_height/2))
        dungeon_map.window.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(15)
    



if __name__ == "__main__":
     game_intro()
     run = True
     while run:
         clock.tick(27)

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
         redrawGameWindow()


