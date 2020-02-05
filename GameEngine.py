import pygame
import pygame.freetype
import DungeonMap
import Character
pygame.init()

pygame.display.set_caption("PyCrawler1.0")
map_width = 600
map_height = 600
vel = 15
clock = pygame.time.Clock()

dungeon_map = DungeonMap.DungeonMap(map_width,map_height)
player1 = Character.Character(10,10,20,20)


def redrawGameWindow():
    #dungeon_map.window.blit((0,0,0), (0, 0))
    dungeon_map.window.fill((255, 255, 255))
    player1.walk(dungeon_map.window)
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


