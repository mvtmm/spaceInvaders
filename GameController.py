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

        # Spielbreite festlegen
        self.width      = width
        # Spielhöhe festlegen
        self.height     = height
        # Bildschirm mit Breite und Höhe anlegen
        self.screen     = pygame.display.set_mode((width, height))
        # Spielzeit anlegen
        self.clock      = pygame.time.Clock()
        # LocalPlayer mit Anfangsschiff hinzufügen
        self.Player     = LocalPlayer(self, width / 2, height - 20, Ship_Five)
        # Spielobjekte anlegen
        self.Object     = LocalObjects(self)
        # Gegner anlegen
        self.Enemys     = Enemy_One()
        # Bedingung für die Schleife, Spielabbruch
        quitgame        = False

        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(DamageBoostItemObject(self))
        self.Object.addObject(HealthItemObject(self))

        # Spielschleife
        while not quitgame:    

            # Variable die gedrückte Tasten innehat
            keypress = pygame.key.get_pressed()  

            # Pfeiltaste nach unten Event
            if keypress[pygame.K_DOWN]:
                # Überprüfung ob Spielerschiff innerhalb des sichtbaren Bereichs ist
                if (self.Player.PlayerY >= self.height - 0 and self.Player.PlayerY <= (self.height + self.Player.PlayerShip.PlayerShipRectSize[1])): 
                    # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                    self.Player.PlayerY = self.height
                else: 
                    # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                    self.Player.PlayerY += self.Player.PlayerShip.speed 

            # Pfeiltaste nach oben Event
            if keypress[pygame.K_UP]: 

                if (self.Player.PlayerY <= self.Player.PlayerShip.PlayerShipRectSize[1] + (self.Player.PlayerShip.PlayerShipRectSize[1] / 2)): 
                    # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                    self.Player.PlayerY = self.Player.PlayerShip.PlayerShipRectSize[1] + (self.Player.PlayerShip.PlayerShipRectSize[1] / 2)
                else:
                    # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                    self.Player.PlayerY -= self.Player.PlayerShip.speed 

            # Pfeiltaste nach Links Event
            if keypress[pygame.K_LEFT]: 

                if self.Player.PlayerX <= (self.Player.PlayerShip.PlayerShipRectSize[0] / 2):
                    # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                    self.Player.PlayerX = (self.Player.PlayerShip.PlayerShipRectSize[0] / 2)  
                else:
                    # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                    self.Player.PlayerX -= self.Player.PlayerShip.speed  

            # Pfeiltaste nach Rechts Event        
            if keypress[pygame.K_RIGHT]:

                if self.Player.PlayerX >= (self.width - self.Player.PlayerShip.PlayerShipRectSize[0]): 
                    # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                    self.Player.PlayerX = (width - self.Player.PlayerShip.PlayerShipRectSize[0])  
                else:
                    # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                    self.Player.PlayerX += self.Player.PlayerShip.speed     
               

            for pyevents in pygame.event.get():
                if pyevents.type == pygame.QUIT:
                    quitgame = True    

            pygame.display.flip()

            # FPS einstellen/ Ticks per Sek
            self.clock.tick(60)

            # Schwarzer Hintergrund
            self.screen.fill((0, 0, 0))

            # Spieler zeichnen
            self.Player.draw()
            # Gegner zeichnen
            self.Enemys.draw(self, 200, 200)
            # Objekte zeichnen
            self.Object.draw()

            # Item einsammeln Kollision
            # Iteration über alle gespawnten Items
            for items in self.Object.getObjects():
                # Check ob Spielership Items kollidieren
                if self.Player.PlayerShip.PlayerShipRect.colliderect(items.ItemRect):
                    # Item einsammeln
                    self.Object.removeObject(items)
                    # Eigenschaft verteilen
          

  

          


