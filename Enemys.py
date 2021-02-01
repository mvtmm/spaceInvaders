from Explosion import Explosion
from Assettype import AssetType
from Assetloader import Assetloader
import pygame
import random
from Konstanten import *
from Weapons import *
from random import randint
from LocalPlayer import *


class IEnemyShip:

    def __init__(self, game):
        # X Koordinate des Enemy
        self.ship_X = 0
        # Y Koordinate des Enemy
        self.ship_Y = 0
        # Enemy als Bild
        self.ship = None
        # Enemy als Rect
        self.shipRect = None
        # Zugriffsvariable
        self.game = game
        # Zählervariable
        self.move_counter = 0
        # Enemybewegung auf x-Achse, bei positivem Wert nach rechts, bei negativem Wert nach links
        self.move_direction_x = 0
        # Enemybewegung auf y-Achse
        self.move_direction_y = 0

    def trigger(self):
        pass

    # Methode zum Zeichnen der Enemys
    def draw(self):
        self.moveShipRect()

    # Methode zum Updaten der Enemys
    def update(self):
        pass

    # Enemys als Rect
    def getShipRect(self):
        self.shipRect = pygame.Rect(self.ship_X, self.ship_Y, 64, 32)
        return self.shipRect

    # Methode zum Bewegen der Enemys
    def moveShipRect(self):
        # Enemy von links nach rechts bewegen & nach unten
        self.ship_X += self.move_direction_x
        self.move_counter += 1
        if abs(self.move_counter) > 300:
            self.move_direction_x *= -1
            self.ship_Y += self.move_direction_y
            self.move_counter = 0

        # Enemys auf Bildschirm zeichnen
        self.game.game.screen.blit(self.ship, self.shipRect)


class Enemy_One(IEnemyShip):
    def __init__(self, game, row, cell):
        self.ship_X = (40 * row)
        self.ship_Y = (70 * cell)
        self.ship_Row = row
        self.ship_Cell = cell
        self.ship = None
        self.shipRect = None
        self.game = game
        self.move_counter = 0
        self.move_direction_x = 1
        self.move_direction_y = 25
        self.randomimage = randint(1, 5)

    # Override der Update Methode
    def update(self):
        # Grafik laden & Ship Rect erzeugen
        self.ship = Assetloader.getAsset(
            AssetType.Graphics, "Ship1_" + str(self.randomimage) + ".png")
        self.shipRect = self.getShipRect()

    # Override der Trigger Methode
    def trigger(self):
        self.game.game.enemys.removeObject(self)
        # Explosion als Animation anzeigen an der Position
        explosion = Explosion(self.ship_X+30, self.ship_Y+15)
        self.game.game.animations_Explosions.add(explosion)
        self.game.game.player.increaseScore(10)
