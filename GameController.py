from playership import Ship_Five, Ship_One, Ship_Six, Ship_Two
from assettype import AssetType
from assetloader import Assetloader
import pygame
import pygame.display
from LocalPlayer import LocalPlayer
from daniel import *


class GameController:
    pygame.init()
    pygame.display.init()
    _screen = None
   
    def __init__(self, width, height):
        pygame.display.set_caption('Daniel ist schon ein bisschen komisch')

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        quitgame = False

        Player  = LocalPlayer(self, width / 2, height - 20, Ship_One)
        Enemy   = Enemy_One()
             
        while not quitgame:    
            keypress = pygame.key.get_pressed()   

            if keypress[pygame.K_DOWN]:
                    Player.y += Player.ship.speed 
            if keypress[pygame.K_UP]: 
                    Player.y -= Player.ship.speed 
            if keypress[pygame.K_LEFT]: 
                if Player.x > self.width:
                    Player.x = self.width
                else:
                    Player.x -= Player.ship.speed  
            if keypress[pygame.K_RIGHT]:
                if Player.x > self.width:
                    Player.x = self.width
                else:
                    Player.x += Player.ship.speed     

            for pyevents in pygame.event.get():
                if pyevents.type == pygame.QUIT:
                    quitgame = True    

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            Player.draw()
            Enemy.draw(self, 200, 200)
          


