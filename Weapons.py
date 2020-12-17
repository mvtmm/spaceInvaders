import pygame
from assettype import AssetType
from assetloader import Assetloader

class IWeapon:

    def __init__(self, game):

        # Das Projektil als Bild
        self.Projectile_Item = None
        # Das Item als Rect
        self.Projectile_Rect = None
        # Zufällige Geschwindigkeiten
        self.Projectile_Rect_Speed = 6
        # Zugriffsvariable
        self.game = game
        
        # X Koordinate des Projektil
        self.Projectile_X = 0
        # Y Koordinate des Projektil
        self.Projectile_Y = 0

 

    # Methode zum Zeichnen des Projektiles
    def draw(self):
        pass

    # Methode zum Updaten des Projektiles
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        if (self.Projectile_X == 0 and self.Projectile_Y == 0):
            # Projektil über dem Schiff positionieren #17.12 X-Position +10 gesetzt, damit der shot aus der Mitte des Schiffes kommt
            self.Projectile_Rect = pygame.Rect(self.game.game.Player.PlayerShip.PlayerShipRect[0]+12, self.game.game.Player.PlayerShip.PlayerShipRect[1], 5, 50)
            self.Projectile_X = self.game.game.Player.PlayerShip.PlayerShipRect[0]
            self.Projectile_Y = self.game.game.Player.PlayerShip.PlayerShipRect[1]
        else:
            # Bewegen (X+10 gesetzt, damit der Schuss aus der Mitte des Schiffes abgefeuert wird)
            self.Projectile_Rect = pygame.Rect(self.Projectile_X+12, self.Projectile_Y, 5, 32)
          
        # ItemRect zurückgeben
        return self.Projectile_Rect

    # Methode zum Bewegen eines Objektes
    def moveItemRect(self):
        # Item runterskalieren

        # Überprüfung ob das Item Y innerhalb des Bildschirms ist

        if (self.Projectile_Y >= 15):
            # Item mit den zufälligen Item Speed von unten nach oben bewegen lassen
            self.Projectile_Y  = self.Projectile_Y - self.Projectile_Rect_Speed
        else:
            self.game.game.Player.RemovePlayerShoot(self)
        # Item zeichnen
        self.game.game.screen.blit(self.Projectile_Item, self.Projectile_Rect)


class ProjectileWeapon(IWeapon):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Image laden für das Projektil
        if self.Projectile_Item is None:
            self.Projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot2small.png")
            self.Projectile_Item = pygame.transform.scale(self.Projectile_Item, (32, 8))
            self.Projectile_Item = pygame.transform.rotate(self.Projectile_Item, -90)
        # Item Rect erzeugen
        self.Projectile_Rect = self.getItemRect()   

class EnergyWeapon(IWeapon):

    # Override der Draw Methode
    def draw(self):
        self.Projectile_Rect_Speed = 9
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        self.Projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot1small.png")
        self.Projectile_Item = pygame.transform.scale(self.Projectile_Item, (32, 8))
        self.Projectile_Item = pygame.transform.rotate(self.Projectile_Item, 90)
        self.Projectile_Rect = self.getItemRect()        

