from Weapons import *
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

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        # Überprüfen ob ein Item die Koordinaten X,Y = 0 hat = Item wird gerade hinzugefügt
        if (self.Item_X == 0 and self.Item_Y == 0):
            # Zufalls X Koordinate
            randomwidth = random.randint(0, self.game.game.width - 80)
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
        #self.Item = pygame.transform.rotate(self.Item, self.Item_Angle)
        # Item runterskalieren
       
        # Überprüfung ob das Item Y innerhalb des Bildschirms ist
        if (self.Item_Y <= (self.game.game.height - 50)):
            # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
            self.Item_Y  = self.Item_Y + self.Item_Speed
        else:
            # Objekte entfernen
            self.game.game.GameObjects.remove(self)

        # Item zeichnen
        self.game.game.screen.blit(self.Item, self.ItemRect)

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
        if self.Item is None:
            self.Item = Assetloader.getAsset(AssetType.Items, "Armor_Bonus.png")
            self.Item = pygame.transform.scale(self.Item, (50, 50))
        self.ItemRect = self.getItemRect()   

    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.game.Player.increaseArmor()
   
# Lebensitemobjekt
class HealthItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.Item is None:
            self.Item = Assetloader.getAsset(AssetType.Items, "HP_Bonus.png")
            self.Item = pygame.transform.scale(self.Item, (50, 50))
        self.ItemRect = self.getItemRect()

    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.game.Player.increaseHealth(10)

# DamageBoostItemobject
class SwitchWeaponItemObject(IObjects):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.Item is None:
            self.Item = Assetloader.getAsset(AssetType.Items, "Damage_Bonus.png")
            self.Item = pygame.transform.scale(self.Item, (50, 50))
        self.ItemRect = self.getItemRect()
 
    # Override der Item eingesammelt Methode
    def trigger(self):
        # Wenn mehrere Waffensysteme eingebaut werden kann hier das Waffen wechseln passieren
        if type(self.game.game.Player.PlayerShipWeapon).__name__  == "ProjectileWeapon":
            self.game.game.Player.PlayerShipWeapon = EnergyWeapon(self)
        
        


