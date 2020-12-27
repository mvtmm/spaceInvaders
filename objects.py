from Weapons import *
from Assettype import AssetType
from Assetloader import Assetloader
import pygame
import random


class IObjects:

    # Interface Init
    def __init__(self, game):
        # X Koordinate des Items
        self.item_X = 0
        # Y Koordinate des Items
        self.item_Y = 0
        # Das Item als Bild
        self.item = None
        # Das Item als Rect
        self.itemRect = None
        # Item Ausrichtung
        self.item_Angle = 0
        # Zufällige Geschwindigkeiten
        self.item_Speed = random.randint(1, 4)
        # Zugriffsvariable 
        self.game = game

    # Methode zum Zeichnen der Objekte
    def draw(self):
        pass

    # Methode zum Updaten der Objekte
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        # Überprüfen ob ein Item die Koordinaten X,Y = 0 hat = Item wird gerade hinzugefügt
        if (self.item_X == 0 and self.item_Y == 0):
            # Zufalls X Koordinate
            randomwidth = random.randint(0, self.game.game.width - 80)
            # ItemRect erzeugen als Rect mit dem Zufalls X Wert
            self.itemRect = pygame.Rect(randomwidth, self.item_Y, 50, 50)
        else:
            # Item bereits bewegt, deswegen das neue ItemRect zurückliefern mit den neuen Y Koordinaten
            self.itemRect = pygame.Rect(self.itemRect[0], self.item_Y, 50, 50)
        # ItemRect zurückgeben
        return self.itemRect

    # Methode zum Bewegen eines Objektes
    def moveItemRect(self):
        # Item um sich selbst drehen lassen
        #self.Item = pygame.transform.rotate(self.Item, self.Item_Angle)
        # Item runterskalieren
       
        # Überprüfung ob das Item Y innerhalb des Bildschirms ist
        if (self.item_Y <= (self.game.game.height - 50)):
            # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
            self.item_Y  = self.item_Y + self.item_Speed
        else:
            # Objekte entfernen
            self.game.game.gameObjects.remove(self)

        # Item zeichnen
        self.game.game.screen.blit(self.item, self.itemRect)

    # Methode sobald das Item eingesammelt wurde
    def trigger(self):
        pass

# Rüstungsitemobjekt
class ArmorItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.item is None:
            self.item = Assetloader.getAsset(AssetType.Items, "Armor_Bonus.png")
            self.item = pygame.transform.scale(self.item, (50, 50))
        self.itemRect = self.getItemRect()   

    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.game.player.increaseArmor()
   
# Lebensitemobjekt
class HealthItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.item is None:
            self.item = Assetloader.getAsset(AssetType.Items, "HP_Bonus.png")
            self.item = pygame.transform.scale(self.item, (50, 50))
        self.itemRect = self.getItemRect()

    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.game.player.increaseHealth(10)

# DamageBoostItemobject
class SwitchWeaponItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.item is None:
            self.item = Assetloader.getAsset(AssetType.Items, "Damage_Bonus.png")
            self.item = pygame.transform.scale(self.item, (50, 50))
        self.itemRect = self.getItemRect()
 
    # Override der Item eingesammelt Methode
    def trigger(self):
        # Wenn mehrere Waffensysteme eingebaut werden kann hier das Waffen wechseln passieren
        if type(self.game.game.player.playerShipWeapon).__name__  == "ProjectileWeapon":
            self.game.game.player.playerShipWeapon = EnergyWeapon(self, -90, 0, 0, 0)
        
        


