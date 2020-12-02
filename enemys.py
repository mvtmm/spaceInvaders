from assettype import AssetType
from assetloader import Assetloader
import pygame
import random

class IEnemyShip:

    # Interface Init
    def __init__(self, game):
        # X Koordinate des Ship
        self.Ship_X = 0
        # Y Koordinate des Ship
        self.Ship_Y = 0
        # Das Ship als Bild
        self.Ship = None
        # Das Ship als Rect
        self.ShipRect = None
        # Zugriffsvariable 
        self.game = game
        # Zählervariable
        self.move_counter = 0
        # Ship bewegt sich nach rechts wegen positivem Wert
        self.move_direction = 1
        

    # Methode zum Zeichnen der Objekte
    def draw(self):
        self.moveShipRect()

    # Methode zum Updaten der Objekte
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getShipRect(self):
        self.ShipRect = pygame.Rect(self.Ship_X, self.Ship_Y, 200, 200)
        return self.ShipRect

    # Methode zum Bewegen eines Objektes
    def moveShipRect(self):
        # Ship um sich selbst drehen lassen
        self.Ship = pygame.transform.rotate(self.Ship, -90)
        # Ship runterskalieren auf 100x100
        self.Ship = pygame.transform.scale(self.Ship, (100, 100))
        
        self.Ship_X  += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 200:
            self.move_direction *= -1
            self.move_counter = self.move_direction * self.move_direction
        #print(self.Ship_X)
        #print(self.move_counter)
        # Überprüfung ob das Item X innerhalb des Bildschirms ist
        #if (self.Ship_X <= (self.game.width + (self.Ship_Row) - 100)):
        #    # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
        #    self.Ship_X  = self.Ship_X + self.Ship_Speed

        # Item zeichnen
        self.game.screen.blit(self.Ship, self.ShipRect)

        


class Enemy_One(IEnemyShip):
    def __init__(self, game, row, cell):
        # X Koordinate des Ship
        self.Ship_X = (40 * row)
        # Y Koordinate des Ship
        self.Ship_Y = (70 * cell)

        self.Ship_Row = row

        self.Ship_Cell = cell
        # Das Ship als Bild
        self.Ship = None
        # Das Ship als Rect
        self.ShipRect = None
        # Zugriffsvariable 
        self.game = game
        self.move_counter = 0
        self.move_direction = 1
        
    # Override der Update Methode
    def update(self):
        # Ship Rect erzeugen
        self.Ship = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
        self.ShipRect = self.getShipRect()

 
 