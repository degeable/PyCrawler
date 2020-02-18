import pygame
import pygame.freetype
import DungeonMap
import Character
import Tile

pygame.init()

pygame.display.set_caption("PyCrawler1.0")
map_width = 610
map_height = 320
clock = pygame.time.Clock()

dungeon_map = DungeonMap.DungeonMap(map_width,map_height)
player1 = Character.Player(120,120,20,20,5,dungeon_map)
npc = Character.WeakNpc(320,250,20,20,5,dungeon_map)

playerSprites = pygame.sprite.Group()
playerSprites.add(player1)
playerSprites.add(npc)

def redrawGameWindow():
    dungeon_map.drawMap()
    player1.walk(dungeon_map.window)
    npc.walk(dungeon_map.window)
    playerSprites.update()
    playerSprites.draw(dungeon_map.window)
    pygame.display.update()

if __name__ == "__main__":
     print("hello")
     run = True
     while run:
         clock.tick(27)

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
         redrawGameWindow()


