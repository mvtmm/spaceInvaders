from Explosion import Explosion
from Weapons import EnergyWeapon, ProjectileWeapon
from Meteors import MeteorItemObject
from Objects import *
from Playership import *
from Enemys import *
from Assettype import AssetType
from Assetloader import Assetloader
import pygame
import pygame.display
import random

from Tastatur import *
from Levelmanager import *
from Level import *
from LocalPlayer import LocalPlayer
from LocalEnemys import LocalEnemys
from LocalObjects import LocalObjects

from Konstanten import *
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
        self.player = LocalPlayer(self, width / 2, height - 20, Ship_Five, ProjectileWeapon)
        # Spielobjekte anlegen
        self.Object = LocalObjects(self)
        # Gegner anlegen
        self.Enemys = LocalEnemys(self)
        # Bedingung für die Schleife, Spielabbruch
        quitgame = False
        # Zeitstempel fürs Schießen
        self.vorherZeit = pygame.time.get_ticks()
        # Animationsgruppe
        self.Animations_Explosions = pygame.sprite.Group()
        # Tastatur Invoker
        self.Tastatur = Invoker()
        # Levelmanager
        self.Levelmanager = Levelmanager(self)

        if (self.Levelmanager.level is None):
            self.Levelmanager.loadLevel(Level1(self))

     

        # Spielschleife
        while not quitgame:

            # Levelmanager updaten
            self.Levelmanager.update()

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
            self.screen.blit(self.Levelmanager.getBackground(),(0,0))            
            # Items updaten
            self.Object.update()
            # Enemys updaten
            self.Enemys.update()
            # Spieler updaten
            self.player.update()
            # Spieler zeichnen
            self.player.draw()
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
                if self.player.playerShip.playerShipRect.colliderect(items.itemRect):
                    # Eigenschaft des Item verteilen
                    items.trigger()
                    # Item einsammeln & entfernen
                    self.Object.removeObject(items)

            # Iteration über alle Schüsse
            for projectile in self.player.getProjectileObjects():

                # Check ob Projectile Gegner treffen
                for enemy in self.Enemys.getObjects():
                    # Wenn Kollision besteht dann entfernen
                    if enemy.shipRect.colliderect(projectile.projectile_Rect):
                        print("ShipRect",enemy.shipRect, "ProjectileRect",projectile.projectile_Rect)
                        self.Enemys.removeObject(enemy)
                        # Explosion als Animation anzeigen an der Position
                        explosion = Explosion(enemy.ship_X + 19, enemy.ship_Y + 64)
                        self.Animations_Explosions.add(explosion)
                        # Projektil entfernen
                        self.player.RemovePlayerShoot(projectile)



                # Check ob Meteore getroffen wurden
                for items in self.Object.getObjects():
                   # Wenn Meteor und Kollision besteht dann entfernen
                    if type(items).__name__ == "MeteorItemObject" and items.itemRect.colliderect(projectile.projectile_Rect):
                        self.Object.removeObject(items)
                        # Explosion als Animation anzeigen an der Position
                        explosion = Explosion(items.itemRect[0] + 50, items.item_Y + 50)
                        self.Animations_Explosions.add(explosion)
                        # Projektil entfernen
                        self.player.RemovePlayerShoot(projectile)

     
