from Explosion import Explosion
from Weapons import EnergyWeapon, ProjectileWeapon
from Meteors import MeteorItemObject
from objects import *
from playership import *
from enemys import *
from assettype import AssetType
from assetloader import Assetloader
import pygame
import pygame.display
import random

from Tastatur import *

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
        # Tastatur Invoker
        self.Tastatur = Invoker()

        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(ArmorItemObject(self))
        self.Object.addObject(SwitchWeaponItemObject(self))
        self.Object.addObject(HealthItemObject(self))

        self.Enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 5, 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.Enemys.addObjectBundle(Enemy_One(self, 6, 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 6,  2))

        self.Enemys.addObjectBundle(Enemy_One(self, 7, 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 7, 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 7,  2))
        
        self.Enemys.addObjectBundle(Enemy_One(self, 8, 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 8, 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 8,  2))
        
        
        self.Enemys.addObjectBundle(Enemy_One(self, 9, 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 9, 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 9,  2))
        
        
        self.Enemys.addObjectBundle(Enemy_One(self, 10 , 0))
        self.Enemys.addObjectBundle(Enemy_One(self, 10 , 1))
        self.Enemys.addObjectBundle(Enemy_One(self, 10,  2))

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

            command_Down    = PlayerDown(self)
            command_Up      = PlayerUp(self)
            command_Right   = PlayerRight(self)
            command_Left    = PlayerLeft(self)
            command_Space   = PlayerSpace(self)

            self.Tastatur.setBefehl(pygame.K_DOWN,      command_Down)
            self.Tastatur.setBefehl(pygame.K_UP,        command_Up)
            self.Tastatur.setBefehl(pygame.K_RIGHT,     command_Right)
            self.Tastatur.setBefehl(pygame.K_LEFT,      command_Left)
            self.Tastatur.setBefehl(pygame.K_SPACE,     command_Space)

            self.Tastatur.PressedKey(pygame.key.get_pressed())

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

            for projectile in self.Enemy.getProjectileObjects():
                for 
