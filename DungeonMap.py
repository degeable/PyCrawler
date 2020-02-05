import pygame



class DungeonMap():
    """
    Represents the game map
    """

    def __init__(self,width=200, height=200):

        self.window = pygame.display.set_mode((width, height))
        self.window.fill((255, 255, 255))