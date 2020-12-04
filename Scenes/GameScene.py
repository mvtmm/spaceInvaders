from Explosion import Explosion
from Weapons import EnergyWeapon, ProjectileWeapon
from Meteors import MeteorItemObject
from objects import *
from playership import Ship_Five, Ship_One, Ship_Six, Ship_Two
from enemys import *
from assettype import AssetType
from assetloader import Assetloader
import pygame
import pygame.display
import random

from LocalPlayer import LocalPlayer
from LocalEnemys import LocalEnemys
from LocalObjects import LocalObjects

from konstanten import *
from SceneBase import SceneBase


class GameScene(SceneBase):
    pygame.init()
    pygame.display.init()
    _screen = None

    def __init__(self):
        pygame.display.set_caption('Daniel ist schon ein bisschen komisch')

        # Spielbreite festlegen
        self.width = width
        # Spielhöhe festlegen
        self.height = height
        # Bildschirm mit Breite und Höhe anlegen
        self.screen = pygame.display.set_mode((width, height))
        # Spielzeit anlegen
        self.clock = pygame.time.Clock()
        # LocalPlayer mit Anfangsschiff hinzufügen
        self.Player = LocalPlayer(self, width / 2, height - 20, Ship_Five, ProjectileWeapon)
        # Spielobjekte anlegen
        self.Object = LocalObjects(self)
        # Gegner anlegen
        self.Enemys = LocalEnemys(self)
        # Bedingung für die Schleife, Spielabbruch
        quitgame = False
        # Zeitstempel fürs Schießen
        self.VorherZeit = pygame.time.get_ticks()
        # Animationsgruppe
        self.Animations_Explosions = pygame.sprite.Group()


        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(SwitchWeaponItemObject(self))
        self.Object.addObject(HealthItemObject(self))

        self.Enemys.addObjectBundle(Enemy_One(self, 10 , 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 10 , 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 10 , 2))

        self.Enemys.addObjectBundle(Enemy_One(self, 11 , 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 11 , 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 11 , 2))

        self.Enemys.addObjectBundle(Enemy_One(self, 12 , 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 12 , 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 12 , 2))
        

        for i in range(5):
            self.Object.addObject(MeteorItemObject(self))

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
                    self.Player.PlayerY = self.Player.PlayerShip.PlayerShipRectSize[1] + (
                        self.Player.PlayerShip.PlayerShipRectSize[1] / 2)
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

            # Spieler schießt Waffen ab
            if keypress[pygame.K_SPACE]:
                # Zeitstempel
                time = pygame.time.get_ticks()
                if time - self.VorherZeit > 500:
                    self.VorherZeit = time
                    if type(self.Player.PlayerShipWeapon).__name__  == "ProjectileWeapon":
                        self.Player.PlayerShoot(ProjectileWeapon(self))
                    else:
                        self.Player.PlayerShoot(EnergyWeapon(self))
                    

            for pyevents in pygame.event.get():
                if pyevents.type == pygame.QUIT:
                    quitgame = True
           
                    
 

            pygame.display.flip()

            # FPS einstellen/ Ticks per Sek
            self.clock.tick(60)

            # Schwarzer Hintergrund
            self.screen.fill((0, 0, 0))

            # Items updaten
            self.Object.update()
            # Enemys updaten
            self.Enemys.update()
            # Spieler updaten
            self.Player.update()

            # Spieler zeichnen
            self.Player.draw()
            # Gegner zeichnen
            self.Enemys.draw()
            # Objekte zeichnen
            self.Object.draw()

            # Explosionen zeichnen
            self.Animations_Explosions.draw(self.screen)
            # Explosionen updaten
            self.Animations_Explosions.update()
         

            # Item einsammeln Kollision
            # Iteration über alle gespawnten Items
            for items in self.Object.getObjects():
                # Check ob Spielership Items kollidieren
                if self.Player.PlayerShip.PlayerShipRect.colliderect(items.ItemRect):
                    # Eigenschaft des Item verteilen
                    items.trigger()
                    # Item einsammeln & entfernen
                    self.Object.removeObject(items)

            # Iteration über alle Schüsse
            for projectile in self.Player.getProjectileObjects():

                # Check ob Projectile Gegner treffen
                for enemy in self.Enemys.getObjects():
                    # Wenn Kollision besteht dann entfernen
                    if enemy.ShipRect.colliderect(projectile.Projectile_Rect):
                        self.Enemys.removeObject(enemy)
                        # Explosion als Animation anzeigen an der Position
                        explosion = Explosion(enemy.Ship_X + 50, enemy.Ship_Y + 50)
                        self.Animations_Explosions.add(explosion)
                        # Projektil entfernen
                        self.Player.RemovePlayerShoot(projectile)



                # Check ob Meteore getroffen wurden
                for items in self.Object.getObjects():
                   # Wenn Meteor und Kollision besteht dann entfernen
                    if type(items).__name__ == "MeteorItemObject" and items.ItemRect.colliderect(projectile.Projectile_Rect):
                        self.Object.removeObject(items)
                        # Explosion als Animation anzeigen an der Position
                        explosion = Explosion(items.ItemRect[0] + 50, items.Item_Y + 50)
                        self.Animations_Explosions.add(explosion)
                        # Projektil entfernen
                        self.Player.RemovePlayerShoot(projectile)
