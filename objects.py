from assettype import AssetType
from assetloader import Assetloader
import pygame
import random


class IObjects:

    # Interface Init
    def __init__(self, game):
        # X Koordinate des Items
        self.Item_X = 0
        # Y Koordinate des Items
        self.Item_Y = 0
        # Das Item als Bild
        self.Item = None
        # Das Item als Rect
        self.ItemRect = None
        # Item Ausrichtung
        self.Item_Angle = 0
        # Zufällige Geschwindigkeiten
        self.Item_Speed = random.randint(1, 4)
        # Zugriffsvariable 
        self.game = game

    # Methode zum Zeichnen der Objekte
    def draw(self):
        pass

    # Methode zum Updaten der Objekte
    def update(self):
        pass

    # Methode zum Laden der Objekte
    def loadImage(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        # Überprüfen ob ein Item die Koordinaten X,Y = 0 hat = Item wird gerade hinzugefügt
        if (self.Item_X == 0 and self.Item_Y == 0):
            # Zufalls X Koordinate
            randomwidth = random.randint(0, self.game.width - 80)
            # ItemRect erzeugen als Rect mit dem Zufalls X Wert
            self.ItemRect = pygame.Rect(randomwidth, self.Item_Y, 50, 50)
        else:
            # Item bereits bewegt, deswegen das neue ItemRect zurückliefern mit den neuen Y Koordinaten
            self.ItemRect = pygame.Rect(self.ItemRect[0], self.Item_Y, 50, 50)
        # ItemRect zurückgeben
        return self.ItemRect

    # Methode zum Bewegen eines Objektes
    def moveItemRect(self):
        # Item um sich selbst drehen lassen
        self.Item = pygame.transform.rotate(self.Item, self.Item_Angle)
        # Item runterskalieren
        self.Item = pygame.transform.scale(self.Item, (50, 50))

        # Überprüfung ob das Item Y innerhalb des Bildschirms ist
        if (self.Item_Y <= (self.game.height - 50)):
            # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
            self.Item_Y  = self.Item_Y + self.Item_Speed
        # Item zeichnen
        self.game.screen.blit(self.Item, self.ItemRect)
        # Item Rotation erhöhen
        self.Item_Angle = self.Item_Angle + 1


# Rüstungsitemobjekt
class ArmorItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        self.ItemRect = self.getItemRect()

    # Override der Lade Bild Methode
    def loadImage(self):
        # Item Bild laden
        self.Item = Assetloader.getAsset(AssetType.Items, "Armor_Bonus.png")
   
# Lebensitemobjekt
class HealthItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        self.ItemRect = self.getItemRect()

    # Override der Lade Bild Methode
    def loadImage(self):
        # Item Bild laden
        self.Item = Assetloader.getAsset(AssetType.Items, "HP_Bonus.png")

# DamageBoostItemobject
class DamageBoostItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        self.ItemRect = self.getItemRect()
 
    # Override der Lade Bild Methode
    def loadImage(self):
        # Item Bild laden
        self.Item = Assetloader.getAsset(AssetType.Items, "Damage_Bonus.png")

