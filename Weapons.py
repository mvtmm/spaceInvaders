import pygame
from assettype import AssetType
from assetloader import Assetloader

class IWeapon:

    def __init__(self, game, rotation, direction, start_x, start_y):

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

        # Rotation für das Projektil
        self.rotation = rotation
        # Richtung für das Projektil
        self.direction = direction
        
        # Startwerte X
        self.StartProjectil_X = start_x
        # Startwert Y
        self.StartProjectil_Y = start_y

    # Methode zum Zeichnen des Projektiles
    def draw(self):
        pass

    # Methode zum Updaten des Projektiles
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        if self.direction == 0:
            if (self.Projectile_X == 0 and self.Projectile_Y == 0):
                 # Projektil über dem Schiff positionieren #17.12 X-Position +10 gesetzt, damit der shot aus der Mitte des Schiffes kommt
                self.Projectile_Rect = pygame.Rect(self.game.game.Player.PlayerShip.PlayerShipRect[0]+12, self.game.game.Player.PlayerShip.PlayerShipRect[1], 5, 50)
                self.Projectile_X = self.game.game.Player.PlayerShip.PlayerShipRect[0]
                self.Projectile_Y = self.game.game.Player.PlayerShip.PlayerShipRect[1]
            else:
                # Bewegen
                self.Projectile_Rect = pygame.Rect(self.Projectile_X +12, self.Projectile_Y, 5, 50)
        else:
            if (self.Projectile_X == 0 and self.Projectile_Y == 0):
                # Projectil über dem Schiff positionieren
                self.Projectile_Rect = pygame.Rect(100, 100, 50, 50)
                self.Projectile_X = self.StartProjectil_X
                self.Projectile_Y = self.StartProjectil_Y
            else:
               # Bewegen (X+10 gesetzt, damit der Schuss aus der Mitte des Schiffes abgefeuert wird)
                self.Projectile_Rect = pygame.Rect(self.Projectile_X+12, self.Projectile_Y, 5, 50)

        # ItemRect zurückgeben
        return self.Projectile_Rect

    # Methode zum Bewegen eines Objektes
    def moveItemRect(self):
        if self.direction == 0: # von unten nach oben
            # Überprüfung ob das Item Y innerhalb des Bildschirms ist
            if (self.Projectile_Y >= 15):
                # Item mit den zufälligen Item Speed von unten nach oben bewegen lassen
                self.Projectile_Y  = self.Projectile_Y - self.Projectile_Rect_Speed
            else:
                self.game.game.Player.RemovePlayerShoot(self)
            # Item zeichnen
            self.game.game.screen.blit(self.Projectile_Item, self.Projectile_Rect)
        else: ## Gegnerische Schüsse
            # Überprüfung ob das Item Y innerhalb des Bildschirms ist
            if (self.Projectile_Y <= 1000):
                # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
                self.Projectile_Y  = self.Projectile_Y + self.Projectile_Rect_Speed
            else:
                self.game.Enemys.RemoveEnemyShoot(self)
            # Item zeichnen
            self.game.screen.blit(self.Projectile_Item, self.Projectile_Rect)


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
        if self.Projectile_Item is None:
            self.Projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot2.png")
            # Item runterskalieren
            self.Projectile_Item = pygame.transform.scale(self.Projectile_Item, (50, 50))
            self.Projectile_Item = pygame.transform.rotate(self.Projectile_Item, self.rotation)
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
        if self.Projectile_Item is None:
            self.Projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot1.png")
            # Item runterskalieren
            self.Projectile_Item = pygame.transform.scale(self.Projectile_Item, (50, 50))
            self.Projectile_Item = pygame.transform.rotate(self.Projectile_Item, 90)
        self.Projectile_Rect = self.getItemRect()        

