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
        # Zufällige Geschwindigkeiten
        self.Ship_Speed = random.randint(1, 4)
        # Zugriffsvariable 
        self.game = game

    # Methode zum Zeichnen der Objekte
    def draw(self):
        pass

    # Methode zum Updaten der Objekte
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getShipRect(self):
        # Überprüfen ob ein Item die Koordinaten X,Y = 0 hat = Item wird gerade hinzugefügt
        if (self.Ship_X == 0 and self.Ship_Y == 0):
            # Zufalls X Koordinate
            randomwidth = random.randint(0, self.game.width - 80)
            # ItemRect erzeugen als Rect mit dem Zufalls X Wert
            self.ShipRect = pygame.Rect(randomwidth, self.Ship_Y, 50, 50)
        else:
            # Item bereits bewegt, deswegen das neue ItemRect zurückliefern mit den neuen Y Koordinaten
            self.ShipRect = pygame.Rect(self.ShipRect[0], self.Ship_Y, 50, 50)
        # ItemRect zurückgeben
        return self.ShipRect

    # Methode zum Bewegen eines Objektes
    def moveShipRect(self):
        # Item um sich selbst drehen lassen
        self.Ship = pygame.transform.rotate(self.Ship, -90)
        # Item runterskalieren
        self.Ship = pygame.transform.scale(self.Ship, (50, 50))
        # Überprüfung ob das Item Y innerhalb des Bildschirms ist
        if (self.Ship_Y <= (self.game.height - 50)):
            # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
            self.Ship_Y  = self.Ship_Y + self.Ship_Speed
        # Item zeichnen
        self.game.screen.blit(self.Ship, self.ShipRect)

        



class Enemy_One(IEnemyShip):
    speed = 2

    def draw(self):
        self.moveShipRect()
    
    # Override der Update Methode
    def update(self):
        # Ship Rect erzeugen
        self.Ship = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
        self.ShipRect = self.getShipRect()

 