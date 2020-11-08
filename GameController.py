from LocalObjects import LocalObjects
from objects import ArmorItemObject, DamageBoostItemObject, HealthItemObject, IObjects
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

        self.width      = width
        self.height     = height
        self.screen     = pygame.display.set_mode((width, height))
        self.clock      = pygame.time.Clock()
        self.Player     = LocalPlayer(self, width / 2, height - 20, Ship_One)
        self.Object     = LocalObjects(self)
        self.Enemys     = Enemy_One()
        quitgame        = False

        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(DamageBoostItemObject(self))
        self.Object.addObject(HealthItemObject(self))
  
        while not quitgame:    
            keypress = pygame.key.get_pressed()   

            if keypress[pygame.K_DOWN]:

                if (self.Player.y >= self.height - 0 and self.Player.y <= (self.height + self.Player.imageRect[1])): 
                    self.Player.y = self.height
                else:
                    self.Player.y += self.Player.ship.speed 
               
            if keypress[pygame.K_UP]: 

                if (self.Player.y <= self.height - 0 and self.Player.y >= (self.height + self.Player.imageRect[1])): 
                    self.Player.y = 0
                else:
                    self.Player.y += self.Player.ship.speed 

            if keypress[pygame.K_LEFT]: 

                if self.Player.x <= 0: 
                    self.Player.x = 0
                else:
                    self.Player.x -= self.Player.ship.speed  
                    
            if keypress[pygame.K_RIGHT]:

                if self.Player.x >= (self.width - self.Player.imageRect[0]): 
                    self.Player.x = (width - self.Player.imageRect[0])  
                else:
                    self.Player.x += self.Player.ship.speed     
               

            for pyevents in pygame.event.get():
                if pyevents.type == pygame.QUIT:
                    quitgame = True    

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            # Spieler zeichnen
            self.Player.draw()
            # Gegner zeichnen
            self.Enemys.draw(self, 200, 200)
            # Objekte zeichnen
            self.Object.draw()

          


